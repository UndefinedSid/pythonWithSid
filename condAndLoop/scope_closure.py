x=87

def f1():
    x=24
    def f2():
        print(x)
    f2()
f1()

# 0/p--> 24

def change():
    global x
    x=38

change()
print(x) #o/p-> 38 due to global keyword

def f1():
    x=25
    def f2():
        print(x)
    return f2
myAns=f1()
myAns() # o/p -> 25 due to closure

# A closure is a function that Remembers variables from its enclosing scope
# Even after the outer function has finished executing and 
# Inner functions keep a reference, not a copy, of outer variables

def power(n):
    def cal(x):
        return x ** n # n is remembered from the outer scope due to closure
    return cal # returns the inner function cal

square=power(2) #returns cal function with n=2
cube=power(3)   #returns cal function with n=3

print(square(5)) #o/p-> 25
print(cube(7)) # o/p-> 343


