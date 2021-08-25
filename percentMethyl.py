# Collin Hansen
# Finds the number of chosen methylated nucleotide and gives you the percentage of chosen methylated nucleotide
# This assumes the user's input is capital letters for unmethylated and lowercase for methylated
# Methyalted: atgcatgc
# Unmethylated: ATGCATGC

def main():
    userLetter = input('Enter methylated nucleotide Letter: ') # lower case
    userletter2 = input('Enter unmethylated nucleotide Letter: ') # capitalized
    dna = input('Enter single strand DNA sequence: ') # only enter one strand at a time
    dna = list(dna) # converts dna variable into a list

    letterCount = 0
    for sequence in dna:
        letterCount += sequence.count(userLetter)

    letterCount2 = 0
    for sequence in dna:
        letterCount2 += sequence.count(userletter2)


    total = letterCount2 + letterCount

    percentage = letterCount / total

    print(format(percentage, '0.2f'))

main()