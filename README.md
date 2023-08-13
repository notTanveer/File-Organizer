# File Organizer Program

The File Organizer Program is a Python script that helps you organize your files in a given folder by categorizing them into separate subfolders based on their file types. It is a useful tool to keep your files organized and easily accessible.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Supported File Types](#supported-file-types)
- [Getting Started](#getting-started)
- [Customization](#customization)
- [Notes](#notes)

## Introduction

Have you ever found yourself overwhelmed by a cluttered folder filled with different types of files? The File Organizer Program is here to help! It automatically sorts your files into specific subfolders based on their file extensions, making it easier for you to locate and manage your files.

## Usage

1. **Clone or Download**: Start by cloning this repository to your local machine or downloading the Python script (`file_organizer.py`) directly.

2. **Setup Subfolders**: Before running the script, make sure to create the following subfolders within the directory where the script is located:

   - `Music`
   - `Images`
   - `CSV Data`
   - `Executable Files`
   - `Archives`
   - `Documents`
   - `PDFs`
   - `Videos`

3. **Run the Script**: Open a terminal or command prompt, navigate to the directory containing the script, and run the following command:

   ```bash
   python file_organizer.py


Follow the Instructions: The script will prompt you to provide the path to the folder you want to organize. Enter the folder path and press Enter.

Sit Back and Relax: The File Organizer Program will automatically categorize the files in the specified folder and move them to the corresponding subfolders based on their types.


## Supported File Types

The File Organizer Program currently supports the following file types and categorizes them accordingly:

- Music: mp3, wav, flac
- Images: jpg, jpeg, png, gif, bmp
- CSV Data: csv, xlsx
- Executable Files: exe, msi
- Archives: zip, rar, 7z
- Documents: doc, docx, txt, rtf
- PDFs: pdf
- Videos: mp4, avi, mkv, mov



## Getting Started

1. **Requirements**: Ensure you have Python 3.x or higher installed on your system.

2. **Clone Repository**: Clone this repository to your local machine:

   ```bash
   git clone https://github.com/notTanveer/file-organizer.git

bash
Copy code
mkdir Music Images "CSV Data" "Executable Files" Archives Documents PDFs Videos
Run the Script: Follow the usage instructions mentioned above to run the File Organizer Program.

# Customization
You can customize the file_types dictionary in the script to add or modify supported file types and their corresponding extensions. Feel free to adjust the program to meet your specific organizational needs.

# Notes
Always exercise caution when using scripts that modify your file system. Test the File Organizer Program on a small set of files before using it on important directories.

Make sure to create the required subfolders before running the script to avoid any errors.

The program categorizes files based on their extensions and does not analyze file content.