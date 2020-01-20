# python3
import sys

def min_stops(d, l, arr):
    current_refill = 0
    number_of_refills = 0
    # arr.append(d)
    n = len(arr)
    # print(arr)

    while current_refill <= n:
        last_refill = current_refill
        while (current_refill <= n ) and (arr[current_refill+1]- arr[last_refill] <= l):
            current_refill += 1
        if current_refill == last_refill:
            return -1
        if current_refill <= n:
            number_of_refills += 1
    
    return number_of_refills

print(min_stops(950,400,[200,375,550,750]))
    
# def compute_min_refills(distance, tank, stops):
#     # write your code here
#     return -1

# if __name__ == '__main__':
#     d, m, _, *stops = map(int, sys.stdin.read().split())
#     print(compute_min_refills(d, m, stops))

