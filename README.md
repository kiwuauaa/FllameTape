<div align="center">

# 🎬 FllameTape - File Metadata Extractor

```
███████╗██╗     ██╗      █████╗ ███╗   ███╗███████╗████████╗ █████╗ ██████╗ ███████╗
██╔════╝██║     ██║     ██╔══██╗████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝
█████╗  ██║     ██║     ███████║██╔████╔██║█████╗     ██║   ███████║██████╔╝█████╗  
██╔══╝  ██║     ██║     ██╔══██║██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██╔═══╝ ██╔══╝  
██║     ███████╗███████╗██║  ██║██║ ╚═╝ ██║███████╗   ██║   ██║  ██║██║     ███████╗
╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚══════╝
```

### 🔍 *A powerful Python tool to extract metadata from various file types*

**📷 Images (EXIF) • 🎵 Audio/Video (MediaInfo/ID3) • 📄 PDF Documents**

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/kiwuauaa/FllameTape/graphs/commit-activity)

</div>

---

## 👤 Author

**Created by [kiwuauaa](https://github.com/kiwuauaa)**

---

🔧 **Built with Python** using:
- [Pillow](https://python-pillow.org/) - For image EXIF data extraction
- [pymediainfo](https://github.com/sbraz/pymediainfo) - For audio/video metadata
- [pypdf](https://github.com/py-pdf/pypdf) - For PDF document information

**Perfect for:** Digital forensics exercises, data analysis, or simply exploring file metadata.

---

## ✨ Features

- 📷 **Image Metadata**: Extract EXIF data from JPEG, PNG, and other image formats
- 🎵 **Media Metadata**: Extract comprehensive metadata from audio and video files including ID3 tags
- 📄 **PDF Metadata**: Extract document information from PDF files
- 🎨 **Interactive Interface**: Custom terminal interface with ASCII art banner
- 🌈 **Colorful Output**: Structured and easy-to-read colored terminal output
- 🛡️ **Error Handling**: Robust error handling for unsupported or corrupted files
- 🎯 **User-Friendly**: Simple menu-driven command-line interface

---

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kiwuauaa/FllameTape.git
   cd FllameTape
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Usage

Run the script from the terminal:

```bash
python metadata_extractor.py
```

### Interactive Menu

The script provides a simple interactive menu:

1. **📷 Image (EXIF)** - Extract EXIF metadata from image files
2. **🎵 Audio/Video (MediaInfo/ID3)** - Extract metadata from media files
3. **📄 PDF** - Extract document information from PDF files
4. **🚪 Exit** - Close the application

### Steps:
1. Select the file type (1-4)
2. Enter the full path to your file
3. View the extracted metadata in your terminal

---

## 📁 Supported File Types

- **Images**: JPEG, PNG, TIFF, and other formats supported by Pillow
- **Audio**: MP3, FLAC, OGG, M4A, and more
- **Video**: MP4, AVI, MKV, MOV, and other common formats
- **Documents**: PDF files

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⭐ Show Your Support

If you find this project helpful, please consider giving it a star on GitHub!

---

## 👨‍💻 About the Author

**[kiwuauaa](https://github.com/kiwuauaa)** - *Creator & Lead Developer*

- 🔬 Passionate about digital forensics and data analysis
- 🛡️ Cyber security and IT student

*"Uncovering the hidden stories that files tell through their metadata"*

### Connect with the Author:
- 🐙 GitHub: [@kiwuauaa](https://github.com/kiwuauaa)

---

<div align="center">

**Built with ❤️ by [kiwuauaa](https://github.com/kiwuauaa)**

*Making metadata extraction accessible to everyone*

</div>