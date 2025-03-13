import os
from azure.storage.blob import BlobServiceClient, ContentSettings

# ✅ Corrected Account URL (without SAS token)
ACCOUNT_URL = "https://alumniweb.blob.core.windows.net"
SAS_TOKEN = "sp=rw&st=2025-03-13T17:11:46Z&se=2025-03-15T01:11:46Z&sv=2022-11-02&sr=c&sig=pdw85jhXpVCvKtuKaXvP%2FMVFkbWYaIICSacye664AeM%3D"

container_name = "alumni/alumni"
folder_path = "D:/bucket/upload1/"  # Change this to your folder path

# ✅ Connect to Azure Blob Storage
blob_service_client = BlobServiceClient(account_url=ACCOUNT_URL, credential=SAS_TOKEN)
container_client = blob_service_client.get_container_client(container_name)

def upload_image(image_path):
    """Uploads an image to Azure Blob Storage and prints the public URL."""
    file_name = os.path.basename(image_path)  # Extract filename
    blob_name = f"{file_name}"  # Store inside "alumni/" container

    try:
        with open(image_path, "rb") as data:
            blob_client = container_client.get_blob_client(blob_name)

            # ✅ Upload the file
            blob_client.upload_blob(data, overwrite=True, content_settings=ContentSettings(content_type="image/jpeg"))

            # ✅ Construct and print the public URL
            blob_url = f"{ACCOUNT_URL}/{container_name}/{blob_name}"
            print(f"✅ Uploaded: {blob_url}")

    except Exception as e:
        print(f"❌ Upload failed for {image_path}: {e}")

# ✅ Upload all images in folder
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    
    if os.path.isfile(file_path): 
        upload_image(file_path)
