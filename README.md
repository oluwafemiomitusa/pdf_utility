# PDF Utility 📄

[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A robust Python utility for merging multiple PDF files into a single document while maintaining the specified order. Perfect for combining chapters, reports, or any series of PDF documents into a unified file.

## ✨ Features

- Combines multiple PDF files into a single output document
- Preserves the original order of files as specified
- Robust error handling for invalid or missing files
- Automatically creates output directory if it doesn't exist
- Simple and clean API for easy integration
- Memory-efficient processing of PDF files

## 🔧 Requirements

- Python 3.x
- `pypdf` library

## 📦 Installation

1. Ensure you have Python 3.x installed
2. Install the required dependency:

```bash
pip install pypdf
```

## 🚀 Usage

### As a Module

```python
from pdf_utility import combine_pdfs

# Define your paths and files
input_folder = '/path/to/input/folder'
output_folder = '/path/to/output/folder'
output_pdf_name = 'combined_output.pdf'

# List files in the order you want them combined
selected_files = [
    'chapter1.pdf',
    'chapter2.pdf',
    'chapter3.pdf'
]

# Combine PDFs
combine_pdfs(input_folder, output_folder, output_pdf_name, selected_files)
```

### As a Script

The script includes a built-in example that can be modified:

```python
if __name__ == "__main__":
    input_folder = '/path/to/input/folder'
    output_folder = '/path/to/output/folder'
    output_pdf_name = 'combined_output.pdf'
    
    selected_files = [
        'file1.pdf',
        'file2.pdf',
        'file3.pdf'
    ]
    
    combine_pdfs(input_folder, output_folder, output_pdf_name, selected_files)
```

## 📝 Function Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input_folder` | str | Path to the folder containing input PDF files |
| `output_folder` | str | Path to the folder where output PDF will be saved |
| `output_pdf_name` | str | Name of the output PDF file |
| `selected_files` | list | List of PDF filenames to combine in order |

## ⚠️ Error Handling

The utility includes robust error handling:

- Checks for valid PDF files in the input folder
- Skips invalid or missing files with appropriate error messages
- Creates output directory if it doesn't exist
- Provides clear error messages for troubleshooting

Common error messages:
- `"No valid PDF files found in: {input_folder}"` - Check if your input folder path is correct
- `"Error processing {pdf_file}: {error}"` - Individual file processing errors

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔍 Troubleshooting

1. **Files not being combined?**
   - Verify that the file names in `selected_files` match exactly (case-sensitive)
   - Ensure all paths are absolute or properly referenced

2. **Permission errors?**
   - Check if you have read permissions for input files
   - Verify write permissions for the output folder

3. **Invalid PDF errors?**
   - Confirm that all input files are valid PDFs
   - Check if PDFs are not password-protected
