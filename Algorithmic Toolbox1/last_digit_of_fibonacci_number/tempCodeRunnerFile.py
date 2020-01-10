def fib_last_digit(n):
    if (n <= 1):
        return n
    numbers = [0, 1] 
    for i in range (2, n+1):
        numbers.append(numbers[i-1] + numbers[i-2])
    return numbers[n] % 10


print(fib_last_digit(613455))