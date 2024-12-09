from flask import Flask, render_template, request, redirect, url_for, jsonify # type: ignore
from blob_utils import read_comments, write_comments
from azure.ai.textanalytics import TextAnalyticsClient # type: ignore # type: ignore
from azure.core.credentials import AzureKeyCredential # type: ignore
import json
import os

# Affichage des variables d'environnement pour débogage
print("AZURE_STORAGE_ACCOUNT:", os.getenv("AZURE_STORAGE_ACCOUNT"))
print("AZURE_STORAGE_KEY:", os.getenv("AZURE_STORAGE_KEY"))

# Configuration pour Azure Text Analytics
TEXT_ANALYTICS_ENDPOINT = os.getenv("TEXT_ANALYTICS_ENDPOINT")  # Endpoint de Text Analytics
TEXT_ANALYTICS_KEY = os.getenv("TEXT_ANALYTICS_KEY")            # Clé de Text Analytics

if not TEXT_ANALYTICS_ENDPOINT or not TEXT_ANALYTICS_KEY:
    raise ValueError("Les variables TEXT_ANALYTICS_ENDPOINT et TEXT_ANALYTICS_KEY ne sont pas définies.")

credential = AzureKeyCredential(TEXT_ANALYTICS_KEY)
text_analytics_client = TextAnalyticsClient(endpoint=TEXT_ANALYTICS_ENDPOINT, credential=credential)

app = Flask(__name__)

# Fonction pour analyser la tonalité
def analyze_sentiment(comment):
    try:
        response = text_analytics_client.analyze_sentiment(documents=[comment])[0]
        return response.sentiment  # Retourne 'positive', 'neutral', ou 'negative'
    except Exception as e:
        print(f"Erreur lors de l'analyse de la tonalité : {e}")
        return "unknown"

# Page principale : liste des articles
@app.route('/')
def index():
    articles = [
        {"id": 1, "title": "Introduction à mon blog", "content": "Bienvenue sur mon blog personnel !"},
        {"id": 2, "title": "Mes inspirations", "content": "Découvrez mes inspirations pour ce blog."},
    ]
    return render_template('index.html', articles=articles)

# Page pour un article spécifique
@app.route('/article/<int:article_id>')
def article(article_id):
    articles = {
        1: {"title": "Introduction à mon blog", "content": "Bienvenue sur mon blog personnel !"},
        2: {"title": "Mes inspirations", "content": "Découvrez mes inspirations pour ce blog."},
    }
    article = articles.get(article_id)
    if not article:
        return "Article introuvable", 404

    # Charger les commentaires depuis Azure Blob Storage
    comments = read_comments()
    if comments:
        comments_data = json.loads(comments).get(str(article_id), [])
    else:
        comments_data = []

    return render_template('article.html', article=article, article_id=article_id, comments=comments_data)

# Soumettre un commentaire
@app.route('/submit_comment/<int:article_id>', methods=['POST'])
def submit_comment(article_id):
    comment = request.form.get("comment")
    if not comment:
        return "Commentaire vide", 400

    # Analyser la tonalité du commentaire
    sentiment = analyze_sentiment(comment)

    # Charger les commentaires existants depuis Azure Blob Storage
    comments = read_comments()
    if comments:
        comments_data = json.loads(comments)
    else:
        comments_data = {}

    # Ajouter le commentaire avec la tonalité
    if str(article_id) not in comments_data:
        comments_data[str(article_id)] = []
    comments_data[str(article_id)].append({"text": comment, "sentiment": sentiment})

    # Sauvegarder les commentaires dans Azure Blob Storage
    write_comments(json.dumps(comments_data))

    return redirect(url_for('article', article_id=article_id))

if __name__ == "__main__":
    app.run(debug=True)

