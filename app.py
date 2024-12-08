from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

# Vérifier si le fichier de stockage des commentaires existe
COMMENTS_FILE = "comments.json"
if not os.path.exists(COMMENTS_FILE):
    with open(COMMENTS_FILE, "w") as f:
        json.dump({}, f)

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

    # Charger les commentaires associés
    with open(COMMENTS_FILE, "r") as f:
        comments = json.load(f).get(str(article_id), [])

    return render_template('article.html', article=article, article_id=article_id, comments=comments)

# Soumettre un commentaire
@app.route('/submit_comment/<int:article_id>', methods=['POST'])
def submit_comment(article_id):
    comment = request.form.get("comment")
    if not comment:
        return "Commentaire vide", 400

    # Charger les commentaires existants
    with open(COMMENTS_FILE, "r") as f:
        comments = json.load(f)

    # Ajouter le commentaire
    if str(article_id) not in comments:
        comments[str(article_id)] = []
    comments[str(article_id)].append(comment)

    # Sauvegarder les commentaires
    with open(COMMENTS_FILE, "w") as f:
        json.dump(comments, f)

    return redirect(url_for('article', article_id=article_id))

if __name__ == "__main__":
    app.run(debug=True)
