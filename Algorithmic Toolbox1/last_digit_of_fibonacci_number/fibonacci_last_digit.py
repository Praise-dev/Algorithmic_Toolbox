# Uses python3
import sys

# from random import randint

# def get_fibonacci_last_digit_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current
#     # print(current % 10)
#     return current % 10
def fib_last_digit(n):
    if (n <= 1):
        return n
    numbers = [0, 1] 
    for i in range (2, n+1):
        numbers.append((numbers[i-1] + numbers[i-2])%10)
    return numbers[n]

# print(fib_last_digit(12))


    



# while (True): 
#     i = randint(1, 200) 
#     efficient = fib_last_digit(i)
#     naive = get_fibonacci_last_digit_naive(i)
#     if ( efficient != naive ):
#         print(f"efficient : {efficient}, naive : {naive}")
#         break
#     else:
#         print(f"efficient : {efficient}, naive : {naive}")
#         print("OK")


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fib_last_digit(n))
