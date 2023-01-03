import sys
import os

from weasyprint import HTML
from ghostscript import Ghostscript


def html_to_image(html_file_path: str, image_file_path: str):
    # Convert the HTML file to a PDF
    html = HTML(html_file_path)
    pdf_file_path = html_file_path.replace(".html", ".pdf")
    html.write_pdf(pdf_file_path)

    # Use Ghostscript to convert the PDF to an image
    args = [
        "gs",
        "-sDEVICE=jpeg",
        "-dJPEGQ=95",
        "-dNOPAUSE",
        "-dBATCH",
        "-dSAFER",
        "-dGraphicsAlphaBits=4",
        "-dTextAlphaBits=4",
        f"-sOutputFile={image_file_path}",
        pdf_file_path,
    ]
    Ghostscript(*args)


if __name__ == "__main__":
    # Ensure that the correct number of arguments have been passed in
    if len(sys.argv) != 3:
        print("Usage: python html_to_image.py html_file_path image_file_path")
        sys.exit(1)

    # Get the HTML file path and image file path from the command line arguments
    html_file_path = sys.argv[1]
    image_file_path = sys.argv[2]

    # Convert the HTML file to an image
    html_to_image(html_file_path, image_file_path)
