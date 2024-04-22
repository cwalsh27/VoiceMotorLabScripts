import os
from docx import Document

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
doc_path = os.path.join(desktop_path, r'TextFiles/CSSPRING20230512-181729_Recording_1280x720_MM.docx')
new_doc_path = os.path.join(desktop_path, r'TextFiles/outputFile')

doc = Document(doc_path)
newDoc = Document()


# appending line labels
last_speaker_B = False
lines = []
count = 0

# for para in doc.paragraphs:
#     for run in para.runs:
#         print(run.text, "\n")

# original draft
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

newDoc.save('newfile.docx')


def parenthetical_check(paragraph):
    if paragraph.text[0::2] == "((" and para.text[-2:] == "))":
        return True
    else:
        return False

def bold_bracket_check(paragraph):
    if "]" in para.text:
        # deal with that
    else:
        # deal with interruption clause
    print("nailed it again")

def bold_check(paragraph):
    if paragraph.text[0] == "[":
        return bold_bracket_check(paragraph)
    else:
        if para.runs[0].bold:
            return True
        else:
            return False

# 2.0
for para in doc.paragraphs:
    newP = newDoc.add_paragraph('')

    # check for double paranthetical
    if parenthetical_check(para):
        newP.add_run(para.text)
    elif bold_check(para):
        print("do stuff")





    # check for non-bold brackets at start of string
    elif para.text[0] == "[":
        bracketFound = False
        for run in para.runs:
            if "]" in run.text:
                bracketFound = True
            elif bracketFound and "\n" not in run.text:


                # do something about it

    # TO DO: make helper functions for different line types and then implement
    else:
        # check for
        if para.runs[0].bold and not last_speaker_B:
            newP.add_run(f'B{count + 1}: {para.text}').bold = True
            last_speaker_B = True
            count += 1
        elif para.runs[0].bold and last_speaker_B:
            newP.add_run(para.text).bold = True
            count += 1
        elif last_speaker_B:
            newP.add_run(f'A{count + 1}: {para.text}')
            last_speaker_B = False
            count += 1
        else:
            newP.add_run(para.text)
            count += 1
