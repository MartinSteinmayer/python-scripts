import PyPDF2

def extract_text_from_pdf(pdf_path):
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    text = ""
    for page in pdf_reader.pages:
        extracted_text = page.extract_text()
        text += extracted_text + "\n"

    pdf_file.close()
    return text

# Path to the PDF file
pdf_path = 'pdfs/EIST_w6.pdf'
output_file = 'output.txt'  # Path to the output .txt file

# Extract text from the PDF
extracted_text = extract_text_from_pdf(pdf_path)

# Write the extracted text to a .txt file with UTF-8 encoding
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(extracted_text)

print(f"Text extracted and written to {output_file}")

