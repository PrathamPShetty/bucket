from azure.storage.blob import ContainerClient
import os

# Replace this with your container SAS URL
CONTAINER_SAS_URL = "https://alumniweb.blob.core.windows.net/envision?sp=racwdli&st=2025-04-20T18:22:25Z&se=2026-09-01T02:22:25Z&sv=2024-11-04&sr=c&sig=4%2FR8MsjueAaD8EnHy9iqCSKpXo6X1MBes%2BuKTz9DWaY%3D"

# Local directory to save downloaded images
DOWNLOAD_PATH = "/home/sai/Data/bucket/downloaded/"

# Ensure the directory exists
os.makedirs(DOWNLOAD_PATH, exist_ok=True)

def download_blobs():
    try:
        container_client = ContainerClient.from_container_url(CONTAINER_SAS_URL)
        blobs = container_client.list_blobs()

        for blob in blobs:
            blob_name = blob.name
            file_path = os.path.join(DOWNLOAD_PATH, blob_name)
            print(f"⬇️ Downloading {blob_name}...")

            with open(file_path, "wb") as file:
                download_stream = container_client.download_blob(blob_name)
                file.write(download_stream.readall())

            print(f"✅ Downloaded to {file_path}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    download_blobs()
