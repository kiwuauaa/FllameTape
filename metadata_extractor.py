import sys
import os
import time
from PIL import Image
from PIL.ExifTags import TAGS
from pymediainfo import MediaInfo
# Import statements with fallback compatibility
try:
    from pypdf import PdfReader
except ImportError:
    try:
        from PyPDF2 import PdfReader
    except ImportError:
        print("Error: Please install pypdf or PyPDF2: pip install pypdf")
        sys.exit(1)

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
    UNDERLINE = '\033[4m'
    PURPLE = '\033[35m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

# Terminal interface utilities
class TerminalUI:
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def print_separator(char="═", length=80, color=Colors.OKCYAN):
        print(f"{color}{char * length}{Colors.ENDC}")
    
    @staticmethod
    def print_box(text, color=Colors.OKBLUE, padding=2):
        lines = text.split('\n')
        max_length = max(len(line) for line in lines)
        width = max_length + (padding * 2)
        
        print(f"{color}╔{'═' * width}╗{Colors.ENDC}")
        for line in lines:
            spaces = ' ' * (max_length - len(line))
            print(f"{color}║{' ' * padding}{line}{spaces}{' ' * padding}║{Colors.ENDC}")
        print(f"{color}╚{'═' * width}╝{Colors.ENDC}")
    
    @staticmethod
    def loading_animation(text, duration=2.0):
        frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        start_time = time.time()
        i = 0
        while time.time() - start_time < duration:
            print(f"\r{Colors.OKCYAN}{frames[i % len(frames)]} {text}{Colors.ENDC}", end='', flush=True)
            time.sleep(0.1)
            i += 1
        print(f"\r{Colors.OKGREEN}✓ {text} - Complete!{Colors.ENDC}")

def print_banner():
    TerminalUI.clear_screen()
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
    
    # Animated welcome message
    welcome_text = f"{Colors.BOLD}{Colors.PURPLE}Welcome to FllameTape - File Metadata Extractor!{Colors.ENDC}"
    author_text = f"{Colors.CYAN}Created by kiwuauaa - Digital Forensics Specialist{Colors.ENDC}"
    
    TerminalUI.print_box(f"{welcome_text}\n{author_text}", Colors.PURPLE)
    
    print(f"\n{Colors.YELLOW}🔍 Discover hidden metadata in your files{Colors.ENDC}")
    print(f"{Colors.GREEN}📊 Professional forensics tool for data analysis{Colors.ENDC}")
    
    TerminalUI.print_separator("─", 80, Colors.OKCYAN)
    print()

def print_command_headers():
    """Print custom headers for each command type"""
    pass

def print_image_header():
    print(f"\n{Colors.PURPLE}{'═' * 80}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}📷 IMAGE METADATA EXTRACTION MODE{Colors.ENDC}")
    print(f"{Colors.PURPLE}{'═' * 80}{Colors.ENDC}")
    print(f"{Colors.YELLOW}🔍 Extracting EXIF data from image files{Colors.ENDC}")
    print(f"{Colors.GREEN}📊 Supported formats: JPEG, PNG, TIFF, and more{Colors.ENDC}\n")

def print_media_header():
    print(f"\n{Colors.BLUE}{'═' * 80}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}🎵 MEDIA METADATA EXTRACTION MODE{Colors.ENDC}")
    print(f"{Colors.BLUE}{'═' * 80}{Colors.ENDC}")
    print(f"{Colors.YELLOW}🔍 Extracting metadata from audio/video files{Colors.ENDC}")
    print(f"{Colors.GREEN}📊 Supported: MP3, MP4, AVI, MKV, FLAC, and more{Colors.ENDC}\n")

def print_pdf_header():
    print(f"\n{Colors.RED}{'═' * 80}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}📄 PDF METADATA EXTRACTION MODE{Colors.ENDC}")
    print(f"{Colors.RED}{'═' * 80}{Colors.ENDC}")
    print(f"{Colors.YELLOW}🔍 Extracting document information from PDF files{Colors.ENDC}")
    print(f"{Colors.GREEN}📊 Document properties, author info, and more{Colors.ENDC}\n")

def extract_image_metadata(file_path):
    print_image_header()
    
    # Animated processing message
    TerminalUI.loading_animation(f"Processing image: {os.path.basename(file_path)}", 1.5)
    
    try:
        image = Image.open(file_path)
        # Use the modern getexif() method instead of deprecated _getexif()
        exif_data = image.getexif()
        
        if not exif_data:
            TerminalUI.print_box(f"⚠️  No EXIF metadata found\nFile: {os.path.basename(file_path)}", Colors.WARNING)
            return

        # Success header
        print(f"\n{Colors.OKGREEN}✅ EXIF METADATA SUCCESSFULLY EXTRACTED{Colors.ENDC}")
        TerminalUI.print_separator("─", 60, Colors.OKGREEN)
        
        print(f"{Colors.BOLD}{Colors.CYAN}📸 Image Information:{Colors.ENDC}")
        print(f"{Colors.YELLOW}   📁 File: {os.path.basename(file_path)}{Colors.ENDC}")
        print(f"{Colors.YELLOW}   📐 Format: {image.format}{Colors.ENDC}")
        print(f"{Colors.YELLOW}   📏 Size: {image.size[0]} x {image.size[1]} pixels{Colors.ENDC}")
        print(f"{Colors.YELLOW}   🎨 Mode: {image.mode}{Colors.ENDC}\n")
        
        print(f"{Colors.BOLD}{Colors.PURPLE}📊 EXIF Metadata Details:{Colors.ENDC}")
        TerminalUI.print_separator("─", 60, Colors.PURPLE)
        
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            # Handle binary data and long strings
            if isinstance(value, bytes):
                try:
                    value = value.decode('utf-8', errors='ignore')
                except:
                    value = str(value)
            elif isinstance(value, str) and len(value) > 100:
                value = value[:100] + "..."
            
            print(f"{Colors.CYAN}   🔸 {tag}: {Colors.WHITE}{value}{Colors.ENDC}")
            
    except FileNotFoundError:
        TerminalUI.print_box(f"❌ File not found\nPath: {file_path}", Colors.FAIL)
    except Exception as e:
        TerminalUI.print_box(f"❌ Error processing image\nError: {str(e)}", Colors.FAIL)

def extract_media_metadata(file_path):
    print_media_header()
    
    # Animated processing message
    TerminalUI.loading_animation(f"Analyzing media file: {os.path.basename(file_path)}", 1.5)
    
    try:
        media_info = MediaInfo.parse(file_path)
        if not media_info.tracks:
            TerminalUI.print_box(f"⚠️  No media metadata found\nFile: {os.path.basename(file_path)}", Colors.WARNING)
            return

        # Success header
        print(f"\n{Colors.OKGREEN}✅ MEDIA METADATA SUCCESSFULLY EXTRACTED{Colors.ENDC}")
        TerminalUI.print_separator("─", 60, Colors.OKGREEN)
        
        print(f"{Colors.BOLD}{Colors.CYAN}🎵 Media File Information:{Colors.ENDC}")
        print(f"{Colors.YELLOW}   📁 File: {os.path.basename(file_path)}{Colors.ENDC}")
        print(f"{Colors.YELLOW}   📊 Total tracks: {len(media_info.tracks)}{Colors.ENDC}\n")
        
        track_icons = {
            'General': '📋',
            'Video': '🎬',
            'Audio': '🎵',
            'Text': '📝',
            'Menu': '📚'
        }
        
        for i, track in enumerate(media_info.tracks, 1):
            track_type = track.track_type
            icon = track_icons.get(track_type, '📄')
            
            print(f"{Colors.BOLD}{Colors.PURPLE}{icon} Track {i}: {track_type.upper()}{Colors.ENDC}")
            TerminalUI.print_separator("─", 50, Colors.PURPLE)
            
            track_data = track.to_data()
            for key, value in track_data.items():
                if value and key != 'track_type':
                    # Handle long values
                    if isinstance(value, str) and len(value) > 100:
                        value = value[:100] + "..."
                    print(f"{Colors.CYAN}   🔸 {key}: {Colors.WHITE}{value}{Colors.ENDC}")
            print()
            
    except FileNotFoundError:
        TerminalUI.print_box(f"❌ File not found\nPath: {file_path}", Colors.FAIL)
    except Exception as e:
        TerminalUI.print_box(f"❌ Error processing media file\nError: {str(e)}", Colors.FAIL)

def extract_pdf_metadata(file_path):
    print_pdf_header()
    
    # Animated processing message
    TerminalUI.loading_animation(f"Reading PDF document: {os.path.basename(file_path)}", 1.5)
    
    try:
        with open(file_path, 'rb') as f:
            reader = PdfReader(f)
            info = reader.metadata
            
            # Success header
            print(f"\n{Colors.OKGREEN}✅ PDF METADATA SUCCESSFULLY EXTRACTED{Colors.ENDC}")
            TerminalUI.print_separator("─", 60, Colors.OKGREEN)
            
            print(f"{Colors.BOLD}{Colors.CYAN}📄 Document Information:{Colors.ENDC}")
            print(f"{Colors.YELLOW}   📁 File: {os.path.basename(file_path)}{Colors.ENDC}")
            print(f"{Colors.YELLOW}   📊 Total pages: {len(reader.pages)}{Colors.ENDC}")
            print(f"{Colors.YELLOW}   🔐 Encrypted: {'Yes' if reader.is_encrypted else 'No'}{Colors.ENDC}\n")
            
            if info:
                print(f"{Colors.BOLD}{Colors.PURPLE}📋 Document Metadata:{Colors.ENDC}")
                TerminalUI.print_separator("─", 60, Colors.PURPLE)
                
                for key, value in info.items():
                    # Clean up the key name (remove leading slash)
                    clean_key = key.lstrip('/')
                    # Handle different value types
                    if hasattr(value, 'strip'):
                        value = value.strip()
                    print(f"{Colors.CYAN}   🔸 {clean_key}: {Colors.WHITE}{value}{Colors.ENDC}")
            else:
                TerminalUI.print_box(f"⚠️  No document metadata found\nFile: {os.path.basename(file_path)}", Colors.WARNING)
                
    except FileNotFoundError:
        TerminalUI.print_box(f"❌ File not found\nPath: {file_path}", Colors.FAIL)
    except Exception as e:
        TerminalUI.print_box(f"❌ Error processing PDF document\nError: {str(e)}", Colors.FAIL)

def display_menu():
    print(f"{Colors.BOLD}{Colors.HEADER}╔══════════════════════════════════════════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.HEADER}║                          🔧 METADATA EXTRACTION MENU                        ║{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.HEADER}╚══════════════════════════════════════════════════════════════════════════════╝{Colors.ENDC}")
    print(f"{Colors.BOLD}\nSelect the type of file you want to analyze:{Colors.ENDC}\n")
    
    print(f"{Colors.BOLD}{Colors.PURPLE}  📷 [1] Image Files{Colors.ENDC}")
    print(f"{Colors.CYAN}      └─ Extract EXIF metadata from photos{Colors.ENDC}")
    print(f"{Colors.CYAN}      └─ Formats: JPEG, PNG, TIFF, etc.{Colors.ENDC}\n")
    
    print(f"{Colors.BOLD}{Colors.BLUE}  🎵 [2] Audio/Video Files{Colors.ENDC}")
    print(f"{Colors.CYAN}      └─ Extract MediaInfo and ID3 tags{Colors.ENDC}")
    print(f"{Colors.CYAN}      └─ Formats: MP3, MP4, AVI, MKV, etc.{Colors.ENDC}\n")
    
    print(f"{Colors.BOLD}{Colors.RED}  📄 [3] PDF Documents{Colors.ENDC}")
    print(f"{Colors.CYAN}      └─ Extract document properties{Colors.ENDC}")
    print(f"{Colors.CYAN}      └─ Author, creation date, etc.{Colors.ENDC}\n")
    
    print(f"{Colors.BOLD}{Colors.WARNING}  🚪 [4] Exit Program{Colors.ENDC}")
    print(f"{Colors.CYAN}      └─ Close FllameTape safely{Colors.ENDC}\n")
    
    TerminalUI.print_separator("─", 80, Colors.OKCYAN)

def main():
    print_banner()

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        if choice == '4':
            print(f"\n{Colors.PURPLE}{'═' * 80}{Colors.ENDC}")
            print(f"{Colors.BOLD}{Colors.CYAN}👋 Thank you for using FllameTape!{Colors.ENDC}")
            print(f"{Colors.PURPLE}{'═' * 80}{Colors.ENDC}")
            print(f"{Colors.YELLOW}🔍 Tool created by kiwuauaa{Colors.ENDC}")
            print(f"{Colors.GREEN}🌟 Perfect for digital forensics and data analysis{Colors.ENDC}")
            print(f"{Colors.CYAN}💡 Visit: https://github.com/kiwuauaa/FllameTape{Colors.ENDC}")
            print(f"{Colors.PURPLE}{'═' * 80}{Colors.ENDC}")
            print(f"{Colors.BOLD}{Colors.OKCYAN}Goodbye! 🚀{Colors.ENDC}\n")
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
            # Results footer
            print(f"\n{Colors.OKGREEN}{'═' * 80}{Colors.ENDC}")
            print(f"{Colors.BOLD}{Colors.GREEN}✨ Metadata extraction completed successfully!{Colors.ENDC}")
            print(f"{Colors.CYAN}📊 Analysis by FllameTape - Created by kiwuauaa{Colors.ENDC}")
            print(f"{Colors.OKGREEN}{'═' * 80}{Colors.ENDC}\n")
            
            input(f"{Colors.YELLOW}Press Enter to continue...{Colors.ENDC}")
        else:
            print(f"{Colors.WARNING}Invalid choice. Please enter a number between 1 and 4.{Colors.ENDC}\n")

if __name__ == '__main__':
    main()

