num=[1,2,3,4,6,-87,286,-343,8237]
posNum=0

for i in num:
    if i > 0:
        posNum += 1

print(posNum)

str="python"
rev_str=""

for char in str:
    rev_str= char + rev_str

print(rev_str) # output --> nohtyp 

rev_str=""

for char in str:
    if char=='h':
        continue
    rev_str= rev_str + char

print(rev_str) # O/p --> pyton

number=13
fact=1
#factorial calculation
while number > 0:
    fact=fact * number
    number -= 1

print(fact)


while True:
    val=int(input("enter value -> "))   
    # we take int() beacuse input is always come in string format to parse string to int

    if 1 <= val <= 100:
        print("valid number")
        break
    else:
        print("invalid number")


num=113
is_prime=True

if num > 1:
    for i in range(2,num):
        if(num % i)==0: # we should use () to avoid math error problem 
            is_prime=False
            break
    print(is_prime)


items=["windows","macOS","linux","unix","debian","macOS","WindowS"]
unique=set()

for prod in items:
    if prod in unique:
        print("found duplicate",prod)
        break
    unique.add(prod)

#found only macOS not WindowS due to change in windows & WindowS

import time
# exponential time wait for incorrect attempt
attempts=0
maxRetry=10
waitTime=1

while attempts < maxRetry:
    print("attempted",attempts + 1,"-> wait time",waitTime)
    time.sleep(waitTime)
    waitTime *= 2
    attempts += 1

