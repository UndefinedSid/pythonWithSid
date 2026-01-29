x=('sid','manoj','dev','ashok','soumo')
y=enumerate(x)
print(y)    #  o/p-> <enumerate object at 0x1026c9670>
z=list(y)
print(z)    # got o/p in key,value pair 
            #[(0, 'sid'), (1, 'manoj'), (2, 'dev'), (3, 'ashok'), (4, 'soumo')]

files=open('trial.txt','w') 
# opens any files in 'w' (write mode) if existing otherwise automatically creates a new file 

try:
    files.write('to write something in file')
finally:
    files.close()   # we have to close the file

# python preferred 

with open('trial.txt','w') as fileName:
    fileName.write('python preferred writing') 
# file opens and stored in fileName variable and also closes the file by self


