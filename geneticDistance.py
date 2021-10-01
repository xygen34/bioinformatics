'''
Created on Sep 30, 2021

@author: David Tuttle Collin Hansen

Purpose:

This program will take in user-defined variables for population size, mutation rate, the total number of generations, the generation a speciation event occurs, and the starting DNA sequence.  From this, the program will simulate the molecular evolution of a population’s DNA before and after a speciation event occurs. 

The population size for all generations up to the speciation event will be the user-defined population. Once the speciation event occurs the population is divided into two. If the population is an odd number it will simply split to the nearest whole number. For example, a population of five will be split into an isolated population of two and three after the speciation event. 

The molecular evolution this program is simulating is neutral evolution. You can see the genetic drift between populations’ DNA as N generations pass. This is measured by calculating the genetic distance between each individual within a population. 

The data outputted will be an array of genotypes and an array of the average genetic distance within each population. 

A line graph will be created showing the relation of genetic distance over the total number of generations.


Example Test Case:
Population Size = 20, Mutation Rat e= 1, Total Generations = 50, Speciation Event = 35, Sequence = AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

'''
import random #Used to create a random number in the mutate function
import matplotlib.pyplot as plt #Used to create a line graph of the data

# User input with data validation
pop_size = int(input("How large is the population: ")) 
if pop_size <= 0:
    print("Your population is not valid. Please try a number greater than 0.")
    exit()
mut_rate = int(input("What would you like your mutation rate to be (0-100): "))
if mut_rate < 0 or mut_rate>100:
    print("Your mutation rate is not valid. Please try a number between 0 and 100.")
    exit()
total_gen = int(input("How many generations would you like to simulate for: "))
if total_gen < 0:
    print("That generation does not exist. Please try a number greater than zero.")
    exit()
speciation_gen = int(input("What generation would you like the speciation event to occur at: "))
if speciation_gen < 0:
    print("That generation does not exist. Please try a number greater than zero.")
    exit()   
sequence = input("Enter the DNA sequence for the population base population: ")

sequence.upper() # makes DNA sequence uppercase if it is not already

# Mutation Dictionaries
A_Mutation = ["G", "T", "C"]
G_Mutation = ["T", "C", "A"]
C_Mutation = ["G", "A", "T"]
T_Mutation = ["C", "A", "G"]

# Empty arrays
speciation_sequences1 = []
speciation_sequences2 = []
sum_values = []
spec_sum_values1 = []
spec_sum_values2 = []
genetic_distance_values=[]
spec_genetic_distance_values1 = []
spec_genetic_distance_values2 = []
generation_counter = []
spec_generation_counter = []

# implicit DNA check; validates the users DNA sequence 
def dna_check(sequence):
    dna_list = ["A","T","G","C"]
 
    dna_match = [nucleotides in dna_list for nucleotides in sequence]
 
    res =  all(dna_match)
 
    if res == True:
        return
    if res == False:
        print("You did not enter DNA try again")
        
        
        
individual_sequences = []
#The following for loop will take the suggested population size and add the stated
#base sequence to the declared array "individual_sequences"
for i in range(0, pop_size):
    individual_sequences.append(sequence)    

#The mutate function takes all the values in our array and generates a random
#value between 1 and 100 for each character in each element and if said
#value is below the designated value then our nucleotide will be assigned
#a value different than its original. This simulates random chance a nucleotide 
#is changed from one generation to the next based on the user defined mutation rate.
def mutate(individual_sequences):
    for j in range(0, pop_size):
        for i in range(0, len(sequence)):
            mut_determiner=random.randint(0, 100)
            if mut_determiner < mut_rate:
                sequence_list=list(individual_sequences[j])
                if sequence_list[i] == "A":
                    sequence_list[i] = random.choice(A_Mutation)
                elif sequence_list[i] == "G":
                    sequence_list[i] = random.choice(G_Mutation)
                elif sequence_list[i] == "C":
                    sequence_list[i] = random.choice(C_Mutation)
                elif sequence_list[i] == "T":
                    sequence_list[i] = random.choice(T_Mutation)

                individual_sequences[j] = ''.join(sequence_list)
    individual_sequences.append(individual_sequences[j])

#This function takes all the values in our first array of speciated elements and generates a random
#value between 1 and 100 for each character in each element and if said
#value is below the designated value then our nucleotide will be assigned
#a value different than its original. This simulates random chance a nucleotide 
#is changed from one generation to the next based on the user defined mutation rate.
def spec_mutate1(speciation_sequences1):
    for j in range(0, len(speciation_sequences1)):
        for i in range(0, len(sequence)):
            mut_determiner=random.randint(0, 100)
            if mut_determiner < mut_rate:
                sequence_list=list(speciation_sequences1[j])
                if sequence_list[i] == "A":
                    sequence_list[i] = random.choice(A_Mutation)
                elif sequence_list[i] == "G":
                    sequence_list[i] = random.choice(G_Mutation)
                elif sequence_list[i] == "C":
                    sequence_list[i] = random.choice(C_Mutation)
                elif sequence_list[i] == "T":
                    sequence_list[i] = random.choice(T_Mutation)

                speciation_sequences1[j] = ''.join(sequence_list)
    speciation_sequences1.append(speciation_sequences1[j])
    
#This function takes all the values in our second array of speciated elements and generates a random
#value between 1 and 100 for each character in each element and if said
#value is below the designated value then our nucleotide will be assigned
#a value different than its original. This simulates random chance a nucleotide 
#is changed from one generation to the next based on the user defined mutation rate.
def spec_mutate2(speciation_sequences2):
    for j in range(0, len(speciation_sequences2)):
        for i in range(0, len(sequence)):
            mut_determiner=random.randint(0, 100)
            if mut_determiner < mut_rate:
                sequence_list=list(speciation_sequences2[j])
                if sequence_list[i] == "A":
                    sequence_list[i] = random.choice(A_Mutation)
                elif sequence_list[i] == "G":
                    sequence_list[i] = random.choice(G_Mutation)
                elif sequence_list[i] == "C":
                    sequence_list[i] = random.choice(C_Mutation)
                elif sequence_list[i] == "T":
                    sequence_list[i] = random.choice(T_Mutation)

                speciation_sequences2[j] = ''.join(sequence_list)
    speciation_sequences2.append(speciation_sequences2[j])
 
#This function takes all of our elements in the individuaL sequences array
# it then compares each element to all other elements in the array
#counting up each nucleotide difference finding the average distance and
#then adding the average to a new array. Gentic distance is a measure of the 
#genetic divergence between populations of a species. 
def genetic_distance(individual_sequences):
    distance_sum=0
    num_comparisons =0    
    for i in range(0, len(individual_sequences)):
        for j in range(i+1, len(individual_sequences)):
            num_comparisons += 1
            for k in range (0, len(sequence)):
                num_comparisons +=1
                compare_list1 = list(individual_sequences[i])
                compare_list2 = list(individual_sequences[j])
                if compare_list1[k] != compare_list2[k]:
                    distance_sum +=1
    distance_sum = distance_sum/num_comparisons;
    sum_values.append(distance_sum)

#This function takes all of our elements in the first speciated sequences array
# it then compares each element to all other elements in the array
#counting up each nucleotide difference finding the average distance and
#then adding the average to a new array.
def spec_genetic_distance1(speciation_sequences1):
    distance_sum=0
    num_comparisons= 0
    for i in range(0, len(speciation_sequences1)):
        for j in range(i+1, len(speciation_sequences1)):
            num_comparisons +=1
            for k in range (0, len(sequence)):
                compare_list1 = list(speciation_sequences1[i])
                compare_list2 = list(speciation_sequences1[j])
                if compare_list1[k] != compare_list2[k]:
                    distance_sum +=1
    distance_sum=distance_sum/num_comparisons
    spec_sum_values1.append(distance_sum)
    
#This function takes all of our elements in the second speciated sequences array
# it then compares each element to all other elements in the array
#counting up each nucleotide difference finding the average distance and
#then adding the average to a new array
def spec_genetic_distance2(speciation_sequences2):
    distance_sum=0
    num_comparisons= 0
    for i in range(0, len(speciation_sequences2)):
        for j in range(i+1, len(speciation_sequences2)):
            num_comparisons +=1
            for k in range (0, len(sequence)):
                compare_list1 = list(speciation_sequences2[i])
                compare_list2 = list(speciation_sequences2[j])
                if compare_list1[k] != compare_list2[k]:
                    distance_sum +=1
    distance_sum=distance_sum/num_comparisons
    spec_sum_values2.append(distance_sum)
    
#The reproduce function takes the elements of our array and puts them through 
#the mutate function and the genetic_distance function.                   
def reproduce(individual_sequences):
    for i in range(0, total_gen):
        if i < speciation_gen:
            mutate(individual_sequences)
            individual_sequences.pop(-1)
            genetic_distance(individual_sequences)
                
reproduce(individual_sequences)

#the following line is where we take our array and split it down the middle
#and inputting it into their own separate arrays
speciation_sequences1 = individual_sequences[:len(individual_sequences)//2]
speciation_sequences2 = individual_sequences[len(individual_sequences)//2:]

#the following for loop is a pseudo reproduce function that puts
#our speciation sequences through their respective mutate and genetic distance
#functions.
for i in range(0, total_gen - speciation_gen):
    spec_mutate1(speciation_sequences1)
    speciation_sequences1.pop(-1)
    spec_mutate2(speciation_sequences2)
    speciation_sequences2.pop(-1)
    spec_genetic_distance1(speciation_sequences1)
    spec_genetic_distance2(speciation_sequences2)
    
#Take our sum_values elements and find their full genetic distance
#then add the resulting values to a new array
for i in range(0, len(sum_values)):
    genetic_distance_values.append((sum_values[i]))
    
#Take our speciated_sum_values elements and find their full genetic distance
#then add the resulting values to a new array    
for i in range(0, len(spec_sum_values1)):
    spec_genetic_distance_values1.append((spec_sum_values1[i])*(1/len(sequence)))
    spec_genetic_distance_values2.append((spec_sum_values2[i])*(1/len(sequence)))

#The following if condition happens if we don't experience a speciation event
#so we instead graph only the genetic_distance of our individual sequence
if speciation_gen > total_gen:
    print(individual_sequences)
    print(genetic_distance_values)
    for i in range(0, len(genetic_distance_values)):
        generation_counter.append(i)
    plt.plot(generation_counter, genetic_distance_values, label = "Original population")
    plt.title('Average Genetic Distance Over Generations')
    plt.xlabel('Generations')
    plt.ylabel('Average Genetic Distance')
    plt.legend()
    plt.show()

#The following if condition happens if we do experience a speciation event
#so we instead graph the genetic_distance of our individual sequence and
#our speciated sequences
else:
    print(speciation_sequences1)
    print(speciation_sequences2)
    print(genetic_distance_values)
    for i in range(0, len(genetic_distance_values)):
        generation_counter.append(i)
    for i in range(speciation_gen, total_gen):
        spec_generation_counter.append(i)
    plt.plot(generation_counter, genetic_distance_values, label = "Original population")
    plt.plot(spec_generation_counter, spec_genetic_distance_values1, label = "Speciation event pop. one")
    plt.plot(spec_generation_counter, spec_genetic_distance_values2, label = "Speciation event pop. two")
    plt.title('Average Genetic Distance Over Generations')
    plt.xlabel('Generations')
    plt.ylabel('Average Genetic Distance')
    plt.legend()
    plt.show()
