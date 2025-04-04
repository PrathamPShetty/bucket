import os
from azure.storage.blob import BlobServiceClient, ContentSettings

# Define account URL and SAS token separately
ACCOUNT_URL = "https://alumniweb.blob.core.windows.net"
SAS_TOKEN = "sp=rac&st=2025-03-13T06:42:57Z&se=2025-03-13T14:42:57Z&sv=2022-11-02&sr=c&sig=%2ByNsdJ83zqJM19Fs%2FfAs8CLHb2WlVLJoW6quYwT1mEs%3D"
container_name = "alumni"
folder_path = "D:/bucket/upload1/"  # Change this to your folder path

def upload_image(image_path):
    try:
        # Correct way to initialize BlobServiceClient with a SAS token
        blob_service_client = BlobServiceClient(account_url=ACCOUNT_URL, credential=SAS_TOKEN)
        container_client = blob_service_client.get_container_client(container_name)

        blob_name = os.path.basename(image_path)  
        blob_client = container_client.get_blob_client(blob_name)

        # Upload file
        with open(image_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True, content_settings=ContentSettings(content_type="image/jpeg"))

        print(f"✅ Image uploaded successfully! URL: {blob_client.url}")

    except Exception as e:
        print(f"❌ Error uploading image: {str(e)}")

# Upload all files in folder
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    
    if os.path.isfile(file_path): 
        upload_image(file_path)

# def upload_image(image_path):
#     try:
#         blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
#         container_client = blob_service_client.get_container_client(container_name)

#         blob_name = os.path.basename(image_path)  
#         blob_client = container_client.get_blob_client(blob_name)

#         with open(image_path, "rb") as data:
#             blob_client.upload_blob(
#                 data, 
#                 overwrite=True, 
#                 content_settings=ContentSettings(content_type="image/jpeg")  # Ensure correct MIME type
#             )

#         print(f"✅ Image uploaded successfully! URL: {blob_client.url}")

#     except Exception as e:
#         print(f"❌ Error uploading image: {str(e)}")


