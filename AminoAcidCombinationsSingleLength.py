from itertools import product
from time import time
import os

amino_acids = 'ACDEFGHIKLMNPQRSTVWY'
sequence_length = 3 #CAREFUL, TOO MUCH (more than 7) WILL FILL UP HARD DRIVE

print(amino_acids)
print(str(len(amino_acids)) + ' different Amino Acids possible \n')
print('Minimum sequence length is' + )


start_time = time() #tracks time at start


counter = 0 #for user interface purposes

with open('all_amino_acid_sequences.txt', 'a') as output_file:

    for sequence in product(amino_acids, repeat=sequence_length): #cartesian product (permutation)
        sequence_string = ''.join(sequence) #tuple -> string
        output_file.write(sequence_string + '\n') #write sequence to file

        if counter % 1000123 == 0: #for user interface purposes
            print(sequence_string)
            print('percent done: ' + str(round(counter/(20**sequence_length)*100, 2)) + '%')
            #print('Runtime is ' + str(round(time() - start_time, 2)) + ' seconds')
            print('...')

        counter += 1



print('Done! Took ' + str(round(time() - start_time, 2)) + ' seconds.')

print('Correct ')
print('File size: ' + str(os.stat('all_amino_acid_sequences.txt').st_size) + ' bytes')

#program is currently CPU-bound, not IO
#need to implement multiprocess module
#or drop down into C code?
