from pymongo import MongoClient
import os

# Source and target cluster URIs
SOURCE_URI = "mongodb+srv://recruitment:40jrDiXbIx5TKyOt@serverlessinstance0.rrix0lr.mongodb.net"
TARGET_URI = "mongodb://adminEnvision:Strongapass202@89.233.104.140:27017"

# Database to transfer
SOURCE_DB_NAME = "alumni"
TARGET_DB_NAME = "alumni"  # can be same or different

# Connect to source and target clients
source_client = MongoClient(SOURCE_URI)
target_client = MongoClient(TARGET_URI)

source_db = source_client[SOURCE_DB_NAME]
target_db = target_client[TARGET_DB_NAME]

# Transfer all collections
for coll_name in source_db.list_collection_names():
    print(f"Transferring collection: {coll_name}")
    source_collection = source_db[coll_name]
    target_collection = target_db[coll_name]

    # Clear target collection if exists
    target_collection.delete_many({})

    # Transfer all documents
    documents = list(source_collection.find())
    if documents:
        target_collection.insert_many(documents)

print("Database transfer complete.")
