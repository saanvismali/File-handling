# open the file in read mode 
file_read = open("Codingal.txt", "r")
print(file_read.read())
file_read.close()

# open the file in write mode
file_write = open("Codingal.txt", "w")

# write in the file 
file_write.write("File in write mode ...")
file_write.write("Hi! I'm being written to a file.")
file_write.close()

# open the file in append mode
file_append = open("Codingal.txt", "a")
# append in the file
file_append.write("This line is appended to the file.")
file_append.write("Hi! I'm being written to a file.")
file_append.close()
