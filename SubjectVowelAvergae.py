import os
from openpyxl import *
del open


EaCount = 0
OuCount = 0
AaCount = 0


for filename in os.listdir():
    if filename.endswith("VowelBias.txt"):
        vowelFreqs = []
        file = open(filename)
        for line in file:
            colonIndex = line.find(":")
            vowelFreqs.append(line[colonIndex+2:].strip)
        EaCount += vowelFreqs[0]
        OuCount += vowelFreqs[1]
        AaCount += vowelFreqs[2]




