import os
from pypdf import PdfReader, PdfWriter

def combine_pdfs(input_folder, output_folder, output_pdf_name, selected_files):
    """
    Combine multiple PDF files from a folder into a single file.

    Parameters
    ----------
    input_folder : str
        Path to the folder containing input PDF files.
    output_folder : str
        Path to the folder where output PDF will be saved.
    output_pdf_name : str
        Name of the output PDF file.
    selected_files : list of str
        List of PDF files to combine in order.

    Returns
    -------
    None
        The function creates a combined PDF file at the specified location.

    Examples
    --------
    >>> from pdf_utility import combine_pdfs
    >>> input_dir = "path/to/pdfs"
    >>> output_dir = "path/to/output"
    >>> files = ["doc1.pdf", "doc2.pdf", "doc3.pdf"]
    >>> combine_pdfs(input_dir, output_dir, "combined.pdf", files)

    Notes
    -----
    - Creates output directory if it doesn't exist
    - Skips invalid or non-existent files
    - Maintains original page order as specified in selected_files
    """
    # Get full paths of selected files
    pdf_files = [os.path.join(input_folder, f) for f in selected_files if os.path.isfile(os.path.join(input_folder, f))]
    if not pdf_files:
        print(f"No valid PDF files found in: {input_folder}")
        return
    
    # Create PDF writer
    pdf_writer = PdfWriter()
    
    # Add pages from each PDF
    for pdf_file in pdf_files:
        try:
            pdf_reader = PdfReader(pdf_file)
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)
        except Exception as e:
            print(f"Error processing {pdf_file}: {e}")
    
    # Create output folder if needed
    os.makedirs(output_folder, exist_ok=True)
    
    # Save combined PDF
    output_pdf_path = os.path.join(output_folder, output_pdf_name)
    with open(output_pdf_path, 'wb') as out_file:
        pdf_writer.write(out_file)
    
    print(f"Combined PDF saved to {output_pdf_path}")
