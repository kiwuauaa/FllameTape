import sys
import os
from PIL import Image
from PIL.ExifTags import TAGS
from pymediainfo import MediaInfo
from PyPDF2 import PdfReader

# ANSI color codes for terminal styling
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_banner():
    banner = f"""
{Colors.OKCYAN}
███████╗██╗     ██╗      █████╗ ███╗   ███╗███████╗████████╗ █████╗ ██████╗ ███████╗
██╔════╝██║     ██║     ██╔══██╗████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝
█████╗  ██║     ██║     ███████║██╔████╔██║█████╗     ██║   ███████║██████╔╝█████╗  
██╔══╝  ██║     ██║     ██╔══██║██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██╔═══╝ ██╔══╝  
██║     ███████╗███████╗██║  ██║██║ ╚═╝ ██║███████╗   ██║   ██║  ██║██║     ███████╗
╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚══════╝
{Colors.ENDC}
    """
    print(banner)
    print(f"{Colors.BOLD}Welcome to the File Metadata Extractor!{Colors.ENDC}\n")

def extract_image_metadata(file_path):
    print(f"{Colors.OKGREEN}Extracting image metadata from '{file_path}'...{Colors.ENDC}")
    try:
        image = Image.open(file_path)
        exif_data = image._getexif()
        if not exif_data:
            print(f"{Colors.WARNING}No EXIF metadata found.{Colors.ENDC}")
            return

        print(f"{Colors.BOLD}EXIF metadata:{Colors.ENDC}")
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            print(f" - {tag}: {value}")
    except Exception as e:
        print(f"{Colors.FAIL}Error extracting image metadata: {e}{Colors.ENDC}")

def extract_media_metadata(file_path):
    print(f"{Colors.OKGREEN}Extracting media metadata from '{file_path}'...{Colors.ENDC}")
    try:
        media_info = MediaInfo.parse(file_path)
        if not media_info.tracks:
            print(f"{Colors.WARNING}No media metadata found.{Colors.ENDC}")
            return

        print(f"{Colors.BOLD}Media metadata:{Colors.ENDC}")
        for track in media_info.tracks:
            print(f"Track type: {track.track_type}")
            for key, value in track.to_data().items():
                if value and key != 'track_type':
                    print(f" - {key}: {value}")
            print()
    except Exception as e:
        print(f"{Colors.FAIL}Error extracting media metadata: {e}{Colors.ENDC}")

def extract_pdf_metadata(file_path):
    print(f"{Colors.OKGREEN}Extracting PDF metadata from '{file_path}'...{Colors.ENDC}")
    try:
        with open(file_path, 'rb') as f:
            reader = PdfReader(f)
            info = reader.metadata
            if not info:
                print(f"{Colors.WARNING}No PDF metadata found.{Colors.ENDC}")
                return
            print(f"{Colors.BOLD}PDF metadata:{Colors.ENDC}")
            for key, value in info.items():
                print(f" - {key}: {value}")
    except Exception as e:
        print(f"{Colors.FAIL}Error extracting PDF metadata: {e}{Colors.ENDC}")

def display_menu():
    print(f"{Colors.BOLD}Select file type to extract metadata from:{Colors.ENDC}")
    print("  1. Image (EXIF)")
    print("  2. Audio/Video (MediaInfo / ID3)")
    print("  3. PDF")
    print("  4. Exit")

def main():
    print_banner()

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        if choice == '4':
            print(f"{Colors.OKCYAN}Exiting. Goodbye!{Colors.ENDC}")
            break
        elif choice in ['1', '2', '3']:
            file_path = input("Enter the path to your file: ").strip()
            if not os.path.isfile(file_path):
                print(f"{Colors.FAIL}File not found. Please try again.{Colors.ENDC}\n")
                continue

            if choice == '1':
                extract_image_metadata(file_path)
            elif choice == '2':
                extract_media_metadata(file_path)
            elif choice == '3':
                extract_pdf_metadata(file_path)
            print("\n" + "-"*60 + "\n")
        else:
            print(f"{Colors.WARNING}Invalid choice. Please enter a number between 1 and 4.{Colors.ENDC}\n")

if __name__ == '__main__':
    main()

