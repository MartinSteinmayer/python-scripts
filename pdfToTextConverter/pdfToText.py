import PyPDF2
import unicodedata

def extract_text_from_pdf(pdf_path, firstPage, lastPage):
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    exclude_text = "Bhatotia, Brügge, Krusche"
    text = ""
    pages = pdf_reader.pages
    for i in range(firstPage-1, lastPage):
        extracted_text = pages[i].extract_text()
        lines = extracted_text.strip().split("\n")

        # Filter out lines containing the excluded text and remove non-alphanumeric characters
        filtered_lines = []
        for line in lines:
            line = line.strip()
            if line and exclude_text not in line:
                line = ''.join(c for c in line if c.isalnum() or c.isspace())
                filtered_lines.append(line)
        
        # Append the filtered lines to the text
        text += "\n".join(filtered_lines) + "\n\n"
    pdf_file.close()
    return text

# Rest of the code remains the same


# Rest of the code remains the same


def remove_repeated_words(text):
    # Split the sentence into a list of words
    words = text.split()

    wordsToDelete = []
    for word in words:
        count = count_word_occurrences(words, word)
        if (count > 70):
            wordsToDelete.append(word)

    # Create a new list without the specified word
    new_words = []

    for word in words:
        toDelete = False
        for wordToDelete in wordsToDelete:
            if (word == wordToDelete):
                toDelete = True
        if (toDelete == False):
            new_words.append(word + " ")
    # Join the remaining words back into a sentence
    new_text = ' '.join(new_words)
    return new_text

def remove_word(text, wordToDelete):
    words = text.split(" ")


    # Create a new list without the specified word
    new_words = []

    for word in words:
        print(word)
        if (word != wordToDelete):
            new_words.append(word + " ")
    # Join the remaining words back into a sentence
    new_text = ' '.join(new_words)
    return new_text

def count_word_occurrences(words, word):
    count = 0
    for w in words:
        if w == word:
            count += 1
    return count
# Path to the PDF file

def produce_text(pdfName):
    pdf_path = "pdfToTextFunc\pdfToTextConverter\pdfs" + str(pdfName) + ".pdf"
    output_file = 'output.txt'  # Path to the output .txt file

    # Extract text from the PDF
    extracted_text = extract_text_from_pdf(pdf_path, 30, 42)

    # Write the extracted text to a .txt file with UTF-8 encoding
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(extracted_text)

    print(f"Text extracted and written to {output_file}")

produce_text("\gad_w6")