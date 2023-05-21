file = input('Enter your file name: ')
fileName = file
name = input('Enter your name: ')
n = name + ', '
street = input('Enter your street address: ')
s = street + ', '
phone = input('Enter your phone number: ')
p = phone + ','

# to append the file change 'w' to 'a'
with open(fileName, 'w') as fileHandle :
  fileHandle.write(n)
  fileHandle.write(s)
  fileHandle.write(p)

with open(fileName, 'r') as filehandle :
  data = filehandle.read()
print(data.rstrip())
