#Python 3

#Written by Griffin Calme
#This script will generate all of the possible amino acid sequences for the specified sequence length
#and for all smaller lengths down to the minimum sequence length.
#It saves these sequences in a file called "all_amino_acid_sequences.fasta" in the local directory

#Since the number of lines is dependent on 20^sequence_length the file size will grow exponentially
#Be careful when running for more than 7-long peptide sequences
#All 6-long is about 1GB (with header data), 7-long sequences is about 22GB, 8-long will therefore be ~450GB and so on.

from itertools import product
from time import time
import os
import sys

amino_acids = 'ACDEFGHIKLMNPQRSTVWY'
max_sequence_length = 7 #CAREFUL, TOO MUCH (more than 7) WILL FILL UP HARD DRIVE
min_sequence_length = 4 #You can change these two numbers
save_filename = str(min_sequence_length) + '-' + str(max_sequence_length) + '_length_aminoacids.fasta'

start_time = time() #tracks time at start

print('\n')
print(amino_acids)
print(str(len(amino_acids)) + ' different Amino Acids possible \n')
print('Minimum sequence length is ' + str(min_sequence_length))
print('Maximum sequence length is ' + str(max_sequence_length) + '\n')
print('GENERATING SEQUENCES...')
print(20*'-')


expected_seq_num = 0
for i in range(min_sequence_length, max_sequence_length+1):
    expected_seq_num += 20**i #calculates expected number of sequences for all lengths of AAs


counter = 0 #for user interface purposes
with open(save_filename, 'a') as output_file:

    for length in range(min_sequence_length, max_sequence_length+1):
        for sequence in product(amino_acids, repeat=length): #cartesian product (permutation)
            sequence_string = ''.join(sequence) #tuple -> string
            output_file.write('>ps|'+ sequence_string + '\n' + sequence_string + '\n') #write sequence and header to file

            if counter % 1000000 == 0: #for user interface purposes
                sys.stdout.write('\r')
                sys.stdout.write(sequence_string)
                sys.stdout.write(' | percent done: ' + str(round(((counter / expected_seq_num) * 100), 2)) + '%')

                sys.stdout.flush()
            counter += 1


print(20*'-')
print('\nDone! Took ' + str(round(time() - start_time, 2)) + ' seconds. \n')

print('Number of sequences should be: ' + str(expected_seq_num))
print('Actual number of sequences: ' + str(counter))

if expected_seq_num == counter:
    print('No errors detected')
elif expected_seq_num != counter:
    print('Error, number of sequences in file does not match expected (missing some or overwrote old file?)')

print(' \nFile size: ' + str(os.stat(save_filename).st_size) + ' bytes')
print('Saved as: ' + save_filename)


