#open the previous file created
#f = open("Myfile.txt", "r") 

#print(f.read()) #read mode to view the contents of the file on the console

#print(f.readline(43)) #read single line using readline

#for x in f:     #using for loops
    #print(x)

#removing the file from path
import os
if os.path.exists("Myfile.txt"):
    os.remove("Myfile.txt")
else:
    print("The File does not exist")