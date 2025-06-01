try:
    file1=open('sample.txt','r')
    print('Reading file contents:')
    count=1
    for i in file1.readlines():
        print('Line',count,': ',i)
        count+=1
    file1.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")