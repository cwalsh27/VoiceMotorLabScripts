# Voice & Motor Lab
WIP Scripts to extract key data points collected during MRI analysis, Udel Voice & Motor Lab

EPrimeDataExtraction.py: Takes in data sheets from E-Prime scripts and isolates the best trials (as identified by subject input) and other variables of interest. Outputs a new sheet with the desired data, as well as text files with the preferred vocal exercises to isolate any bias towards certain vowel sounds/exercises. 

SubjectVowelAverage.py: Takes any number of vowel files produced by a single subject and sums the totals. 

AudioSpectrumAnalysis.py: Automates extraction of four-second intervals by finding frequency changes in specific regions of larger audio files (based on shifts in MRI noise and vocalizations from the subject) 

MicrophenoSpeakerLabels.py: Text editor that automatically marks each intervention during the interview with an intervention number and a speaker label

AudioRenamer.py: Automatically iterates through every audio file for a given participant, and builds directories to support further processing via Praat scripts. 

