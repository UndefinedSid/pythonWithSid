start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

if start > end:
    start, end = end, start

prime_sum = 0

for num in range(start, end + 1):
    if num < 2:
        continue

    is_prime = True

    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            is_prime = False
            break

    if is_prime:
        prime_sum += num

print("Sum of prime numbers in the range:", prime_sum)
