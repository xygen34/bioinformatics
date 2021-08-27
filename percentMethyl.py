# Collin Hansen
# States the number of methylated Adenines and Cytosine and find the percentage of each that are methylated
# This assumes the user's input is capital letters for unmethylated and lowercase for methylated
# Methyalted: atgcatgc
# Unmethylated: ATGCATGC

def main():

    methylAdenine = 'a'
    adenine = 'A'
    methylCytosine = 'c'
    cytosine = 'C' 

# Enter DNA strand
    dna = input('Enter single strand DNA sequence: ') # only enter one strand at a time
    dna = list(dna) # converts dna variable into a list
    

# Cytosine

    methylCytosineCount = 0
    for sequence in dna:
        methylCytosineCount += sequence.count(methylCytosine)

    cytosineCount = 0
    for sequence in dna:
        cytosineCount += sequence.count(cytosine)


    cytosineTotal = methylCytosineCount + cytosineCount

    methylCytosinePercentage = methylCytosineCount / cytosineTotal

    print('Number of Methylated Cytosines: ', methylCytosineCount)
    print('Percent Cytosine Methylated: ', format(methylCytosinePercentage * 100, '0.0f'))
    
# Adenine

    methylAdenineCount = 0
    for sequence in dna:
        methylAdenineCount += sequence.count(methylAdenine)

    adenineCount = 0
    for sequence in dna:
        adenineCount += sequence.count(adenine)


    adenineTotal = methylAdenineCount + adenineCount
    adenineTotal = int(adenineTotal)

    methylAdeninePercentage = methylAdenineCount / adenineTotal

    
    print('Number of Methylated Adenines: ', methylAdenineCount)
    print('Percent Adenine Methylated: ', format(methylAdeninePercentage * 100, '0.0f'))
    
main()
