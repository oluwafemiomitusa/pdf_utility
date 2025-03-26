# PDF Utility Documentation

Welcome to the PDF Utility documentation. This package provides tools for managing PDF files.

```{include} ../README.md
:start-after: # pdf_utility
```

## Table of Contents

```{toctree}
:maxdepth: 1
:hidden:

example
changelog
contributing
conduct
autoapi/index
```

## Quick Links

* {ref}`genindex`
* {ref}`modindex`
* {ref}`search`

## Features

* Combine multiple PDFs into a single file
* Automatic output directory creation
* Error handling for invalid files
* Preserves original page order

## Installation

```bash
pip install pdf_utility
```

## Basic Usage

```python
from pdf_utility import combine_pdfs

# Combine multiple PDFs
combine_pdfs(
    input_folder="path/to/pdfs",
    output_folder="path/to/output",
    output_pdf_name="combined.pdf",
    selected_files=["doc1.pdf", "doc2.pdf", "doc3.pdf"]
)
```

For more detailed examples, check out our [example notebook](example.ipynb).
