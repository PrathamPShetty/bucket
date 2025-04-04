import os

# Specify the folder containing files
folder_path = "D:/bucket/upload1/"  # Change this to your folder path

# Iterate over all files in the folder
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)  # Full path of the file
    
    # Ensure it's a file and has a valid name
    if os.path.isfile(file_path) and len(file_name) > 1:
        new_name = file_name[1:]  # Remove first character
        new_path = os.path.join(folder_path, new_name)  # New full path
        
        # Rename the file
        os.rename(file_path, new_path)
        print(f"Renamed: {file_name} → {new_name}")
