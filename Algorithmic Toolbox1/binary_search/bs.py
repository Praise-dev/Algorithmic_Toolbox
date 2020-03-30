import sys

def binary_search(a, x):
    left, right = 0, len(a)-1
    index = bs(a, x, left, right)
    return index

def bs(a, k, start, end):
    # base case
    if start > end:
        return -1
    # recursive case
    m = start + ((end-start)//2)
    if a[m] == k:
        return m
    
    if a[m] < k: 
        return bs(a, k, m+1, end)

    if a[m] > k:
        return bs(a, k, start, m-1)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')

