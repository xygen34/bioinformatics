'''
Created on Sep 15, 2021
@authors: David Tuttle and Collin Hansen
The program will accept a single DNA input, find possible matches to the prokaryotic promoter -35 and -10 consensus seequences
and output a data frame with best possible matches decending as you read. 
The table outputted gives 
Position, Sequence, Score, -35S Matches, -10S Matches
'''
# importing modules
from fuzzywuzzy import fuzz
import numpy as np
import pandas as pd

# Allows for 3 common ambiguity codes to pass as DNA
dnaDict = {
'Y' : ['C', 'T'],
'R' : ['A', 'G'],
'N' : ['A', 'G', 'T', 'C']
}


# collects possible promoter sequences
promoters = []
# -10 consensus sequence found in most prokaryotes
consensusSequence10 = "TATAAT"
# -35 consensus sequence found in most prokaryotes
consensusSequence35 = "TTGACA"



dna = input("Enter your dna sequence: ") # User inputs DNA sequence (ALL CAPS)
threshold = input ("Enter the percentage of matching nucleotides you want in your consensus sequences: ") # User inputs threshold percent up to 100

# This function makes sure the user inputs DNA correctly
# If DNA is not entered you will be propted to try again
def dna_check(dna):
    dna_list = ["A","T","G","C"]
 
    dna_match = [nucleotides in dna_list for nucleotides in dna]
 
    res =  all(dna_match)
 
    if res == True:
        return
    if res == False:
        print("You did not enter DNA try again") 
dna_check(dna)

# Goes into the DNA sequence and finds possibple matches for both the -35 and the -10 consensus sequences
# that meet the user given threshold and gives them a score based on how well they match. This makes it 
# possible so see through nucleotide ambiguity and get the best possible matches. Even though -35 and -10
# seem like they would be 25 nucleotides apart we did not assume that below since not all prokaryotes are
# the same and biological data varries. 

def findPromoter(dna):
    for i in range(0, len(dna)):
        sequence35 = dna[i : i+6]
        ratio35=fuzz.ratio(sequence35, consensusSequence35)
        match35 = (ratio35/100) * 6
        int(match35)
        if ratio35 > int(threshold):   
                result35 = dna[i : len(dna)]            
                for n in range(i, len(result35)):
                    sequence10 = result35[n : n+6]
                    ratio10=fuzz.ratio(sequence10, consensusSequence10)
                    match10 = (ratio10/100) * 6
                    if ratio10 > int(threshold):
                        finalRatio = (ratio10+ratio35)/2
                        result10 = dna[i : i+n+6]
                        promoters.append(i)
                        promoters.append(result10)
                        promoters.append(finalRatio)
                        promoters.append(round(match35))
                        promoters.append(round(match10))
findPromoter(dna)

# We are setting up our data to be outputted in a clean manner. Most biological data bases present data cleanly
# such as ensembl or ncbi. We organize our data from above into an arrray then make a data frame for easy manipulation and reading.
# The resulting data frame will be sorted by score in decending order.
num = np.array(promoters)
reshaped = num.reshape(int(len(promoters)/5) , 5)
pd.set_option('display.max_columns', None)

dataFrame = pd.DataFrame(reshaped, columns = ['Position', 'Sequence', 'Score', '-35S Matches', '-10S Matches'])

pd.set_option('display.expand_frame_repr', False, 'colheader_justify', 'center') # Makes the dataframe stay on one line and centers the headers

dataFrame.Score = pd.to_numeric(dataFrame.Score, errors='coerce') # Fixes how sort_values sorts the columns correcting the lexsorted result

new = dataFrame.sort_values('Score', ascending = False) # Sorts scores in decending order

print(new) #If you only want to see the top 10 possible sequences type this : ' print(new.head(10)) ' instead
