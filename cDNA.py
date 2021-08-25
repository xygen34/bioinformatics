# Collin Hansen
# The user will input a DNA sequcence and the complent strand will be printed below
def main():
    dna = input('Enter DNA sequence: ') # Enter in all caps

    dna = dna[::-1] # reverses the sequence

    bp={"A":"T","T":"A","G":"C","C":"G"} 

    dna=list(dna) # converts dna into a list

    for index,letter in enumerate(dna): # enumerate allows you to loop over an iterable object and keep track of how many iterations have occurred

        for key,value in bp.items():

            if letter==key:
                dna[index]=value

    print(''.join(dna))
main()
  




