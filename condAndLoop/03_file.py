#file content of 03_file.py upto print(username)
import time
print("learn iter topic")
username="Sid"
print(username)

#-------------------------------------

# iter() and next() function in python


f=open('03_file.py')    # opens file and take reference as f
f.readline()
# O/p-> 'import time\n'
f.readline()
# O/p -> 'print("learn iter topic")\n'
f.readline()
#.   'username="Sid"\n'
f.readline()
#   'print(username)'
f.readline()
#   ''    b/c  file doesnot contain anything afterwards

f.__next__()
# O/p-> 'import time\n'
f.__next__()
# O/p -> 'print("learn iter topic")\n'
f.__next__()
#.   'username="Sid"\n'
f.__next__()
#   'print(username)'
f.__next__()
# O/p-->> StopIteration

for line in open('03_file.py'):   # iterating through file line by line
    print(line)
# O/p-->
#import time
#print("learn iter topic")
#username="Sid"
#print(username)

for line in open('03_file.py'):
    print(line,end='')  # to avoid double new line we use end=''

# O/p-->
#import time
#print("learn iter topic")
#username="Sid"
#print(username)

while True:
    line=f.readline()
    if not line:
        break
    print(line,end='')

# O/p-->
#import time
#print("learn iter topic")
#username="Sid"
#print(username)

iter(f) is f   # checking whether file object is its own iterator
# O/p-> True
iter(f) is f.__iter__()  # checking whether file object is its own iterator using __iter__()
# O/p-> True


test="siddharth"
if not test:
    print("string is empty")

# O/p--> (no output b/c string is not empty)

test=""
if not test:
    print("string is empty")
# O/p--> string is empty

mylist=[1,3,5,7]
it=iter(mylist)   # creating iterator object from list

it
# O/p-> <list_iterator object at 0x104f4d250>

it.__next__()
# O/p-> 1
it.__next__()
# O/p-> 3
it.__next__()
# O/p-> 5
it.__next__()
# O/p-> 7
it.__next__()
# O/p-> StopIteration

iter(mylist) is mylist   # checking whether list object is its own iterator
# O/p-> False
iter(mylist) is mylist.__iter__()  # checking whether list object is its own iterator using __iter__()
# O/p-> True

range(5)  # creating range object
# O/p-> range(0, 5)
it=iter(range(3))  # creating iterator object from range
it
# O/p-> range_iterator object at 0x104f4d310>
it.__next__()
# O/p-> 0
next(it)
# O/p-> 1
next(it)
# O/p-> 2
it.__next__()
# O/p-> 3
it.__next__()
# O/p-> StopIteration

iter(range(5)) is range(5)   # checking whether range object is its own iterator
# O/p-> False

dic={'a':1,'b':2,'c':3}  # creating dictionary object
for key in dic.keys():
    print(key)
# O/p-->
# a
# b
# c

it=iter(dic)   # creating iterator object from dictionary
it
# O/p-> <dict_keyiterator object at 0x104f4d490>
it.__next__()
# O/p-> 'a'
next(it)
# O/p-> 'b'
next(it)
# O/p-> 'c'
it.__next__()
# O/p-> StopIteration

