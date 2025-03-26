# PDF Utility Examples

This guide demonstrates how to use the `pdf_utility` package to combine PDF files.

## Basic Usage

First, let's import the package:

```python
from pdf_utility import combine_pdfs
```

### Example 1: Combining PDFs

Here's a basic example of combining PDF files:

```python
# Define input and output paths
input_folder = "example_pdfs"
output_folder = "output"
output_name = "combined.pdf"

# List of PDFs to combine
files_to_combine = ["file1.pdf", "file2.pdf", "file3.pdf"]

# Combine the PDFs
combine_pdfs(input_folder, output_folder, output_name, files_to_combine)
```

### Example 2: Error Handling

The function handles various error cases gracefully:

```python
# Trying to combine non-existent files
non_existent_files = ["doesnt_exist.pdf"]
combine_pdfs(input_folder, output_folder, "error_test.pdf", non_existent_files)
# Output: No valid PDF files found in: example_pdfs
```

### Example 3: Working with Nested Directories

The function automatically creates output directories if they don't exist:

```python
# Using nested output directory
nested_output = "output/nested/subfolder"
combine_pdfs(input_folder, nested_output, output_name, files_to_combine)
```

## Best Practices

1. Always use full file names including the .pdf extension
2. Make sure you have read permissions for input files
3. Make sure you have write permissions for the output directory
4. Check that input files exist before combining
