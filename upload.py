from azure.storage.blob import ContainerClient, ContentSettings
import os

CONTAINER_SAS_URL = "https://alumniweb.blob.core.windows.net/envision?sp=racwdli&st=2025-04-20T18:22:25Z&se=2026-09-01T02:22:25Z&sv=2024-11-04&sr=c&sig=4%2FR8MsjueAaD8EnHy9iqCSKpXo6X1MBes%2BuKTz9DWaY%3D"  # Use correct SAS here
FOLDER_PATH = "/home/sai/Data/bucket/upload/"

def upload_image(image_path):
    try:
        container_client = ContainerClient.from_container_url(CONTAINER_SAS_URL)
        blob_name = os.path.basename(image_path)
        blob_client = container_client.get_blob_client(blob_name)

        with open(image_path, "rb") as data:
            blob_client.upload_blob(
                data,
                overwrite=True,
                content_settings=ContentSettings(content_type="image/jpeg")
            )

        print(f"✅ Uploaded: {blob_client.url}")
    except Exception as e:
        print(f"❌ Error uploading {image_path}: {e}")

if __name__ == "__main__":
    for file in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, file)
        if os.path.isfile(file_path):
            upload_image(file_path)
