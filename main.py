import os
import shutil

directory = os.path.join(os.path.expanduser("~"),"Downloads")

extensions = {
    ".jpg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".avi": "Videos",
    ".eml": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".mp3": "Music",
    ".java": "Code",
    ".py": "Code",
    ".zip": "Code",
    ".pkg": "Package",
    ".dmg": "Package",
    ".mov": "Videos"
}

for fileName in os.listdir(directory):
    file_path = os.path.join(directory, fileName)
    folder_name = ""

    if(os.path.isfile(file_path)):
        extension = os.path.splitext(fileName)[1].lower()

        if extension in extensions:
            folder_name = extensions[extension] 

            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path,exist_ok=True)
            destination_path = os.path.join(folder_path,fileName)

            shutil.move(file_path, destination_path)

            print("Moved" + fileName + "to" + folder_name)
        
        else:
            print("Skipped" + fileName + "to" + folder_name)
    else:
        print("Skipped" + fileName + "It is a directory")