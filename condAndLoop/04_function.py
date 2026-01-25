def multi(num1,num2):
    print(num1 * num2) 

val=multi(24,4) # O/p--> none , it doesnot return anything due to print statement inside function val 
print(multi(72,5)) # it will print output

def multi(num1,num2):
    return num1 * num2

print(val) # prints return value

val=multi('sid',3) # handle string multiplication automatically
print(val)
val=multi(3,'sid')
print(val)  # O/p-->
# sidsidsid

def parameterHandling(para): # function with single parameter
    return ("given para is :" + para)

print(parameterHandling("sid"))

def parameterHandling(): # function with no parameter
    return ("doesnot given any para :")

 #print(parameterHandling("sid"))  # O/p-> TypeError b/c function expects no argument

def parameterHandling(para="default para"): # function with default parameter if no argument is passed otherwise use passed argument
    return f"given para is : {para}" # another recommended method

print(parameterHandling())
print(parameterHandling("non default"))

def cube(num): # can have multiple lines of code,multiple parameters and return statement
    return num ** 3

print(cube(6))

cube=lambda val : val ** 3; # accpet single parameter only,also single experession and doesnot need return statement

print(cube(5))

nums = [1, 2, 3, 4]
cubes = list(map(lambda x: x**3, nums)) #use lambda  inside map function
print(cubes)
# O/p --> 1,8,27,64

def argsHandler(*args): # always need (*args) recommended and *args used to accept multiple inputs i.e. array,lists
    return sum(args) # sum is a by default method

print(argsHandler(1,3,5))

def argsHandler(*sid): # always need (*args) recommended but can pass anything with * 
    return sum(sid)

def withoutArgs(*args): # alternative method without *args
    print(args) # o/p (1, 7, 8, 9) in tuple form 
    sum=0
    for i in args:
        sum += i
    return sum

print(withoutArgs(1,7,8,9)) 

def kwargsHandler(**kwargs):    # always need (**kwargs) recommended and **kwargs used to accept multiple key value pairs i.e. dictionary
    for key,value in kwargs.items():    # items() is a by default method to get key value pairs
        print(f"{key}:{value}") # f string method

kwargsHandler(name="Sid", course="MCA") #doesnot accept normal arguments only key value pairs 

# yield statement in python function 
# generating even numbers upto limit
def yieldHandler(limit):
    for i in range(2,limit+1,2): #range(start,stop,step)
        return i
    
    
print(yieldHandler(20)) # O/p--> 2 b/c return statement exits the function after first iteration

for num in yieldHandler(20):
    print(num) # O/p--> TypeError b/c return statement returns single value not iterable object


def yieldHandler2(limit):
    li=[]
    for i in range(2,limit + 1,2):
        li.append(i)
    return li

print(yieldHandler2(20)) # O/p--> [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#but we can use yield to make it more efficient because it will not store all values in memory

def yieldHandler3(limit):
    for i in range(2,limit + 1,2):
        yield i  # yield statement  

for num in yieldHandler3(20):
    print(num) # O/p--> 2 4 6 8 10 12 14 16 18 20 each in new line










