import os
import shutil

# Define file extensions and their corresponding folders
file_types = {
    "music": ["mp3", "wav", "flac"],
    "images": ["jpg", "jpeg", "png", "gif", "bmp"],
    "csv_data": ["csv", "xlsx"],
    "executables": ["exe", "msi"],
    "archives": ["zip", "rar", "7z"],
    "documents": ["doc", "docx", "txt", "rtf"],
    "pdfs": ["pdf"],
    "videos": ["mp4", "avi", "mkv", "mov"],
}


def organize_files(src_folder):
    for filename in os.listdir(src_folder):
        file_extension = filename.split(".")[-1].lower()

        for file_type, extensions in file_types.items():
            if file_extension in extensions:
                destination_folder = os.path.join(src_folder, file_type.capitalize())
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                source_path = os.path.join(src_folder, filename)
                destination_path = os.path.join(destination_folder, filename)
                shutil.move(source_path, destination_path)
                print(f"Moved '{filename}' to '{destination_folder}'")


if __name__ == "__main__":
    source_folder = "C:\cohort\edited"  # Change this to the path of the folder you want to organize
    organize_files(source_folder)
