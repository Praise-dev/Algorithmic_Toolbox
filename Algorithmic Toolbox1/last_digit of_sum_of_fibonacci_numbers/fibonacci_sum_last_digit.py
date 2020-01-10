# Uses python3
import sys

# def fibonacci_sum_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1
#     sum      = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current
#     print (sum % 10)
#     return sum % 10


def fib_sum_last_digit(n):
    if (n <= 1):
        return n
    numbers = [1, 0] 
    sums = 1
    for i in range (2, n+1):
        numbers.append(numbers[i-1] + numbers[i-2])
        sums += numbers[i-1] + numbers[i-2]
    return sums % 10 




if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fib_sum_last_digit(n))
