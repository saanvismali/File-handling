# Program to count number of lines in this file 
# opening a file 
file = open("Codingal.txt", "r")
Counter = 0


# Reading from file 
Content = file.read()   
# Splitting content into lines
#And storing them in a list 
Colist = Content.split("\n")

for i in Colist:
    if i:
        Counter += 1


print("This is the number of lines in the file")
print(Counter)  