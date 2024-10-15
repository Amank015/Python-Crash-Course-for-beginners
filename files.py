# Open a file
myFile = open('myfile.txt','w')

# Get some info
print('Name:',myFile.name)
print('Is Closed:',myFile.closed)
print('Opening Mode:',myFile.mode)

# Write a file 
myFile.write('I like to work with python')
myFile.write('And also like to work with JavaScript')
myFile.close()

# Append to file
myFile = open('myfile.txt','w')
myFile.write('I also like Core Java')
myFile.close()

# Read a file
myFile = open('myfile.txt','r+')
text = myFile.read(100)
print(text)