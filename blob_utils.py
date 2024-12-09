from azure.storage.blob import BlobServiceClient # type: ignore
import os
import time


# Configuration pour Azure Blob Storage
account_name = os.getenv("AZURE_STORAGE_ACCOUNT")  # Nom du compte (variable d'environnement)
account_key = os.getenv("AZURE_STORAGE_KEY")      # Clé de stockage (variable d'environnement)
container_name = "blogfiles"                      # Nom du conteneur

# Initialiser le client Blob
blob_service_client = BlobServiceClient(
    account_url=f"https://{account_name}.blob.core.windows.net",
    credential=account_key
)
blob_client = blob_service_client.get_blob_client(container=container_name, blob="comments.json")

# Lire les commentaires depuis Azure Blob Storage
def read_comments():
    for _ in range(3):  # 3 tentatives
        try:
            blob_data = blob_client.download_blob().readall()
            return blob_data.decode('utf-8')
        except Exception as e:
            print(f"Tentative échouée : {e}")
            time.sleep(2)
    return None

# Écrire des commentaires dans Azure Blob Storage
def write_comments(data):
    try:
        blob_client.upload_blob(data, overwrite=True)
        print("Données mises à jour avec succès dans Azure Blob Storage.")
    except Exception as e:
        print(f"Erreur lors de l'écriture : {e}")
