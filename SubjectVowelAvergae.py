import os
from openpyxl import *
del open


EaCount = 0
OuCount = 0
AaCount = 0
subjcectName = ""


for filename in os.listdir():
    if filename.endswith("VowelBias.txt"):
        subjcectName = filename[:-13]
        vowelFreqs = []
        file = open(filename)
        for line in file:
            colonIndex = line.find(":")
            vowelFreqs.append(line[colonIndex+2:].strip)
        EaCount += vowelFreqs[0]
        OuCount += vowelFreqs[1]
        AaCount += vowelFreqs[2]


newFile = open(subjcectName, "w")
newFile.write("Total Ea Count: " + str(EaCount) + "\n")
newFile.write("Total Ou Count: " + str(OuCount) + "\n")
newFile.write("Total A/A Count: " + str(AaCount) + "\n")
newFile.close()






