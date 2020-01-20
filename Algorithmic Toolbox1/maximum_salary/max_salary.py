#Uses python3

import sys

#  def largest_number(a):
#     #write your code here
#     res = ""
#     for x in a:
#         res += x
#     return res

def max_salary(digits):
    salary= ""
    max_digit = 0
    while(digits):
        max_digit = max(digits)
        salary += str(max_digit)
        digits.remove(max_digit)    
    return salary  

def is_greater_or_equal(nums):
    #[21 2], [23, 3], [23, 39, 92]
    for i in len(nums):
        if len(nums[i]) > 1 :
            if(nums[i])
            items.split()
    return
 

print(max_salary([2,3, 9,3]))    

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = input.split()
#     a = data[1:]
#     print(largest_number(a))

num =21
numstr = str(num)

print(numstr[1])