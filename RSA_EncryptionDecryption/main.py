import rsa
import os

def ascii_to_hw2(asc):
    if chr(asc) == ' ': asc = 28 #space handling
    else: asc -= 63
    return asc

def hw2_to_ascii(hw2):
    hw2 += 63
    if hw2 == 91: hw2 = 32 #space handling
    return hw2
    

f_raw = input("Input filename. (must be in same directory as script): ")

user_input = input("Would you like to [e]ncrypt the file or [d]ecrypt the file? (e/d): ")

e = int(input("Input first term of public key (e): "))
n = int(input("Input second term of public key (n): "))

M_raw = [] #list of ascii values of file
M_processed = []#adjusted ascii values

f_processed = open(input("Input filename to write to. (will be created in same directory as script): "),'x')

if user_input == 'e': #ENCRYPTION
    #convert file to input
    for line in open(f_raw):
        for char in line: M_raw.append(ascii_to_hw2(ord(char.upper()))) #append the ascii code for every character of text. 
    
    #write input
    for x in M_raw: M_processed.append(rsa.encrypt(x,(e,n))) 
    for char in M_processed: f_processed.write(str(char) + "\n") #write to the new file all of the numerical values of every value on each line
else: #DECRYPTION
    #convert file to input
    for line in open(f_raw): M_raw.append(int(line)) #append the ascii code for every line. since each line is a numerical value 

    #bruteforce d
    d = rsa.find_d((e,n),100) #bruteforce d. we will use a limit of 100.
    print('d was determined to be: ' + str(d))

    #take input and decrypt
    for x in M_raw: M_processed.append(rsa.decrypt(x,(d,n)))
    for value in M_processed:
        try:
            f_processed.write(chr(hw2_to_ascii(value))) #write to the new file the ord conversions
        except:
            f_processed.write(" ")
f_processed.close()
print('Output saved.')