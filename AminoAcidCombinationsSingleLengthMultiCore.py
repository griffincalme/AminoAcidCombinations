from itertools import product
from time import time
from multiprocessing import Process

amino_acids = 'ACDEFGHIKLMNPQRSTVWY'
amino_acids_invert = amino_acids[::-1]
sequence_length = 6 #CAREFUL, TOO MUCH (more than 7) WILL FILL UP HARD DRIVE

print(amino_acids)
print(str(len(amino_acids)) + ' different Amino Acids possible \n')

start_time = time() #tracks time at start



def first_half():
    counter = 0
    with open('all_amino_acid_sequences.txt', 'a') as output_file:

        for sequence in product(amino_acids, repeat=sequence_length): #cartesian product (permutation)
            sequence_string = ''.join(sequence) #tuple -> string
            output_file.write(sequence_string + '\n') #write sequence to file

            if counter % 1000123 == 0: #for user interface purposes
                print(sequence_string)
                print('percent done: ' + str(round(counter/(20**sequence_length)*100*2, 2)) + '%')
                print('...')

            if counter == ((20**sequence_length)/2)-1:
                print('Done! Took ' + str(round(time() - start_time, 2)) + ' seconds.')
                return
            counter += 1

def second_half():
    counter = 0
    with open('all_amino_acid_sequences.txt', 'a') as output_file:

        for sequence in product(amino_acids_invert, repeat=sequence_length): #cartesian product (permutation)
            sequence_string = ''.join(sequence) #tuple -> string
            output_file.write(sequence_string + '\n') #write sequence to file

            #if counter % 1000123 == 0: #for user interface purposes
            #   print(sequence_string)
            #   print('percent done: ' + str(round(counter/(20**sequence_length)*100, 2)) + '%')
            #   print('...')

            if counter == ((20**sequence_length)/2)-1:
                return
            counter += 1



if __name__=='__main__':
     p1 = Process(target=first_half)
     p1.start()
     p2 = Process(target=second_half)
     p2.start()


#dual core only marginally (30%) better than single thread?