import sys
import PyPDF2
from argparse import ArgumentParser

def extract_slides(input_pdf, output_pdf, start_slide, end_slide):
    with open(input_pdf, 'rb') as infile:
        reader = PyPDF2.PdfReader(infile)
        if start_slide < 1 or end_slide > len(reader.pages) or start_slide > end_slide:
            raise ValueError("Invalid slide range")
        writer = PyPDF2.PdfWriter()
        for i in range(start_slide - 1, end_slide):
            writer.add_page(reader.pages[i])
        with open(output_pdf, 'wb') as outfile:
            writer.write(outfile)
        print(f"Slides {start_slide} to {end_slide} extracted to {output_pdf}")

def main():
    parser = ArgumentParser(description="Extract specific slides from a PDF and save them into a new PDF file.")
    parser.add_argument("input_pdf", help="Path to the inpuat PDF file")
    parser.add_argument("start_slide", type=int, help="Start slide number (1-based index)")
    parser.add_argument("end_slide", type=int, help="End slide number (1-based index)")
    args = parser.parse_args()

    output_pdf = args.input_pdf.replace(".pdf", f"_{args.start_slide}-{args.end_slide}.pdf")
    
    extract_slides(args.input_pdf, output_pdf, args.start_slide, args.end_slide)

if __name__ == "__main__":
    main()
