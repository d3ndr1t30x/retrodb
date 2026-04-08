# RetroDB - ExploitDB Web Interface

A modern, user-friendly web interface for searching and browsing the ExploitDB database. RetroDB provides a clean, searchable front-end to make security research and vulnerability analysis more accessible and efficient.

## Features

- **Full-Text Search**: Search across all exploit descriptions
- **Advanced Filtering**: Filter exploits by platform and type
- **Syntax Highlighting**: View exploit code with color-coded syntax highlighting for multiple languages (Python, C/C++, PHP, Ruby, Perl, Java, and more)
- **Quick Preview**: Browse exploit details and descriptions directly in the interface
- **File Download**: Download exploit files for offline analysis
- **Responsive Design**: Clean, modern web interface
- **Large Database**: Access to thousands of exploits across multiple platforms and categories

## Requirements

- Python 3.7+
- Flask
- Pygments
- Modern web browser

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/d3ndr1t30x/retrodb.git
   cd retrodb
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # or
   source .venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install flask pygments
   ```

## Usage

1. **Start the application:**
   ```bash
   python app.py
   ```

2. **Open your browser and navigate to:**
   ```
   http://localhost:5000
   ```

3. **Search and filter exploits:**
   - Use the search bar to find exploits by keyword
   - Filter by platform (Linux, Windows, Android, etc.)
   - Filter by type (DoS, Remote, Local, WebApp, etc.)
   - Click on any exploit to view details and syntax-highlighted code

4. **Download exploits:**
   - Click the download button on any exploit detail page to save the file locally

## Project Structure

```
retrodb/
├── app.py                  # Main Flask application
├── templates/
│   ├── index.html         # Main search/listing page
│   └── exploit.html       # Individual exploit detail page
├── exploitdb/             # ExploitDB data (submodule/data directory)
│   ├── files_exploits.csv # Exploit metadata
│   ├── exploits/          # Exploit files organized by platform
│   └── shellcodes/        # Shellcode files
└── README.md              # This file
```

## Features in Detail

### Search Functionality
- Search across exploit descriptions and metadata
- Real-time filtering as you type
- Results displayed on the main page

### Platform Support
Supports exploits for:
- Linux (x86, x86-64, MIPS, SPARC, ARM)
- Windows (x86, x86-64)
- macOS/OSX
- Android
- iOS
- BSD variants (FreeBSD, OpenBSD, NetBSD)
- And many more...

### Exploit Types
- **DoS**: Denial of Service exploits
- **Remote**: Remote code execution exploits
- **Local**: Local privilege escalation exploits
- **WebApp**: Web application vulnerabilities

### Code Syntax Highlighting
Automatically detects and highlights code based on file extension:
- Python (.py)
- C (.c, .h)
- C++ (.cpp, .cc, .cxx, .hpp)
- PHP (.php)
- Ruby (.rb)
- Perl (.pl)
- Java (.java)
- And others with automatic detection

## Configuration

### Modifying Port
Edit `app.py` to change the default port (currently 5000):
```python
if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

### Database Updates
The exploit database is stored in the `exploitdb/` directory. To update with the latest exploits, update the CSV files and exploit files.

## Security Considerations

- This tool is intended for **authorized security research only**
- Always obtain proper authorization before testing exploits
- Use exploits only in controlled lab environments
- Respect all applicable laws and regulations in your jurisdiction
- The creator assumes no responsibility for misuse

## ExploitDB Attribution

This project uses the ExploitDB database. For more information about ExploitDB, visit: https://www.exploit-db.com/

## License

This project is built as a front-end interface for the ExploitDB database. Please refer to the ExploitDB license for terms regarding the exploit data: `exploitdb/LICENSE.md`

## Contributing

Contributions are welcome! Feel free to:
- Report bugs and issues
- Suggest improvements
- Submit pull requests
- Improve documentation

## Disclaimer

RetroDB is provided as-is for educational and authorized security research purposes only. The creators and contributors are not responsible for:
- Any damage caused by the use or misuse of exploits
- Legal issues arising from unauthorized access or testing
- Any other harmful activities

Always ensure you have proper authorization before using any exploits or penetration testing tools.

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Last Updated**: April 2026

**Status**: Active Development
