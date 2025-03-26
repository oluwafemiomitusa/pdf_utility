import os
import pytest
from pypdf import PdfWriter
from pdf_utility.pdf_utility import combine_pdfs

@pytest.fixture
def sample_pdfs(tmp_path):
    """Create sample PDF files for testing"""
    pdf_dir = tmp_path / "pdfs"
    pdf_dir.mkdir()
    
    # Create two simple PDF files
    for i in range(2):
        pdf_path = pdf_dir / f"test{i+1}.pdf"
        writer = PdfWriter()
        writer.add_blank_page(width=100, height=100)
        with open(pdf_path, "wb") as f:
            writer.write(f)
    
    return {
        "input_dir": pdf_dir,
        "output_dir": tmp_path / "output",
        "files": [f"test{i+1}.pdf" for i in range(2)]
    }

def test_combine_pdfs_success(sample_pdfs):
    """Test successful PDF combination"""
    combine_pdfs(
        sample_pdfs["input_dir"],
        sample_pdfs["output_dir"],
        "combined.pdf",
        sample_pdfs["files"]
    )
    
    output_file = sample_pdfs["output_dir"] / "combined.pdf"
    assert output_file.exists()

def test_combine_pdfs_empty_list(sample_pdfs):
    """Test behavior with empty file list"""
    combine_pdfs(
        sample_pdfs["input_dir"],
        sample_pdfs["output_dir"],
        "combined.pdf",
        []
    )
    
    output_file = sample_pdfs["output_dir"] / "combined.pdf"
    assert not output_file.exists()

def test_combine_pdfs_invalid_file(sample_pdfs):
    """Test error handling for invalid files"""
    invalid_files = ["nonexistent.pdf"]
    combine_pdfs(
        sample_pdfs["input_dir"],
        sample_pdfs["output_dir"],
        "combined.pdf",
        invalid_files
    )
    
    output_file = sample_pdfs["output_dir"] / "combined.pdf"
    assert not output_file.exists()

def test_combine_pdfs_output_creation(sample_pdfs):
    """Test output directory creation"""
    nested_output = sample_pdfs["output_dir"] / "nested" / "dir"
    
    combine_pdfs(
        sample_pdfs["input_dir"],
        nested_output,
        "combined.pdf",
        sample_pdfs["files"]
    )
    
    output_file = nested_output / "combined.pdf"
    assert output_file.exists()
    assert nested_output.is_dir()
