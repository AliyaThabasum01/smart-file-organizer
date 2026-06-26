import os
import shutil

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
}


def organize_folder(folder_path):

    if not os.path.exists(folder_path):
        raise FileNotFoundError("Folder does not exist.")

    for file in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file)

        if os.path.isdir(file_path):
            continue

        extension = os.path.splitext(file)[1].lower()

        moved = False

        for folder_name, extensions in FILE_TYPES.items():

            if extension in extensions:

                destination = os.path.join(folder_path, folder_name)

                os.makedirs(destination, exist_ok=True)

                shutil.move(file_path, os.path.join(destination, file))

                moved = True

                break

        if not moved:

            others = os.path.join(folder_path, "Others")

            os.makedirs(others, exist_ok=True)

            shutil.move(file_path, os.path.join(others, file))
