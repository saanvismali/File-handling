# Open file and read its contents
file = open('Codingal.txt','r')
print(file.read())
file.close()

# Open file and read its begining 8 charecters
file = open('Codingal.txt','r')
print(file.read(8))
file.close()

# Append your name and age in the file 
file = open('Codingal.txt','a')
file.write("Hi! I am Penguin and I am 1 yr old.")
file.close()