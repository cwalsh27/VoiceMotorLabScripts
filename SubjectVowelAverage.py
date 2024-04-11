import os
from openpyxl import *
del open


EaCount = 0
OuCount = 0
AaCount = 0
subjcectName = ""


for filename in os.listdir():
    if filename.endswith("VowelBias.txt"):
        subjectName = filename[:2]
        print(subjectName)
        vowelFreqs = []
        file = open(filename)
        for line in file:
            colonIndex = line.find(":")
            vowelFreqs.append(line[colonIndex+2:].strip())
        EaCount += int(vowelFreqs[0])
        OuCount += int(vowelFreqs[1])
        AaCount += int(vowelFreqs[2])
print(subjectName)
newFile = open(subjectName + "vowelSummary.txt", "w")
newFile.write("Total Ea Count: " + str(EaCount) + "\n")
newFile.write("Total Ou Count: " + str(OuCount) + "\n")
newFile.write("Total A/A Count: " + str(AaCount) + "\n")
newFile.close()






