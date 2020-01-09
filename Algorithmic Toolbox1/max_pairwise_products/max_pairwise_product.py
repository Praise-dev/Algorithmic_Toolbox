# python3

# from random import randint


# def max_pairwise_product(numbers):
#     n = len(numbers)
#     max_product = 0
#     for first in range(n):
#         for second in range(first + 1, n):
#             max_product = max(max_product,
#                 numbers[first] * numbers[second])
#     # print(max_product)
#     return max_product



def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    first_max = 0
    second_max = 0

    if len(numbers) == 1:
        max_product = numbers[0]
    
    else:
        for price in range(n):
            if numbers[price] > first_max :
                first_max = numbers[price]

        for price in range(n):
            if (numbers[price] > second_max) and (price != numbers.index(first_max)):
                second_max = numbers[price]
    
    max_product = first_max * second_max
    # print(max_product)
    return max_product

# while(True):
#     n = randint(0, 11)#5
#     print(n)
#     i =0
#     numbers = []
#     res_one = max_pairwise_product(numbers)
#     res_two = max_pairwise_product_fast(numbers)
#     # print(number)
#     while (i < n):
#         numbers.append(randint(0, 100000))
#         i+=1
#     print(numbers)
#     if res_one != res_two:
#         print(res_one + " " + res_two)
#         break
#     else:
#         print("OK")





if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
