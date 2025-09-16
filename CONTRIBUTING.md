# 🤝 Contributing to FllameTape

First off, thank you for considering contributing to FllameTape! 🎉

FllameTape is a professional digital forensics metadata extraction tool created by [kiwuauaa](https://github.com/kiwuauaa). We welcome contributions that help improve the tool's functionality, usability, and reliability.

## 🔍 About FllameTape

FllameTape is designed for:
- 👨‍💻 Digital forensics investigators
- 📊 Data analysts
- 🔍 Security researchers
- 📱 Anyone needing professional metadata extraction

## 🎯 How Can You Contribute?

### 🐛 Bug Reports
- Use the bug report template
- Include detailed reproduction steps
- Provide system information
- Attach relevant file samples (if safe)

### ✨ Feature Requests
- Use the feature request template
- Explain the use case clearly
- Consider digital forensics applications
- Describe UI/terminal interface impact

### 💻 Code Contributions
- Follow the coding standards below
- Maintain the professional terminal interface design
- Ensure cross-platform compatibility
- Add appropriate error handling

## 🎨 Coding Standards

### Terminal Interface Guidelines
Following our project specification for custom terminal interfaces:

- **Consistent Visual Elements**: Use Unicode borders, emoji icons, and color themes
- **Command-Specific Headers**: Each command type has its own branded header
- **Animated Feedback**: Loading animations during processing
- **Professional Formatting**: Maintain the forensics-grade appearance

### Code Style
- Use [Black](https://black.readthedocs.io/) for code formatting
- Organize imports with [isort](https://pycqa.github.io/isort/)
- Follow PEP 8 guidelines
- Maximum line length: 88 characters

### Dependencies
- Follow the project's dependency specifications
- Use `pypdf` instead of deprecated `PyPDF2`
- Maintain compatibility with Python 3.7+

## 🚀 Development Setup

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/your-username/FllameTape.git
   cd FllameTape
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # or
   venv\Scripts\activate     # Windows
   ```

3. **Install development dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install black isort flake8 pytest
   ```

4. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## ✅ Testing Your Changes

### Manual Testing
Test your changes with various file types:
- 📷 **Images**: JPEG, PNG, TIFF with EXIF data
- 🎵 **Media**: MP3, MP4, AVI files with metadata
- 📄 **PDFs**: Documents with author information

### Platform Testing
Ensure compatibility across:
- 🖥️ Windows (PowerShell and Command Prompt)
- 🍎 macOS (Terminal and iTerm2)
- 🐧 Linux (various terminal emulators)

### Interface Testing
Verify the terminal interface:
- Colors display correctly
- Unicode characters render properly
- Animations work smoothly
- Error messages are clear and helpful

## 📋 Pull Request Process

1. **Update documentation** if needed
2. **Follow the PR template** completely
3. **Ensure all tests pass** in CI/CD
4. **Maintain backwards compatibility**
5. **Request review** from @kiwuauaa

### PR Requirements
- [ ] Code follows style guidelines
- [ ] Changes are tested thoroughly
- [ ] Terminal interface remains consistent
- [ ] No breaking changes (unless discussed)
- [ ] Documentation is updated

## 🔍 Code Review Process

Reviews focus on:
- **Functionality**: Does it work correctly?
- **Security**: Are there any vulnerabilities?
- **Performance**: Impact on extraction speed
- **Usability**: Terminal interface quality
- **Compatibility**: Cross-platform support

## 🎨 Design Philosophy

FllameTape follows these principles:
- **Professional Appearance**: Forensics-grade tool aesthetics
- **User-Friendly**: Clear, intuitive interface
- **Reliable**: Robust error handling
- **Fast**: Efficient metadata extraction
- **Secure**: Safe file processing

## 📚 Resources

- [Project Wiki](https://github.com/kiwuauaa/FllameTape/wiki)
- [Issue Tracker](https://github.com/kiwuauaa/FllameTape/issues)
- [Discussions](https://github.com/kiwuauaa/FllameTape/discussions)

## 🏷️ Release Process

Releases are managed by @kiwuauaa and follow semantic versioning:
- **Major** (x.0.0): Breaking changes
- **Minor** (0.x.0): New features
- **Patch** (0.0.x): Bug fixes

## 📞 Getting Help

- 💬 [GitHub Discussions](https://github.com/kiwuauaa/FllameTape/discussions)
- 🐛 [Report Issues](https://github.com/kiwuauaa/FllameTape/issues)
- 📧 Contact @kiwuauaa for direct questions

## 📄 License

By contributing to FllameTape, you agree that your contributions will be licensed under the MIT License.

---

## 🙏 Recognition

Contributors will be recognized in:
- 📋 CONTRIBUTORS.md file
- 🎉 Release notes
- 📊 Project README

Thank you for helping make FllameTape better! 🚀

*FllameTape - Professional metadata extraction for digital forensics*
*Created and maintained by [kiwuauaa](https://github.com/kiwuauaa)*