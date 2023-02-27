import os
import sys

filename = input("Output file name: ")
name = input("Image name : ")
extention = input("Image Extention : ")
start = int(input("Start : "))
end = int(input("End : "))
print('\nCreating file...')

original_stdout = sys.stdout # Save a reference to the original standard output

with open('file.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print('--atlas -f rgba8888 -z auto')
    for i in range(end - start + 1):
        print(name+str(i+start)+"."+extention)
    sys.stdout = original_stdout # Reset the standard output to its original value

os.rename("file.txt",filename)
input("Terminée : " + str(start) + " - " + str(end) + "\nFile created at : " + os.path.abspath("."))
