import os
import logging
from PIL import Image
from pillow_heif import register_heif_opener
import tkinter
from tkinter import filedialog

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(message)s")

# Prevent an empty tkinter window from appearing
tkinter.Tk().withdraw()


def convert_files(files):
    """Converts HEIC files to JPG format."""
    for file in files:
        img = Image.open(file)
        output_file = os.path.splitext(file)[0] + ".jpg"
        img.save(output_file, "JPEG")
        logging.info(f"{file} converted to {output_file}")


def convert_folder(input_folder):
    """Converts all HEIC files in a folder to JPG format."""
    for filename in os.listdir(input_folder):
        if not filename.lower().endswith(".heic"):
            logging.info(f"{filename} is not a HEIC file. Skipping...")
            continue

        input_path = os.path.join(input_folder, filename)  # Full path to file
        output_folder = os.path.join(input_folder, "converted_jpgs")

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        output_file = os.path.join(
            output_folder, os.path.splitext(filename)[0] + ".jpg"
        )
        img = Image.open(input_path.replace("\\", "/"))
        img.save(output_file, "JPEG")
        logging.info(f"{filename} converted to {output_file}")

    logging.info("Conversion complete.")


def main():
    """Main function that asks user for input and handles files and folders."""
    logging.info("=====================================")
    logging.info("HEIC to JPG Converter")
    logging.info("=====================================")
    register_heif_opener()
    # Ask user for input
    while True:
        input_type = input(
            "Would you like to convert a folder or individual files? (folder/files) > "
        )
        if input_type == "folder":
            folder = filedialog.askdirectory(
                title="Select folder containing HEIC files to convert."
            )
            convert_folder(folder)
            break
        elif input_type == "files":
            files = filedialog.askopenfilenames(title="Select HEIC files to convert.")
            convert_files(files)
            break
        elif input_type == "exit" or input_type == "quit":
            break
        else:
            logging.info("Invalid input. Please enter 'folder' or 'files'.")
            continue

    input("\nPress enter to exit.")
    exit()


if __name__ == "__main__":
    main()
