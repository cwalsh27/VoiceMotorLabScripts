import docx
import os
from docx import Document

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
doc_path = os.path.join(desktop_path, r'TextFiles/CSSPRING20230512-181729_Recording_1280x720_MM.docx')

doc = Document(doc_path)

print('List of paragraphs')
for para in doc.paragraphs:
    print(para.text, "\n\n\n")


last_speaker_B = True

for count, para in enumerate(doc.paragraphs):
    if any(run.bold for run in para.runs):
        if not last_speaker_B:
            print("B: " + para.text)
            last_speaker_B = True
    else:
        if last_speaker_B:
            print("A: " + para.text)
            last_speaker_B_ = False

