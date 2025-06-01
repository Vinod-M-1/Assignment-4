In=input('Enter text to write to the file : ')

file1=open('Output.txt','w')
file1.write(In)
file1.write('\n')
print('Data successfully written to output.txt.\n')
file1.close()

Ain=input('Enter additional text to append: ')
file1=open('Output.txt','a')
file1.write(Ain)
print('Data successfully appended.\n')
file1.close()

print('Final content of output.txt: ')
file1=open('Output.txt','r')
a=file1.read()
print(a)
file1.close()