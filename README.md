# File Metadata Extractor

Extract metadata (EXIF for images, ID3 for audio, PDF info, etc.) from files using Python.

🔧 Built with Python using [pymediainfo](https://github.com/sbraz/pymediainfo), [Pillow](https://python-pillow.org/), and [PyPDF2](https://github.com/py-pdf/pypdf).

Ideal for digital forensics exercises, data analysis, or simply exploring file metadata.

---

## Features

- Extract EXIF data from images (JPEG, PNG, etc.) using Pillow
- Extract media metadata (audio, video) including ID3 tags using pymediainfo
- Extract metadata from PDF files (basic info) using PyPDF2
- Custom interactive terminal interface with ASCII art banner
- Colorful and structured output for ease of reading
- Error handling for unsupported or missing metadata
- Easy-to-use menu-driven CLI

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/File_Metadata_Extractor.git
```
```bash
cd File_Metadata_Extractor
```
```bash
pip install -r requirements.txt
```

---

## Usage

Run the script from the terminal:

```bash
python metadata_extractor.py
```

# File Metadata Extractor

This Python script extracts metadata from various file types, including images (EXIF), audio/video (MediaInfo/ID3), and PDFs.  It features a user-friendly command-line interface with colored output and an interactive menu.

## Usage

The script guides you through a simple process:

1. **Select File Type:** Choose the file type for metadata extraction:
    * 1. Image (EXIF)
    * 2. Audio/Video (MediaInfo / ID3)
    * 3. PDF
    * 4. Exit

2. **Enter Your Choice:** Input your choice (1-4).

3. **Enter File Path:** Provide the full path to your file (e.g., `/path/to/your/file.jpg`).

### The script will then process the file and display the extracted metadata in your terminal.