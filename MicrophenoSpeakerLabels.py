import os
from docx import Document

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
doc_path = os.path.join(desktop_path, r'TextFiles/CSSPRING20230512-181729_Recording_1280x720_MM.docx')
new_doc_path = os.path.join(desktop_path, r'TextFiles/outputFile')

doc = Document(doc_path)
newDoc = Document()

# Text processing
# def strip_trailing_spaces(text):
#     return '\n'.join(line.rstrip() for line in text.split('\n'))
#
# for paragraph in doc.paragraphs:
#     paragraph.text = strip_trailing_spaces(paragraph.text)

# appending line labels
last_speaker_B = False
lines = []
count = 0

for para in doc.paragraphs:
    newP = newDoc.add_paragraph('')
    if para.text[0:2] == "((" and para.text[-2:] == "))":
        newP.add_run(para.text)
    else:
        if any(run.bold for run in para.runs) and not last_speaker_B:
            newP.add_run(f'B{count+1}: {para.text}').bold = True
            last_speaker_B = True
            count += 1
        elif any(run.bold for run in para.runs) and last_speaker_B:
            newP.add_run(para.text).bold = True
            count += 1
        elif last_speaker_B:
            newP.add_run(f'A{count + 1}: {para.text}')
            last_speaker_B = False
            count += 1
        else:
            newP.add_run(para.text)
            count += 1

newDoc.save('outputFile.docx')
