def format_text_file(input_file, output_file, segment_length):
    f = open(input_file, 'r', encoding='utf-8')
        
    # Split the content into segments based on newline character
    formatted_segments = []
    i = 0
    lineNumber = 0
    formatted_segments.append('')

    for line in f:
        formatted_segments[i] += line.strip('\n')
        lineNumber += 1
        if (lineNumber > segment_length):
            lineNumber = 0
            formatted_segments.append('')
            i += 1

    text = ''
    for j in range(len(formatted_segments)):
        text += formatted_segments[j] + "\n\n"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Formatted text saved to {output_file}")
    f.close()

# Path to the input .txt file
input_file = 'output.txt'

# Path to the output formatted .txt file
output_file = 'summarized.txt'

# Segment length (in number of characters, words, or sentences)
segment_length = 200

# Format the text file
format_text_file(input_file, output_file, segment_length)
