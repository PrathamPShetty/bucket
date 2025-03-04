# **Your SAS URL (temporary access link)**
# **Initialize Blob Service Client**
# blob_service_client = BlobServiceClient(account_url=sas_url)

# **Container name (Extracted from SAS URL)**


# # **Specify file to upload**
# local_file_path = "./muhammedalfas07.jpeg"  # Change this to your file path
# blob_name = os.path.basename(local_file_path)  # Name of the file in the cloud

# try:
#     # **Get a client for the blob (file)**
#     blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

#     # **Upload the file**
#     with open(local_file_path, "rb") as data:
#         blob_client.upload_blob(data, overwrite=True)

#     print(f"✅ File '{blob_name}' uploaded successfully to Azure Blob Storage.")

# except Exception as e:
#     print(f"❌ Error: {e}")



import os
from azure.storage.blob import BlobServiceClient, ContentSettings

AZURE_STORAGE_CONNECTION_STRING = "https://sitmng.blob.core.windows.net/alumni?sp=racwd&st=2025-03-04T14:53:13Z&se=2028-12-31T22:53:13Z&spr=https&sv=2022-11-02&sr=c&sig=d77JujJT2%2F4Sdn2ZXO0OtYocI8l5SdXpHGcvA8tGhWc%3D"

container_name = "alumnis"
folder_path = "D:/bucket/upload1/"  # Change this to your folder

def upload_image(image_path):
    try:
     
        blob_service_client = BlobServiceClient.from_connection_string("https://sitmng.blob.core.windows.net/alumni?sp=racwd&st=2025-03-04T14:53:13Z&se=2028-12-31T22:53:13Z&spr=https&sv=2022-11-02&sr=c&sig=d77JujJT2%2F4Sdn2ZXO0OtYocI8l5SdXpHGcvA8tGhWc%3D")

        container_client = blob_service_client.get_container_client(container_name)

    
        blob_name = os.path.basename(image_path)  
   
        blob_client = container_client.get_blob_client(blob_name)

       
        with open(image_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True, content_settings=ContentSettings(content_type="image/jpeg"))

        print(f"✅ Image uploaded successfully! URL: {blob_client.url}")

    except Exception as e:
        print(f"❌ Error uploading image: {str(e)}")


for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    
    if os.path.isfile(file_path): 
        upload_image(file_path)