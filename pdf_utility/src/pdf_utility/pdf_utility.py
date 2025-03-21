import os
from pypdf import PdfReader, PdfWriter

def combine_pdfs(input_folder, output_folder, output_pdf_name, selected_files):
    """
    Simply combines PDFs from a folder into one file.
    
    :param input_folder: Path to the folder containing input PDF files
    :param output_folder: Path to the folder where output PDF will be saved
    :param output_pdf_name: Name of the output PDF file
    :param selected_files: List of PDF files to combine in order
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
