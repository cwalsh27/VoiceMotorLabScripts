import os

text_dir = r'TextFiles'
text_file = os.path.join(text_dir, 'TextFiles/CSSPRING20230512-181729_Recording_1280x720.docx')

def add_line_numbers(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read the content of the file
            lines = file.readlines()

        # Open the file in write mode to overwrite the content with line numbers
        with open(filename, 'w') as file:
            # Iterate over each line and add line numbers
            for i, line in enumerate(lines, start=1):
                if i % 2 == 1:
                    file.write(f"B{i}: {line}")
                else:
                    file.write(f"A{i}: {line}")


        print("Line numbers added successfully.")
    except FileNotFoundError:
        print("File not found.")

# Example usage
filename = 'example.txt'  # Replace 'example.txt' with your file name
add_line_numbers('TextFiles/CSSPRING20230512-181729_Recording_1280x720.txt')