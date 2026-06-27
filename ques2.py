num = input("Enter a 5 digit number: ")

if not (num.isdigit() and len(num) == 5):
    raise ValueError("Input must be exactly a 5-digit number.")

print(num)

for i in range(1, len(num)):
    print(num[:i], ",", num[i:])

print(num)