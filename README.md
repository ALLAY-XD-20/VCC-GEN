# 🎯 ALPHA DEV - Card Generator Tool

```
     █████╗ ██╗     ██████╗ ██╗  ██╗ █████╗     ██████╗ ███████╗██╗   ██╗
    ██╔══██╗██║     ██╔══██╗██║  ██║██╔══██╗    ██╔══██╗██╔════╝██║   ██║
    ███████║██║     ██████╔╝███████║███████║    ██║  ██║█████╗  ██║   ██║
    ██╔══██║██║     ██╔═══╝ ██╔══██║██╔══██║    ██║  ██║██╔══╝  ╚██╗ ██╔╝
    ██║  ██║███████╗██║     ██║  ██║██║  ██║    ██████╔╝███████╗ ╚████╔╝ 
    ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝  ╚═══╝  
```

> 🔥 **Professional Card Generator Tool with RGB ASCII Interface**

## 📋 Overview

ALPHA DEV is a powerful Python-based card generator tool that creates random card numbers with expiration dates and CVV codes. Features a stunning RGB ASCII interface with colorful output and professional design.

## ✨ Features

- 🎨 **RGB ASCII Banner** - Eye-catching colorful interface
- 💳 **Multi-Card Support** - Generate VISA, MasterCard, and Discover cards
- 🔢 **Bulk Generation** - Generate multiple cards at once
- 💾 **Auto-Save Feature** - Save results to organized files
- 🎯 **Professional UI** - Clean menu system with color coding
- 📁 **Organized Output** - Results saved in timestamped files

## 🛠️ Installation

### Prerequisites

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![pip](https://img.shields.io/badge/pip-required-green.svg)](https://pip.pypa.io/en/stable/installation/)

### Quick Install

1. **Download Python** 
   
   [![Download Python](https://img.shields.io/badge/Download-Python%203.11-blue?style=for-the-badge&logo=python)](https://www.python.org/downloads/)

2. **Install Required Package**
   
   ```bash
   pip install colorama
   ```
   
   [![Install colorama](https://img.shields.io/badge/Install-colorama-red?style=for-the-badge&logo=pypi)](https://pypi.org/project/colorama/)

3. **Clone Repository**
   
   ```bash
   git clone https://github.com/ALLAY-XD-20/VCC-GEN/
   cd VCC-GEN
   ```

### Alternative Installation Methods

<details>
<summary>📦 Using pip directly</summary>

```bash
# Install colorama package
pip install colorama

# For Windows users
pip install colorama --user

# For Linux/Mac users
pip3 install colorama
```

</details>

<details>
<summary>🐍 Using conda</summary>

```bash
# Install colorama using conda
conda install -c conda-forge colorama
```

</details>

## 🚀 Usage

### Run the Tool

```bash
python main.py
```

### Menu Options

| Option | Description | Card Type |
|--------|-------------|-----------|
| **1** | Generate VISA Cards | 439700004xxxxxxxx |
| **2** | Generate MasterCard | 555270xxxxxxxxxx |
| **3** | Generate Discover Cards | 601100xxxxxxxxxx |
| **4** | Check for Updates | Coming Soon |
| **5** | Exit Program | - |

### Save Options

- **[1] SAVE** - Save generated cards to file
- **[2] DON'T SAVE** - Return to main menu
- **[3] REGEN** - Generate new cards

## 📁 File Structure

```
alpha-dev-card-generator/
├── card_generator.py          # Main application
├── README.md                  # This file
└── Results/                   # Generated cards folder
    ├── CARDS-123456.txt      # Timestamped results
    └── CARDS-789012.txt      # Timestamped results
```

## 🎨 Screenshots

### Main Interface
```
    ████████████████████████████████████████████████████████████
    █████╗ ██╗     ██████╗ ██╗  ██╗ █████╗     ██████╗ ███████╗██╗   ██╗
   ██╔══██╗██║     ██╔══██╗██║  ██║██╔══██╗    ██╔══██╗██╔════╝██║   ██║
   ███████║██║     ██████╔╝███████║███████║    ██║  ██║█████╗  ██║   ██║
   ██╔══██║██║     ██╔═══╝ ██╔══██║██╔══██║    ██║  ██║██╔══╝  ╚██╗ ██╔╝
   ██║  ██║███████╗██║     ██║  ██║██║  ██║    ██████╔╝███████╗ ╚████╔╝ 
   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝  ╚═══╝  
    ████████████████████████████████████████████████████████████
```

## 🔧 Technical Details

### Dependencies

- **colorama** - Cross-platform colored terminal text
- **random** - Random number generation
- **datetime** - Date and time handling
- **os** - Operating system interface

### Supported Platforms

- ✅ Windows 10/11
- ✅ macOS 10.14+
- ✅ Linux (Ubuntu, CentOS, Debian)

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is created for educational and testing purposes only. Generated card numbers are random and not associated with any real financial accounts. Use responsibly and in accordance with applicable laws.

## 💡 Support

Having issues? Check out our troubleshooting guide:

<details>
<summary>🔍 Common Issues</summary>

**colorama not found error:**
```bash
pip install --upgrade colorama
```

**Permission denied error:**
```bash
pip install colorama --user
```

**Python not found:**
- Make sure Python is installed and added to PATH
- Try `python3` instead of `python`

</details>

---

<div align="center">

**Made with ❤️ by ALPHA DEV**

[![GitHub stars](https://img.shields.io/github/stars/username/repo.svg?style=social&label=Star)](https://github.com/username/repo)
[![GitHub forks](https://img.shields.io/github/forks/username/repo.svg?style=social&label=Fork)](https://github.com/username/repo/fork)

</div>
