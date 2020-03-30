import sys
from random import randrange
def quick_sort(A,l,r):
    # base case
    if l>= r:
        return
    k = randrange(l,r)
    A[l], A[k] = A[k], A[l]
    m1, m2 = partition(A,l,r)
    quick_sort(A,l, m1-1)
    quick_sort(A,m2 +1, r)
    return A

def partition(A, l, r):
    x = A[l]
    j = l
    k = j
    for i in range(l+1, r+1):
        if A[i] < x:
            j += 1
            k+=1
            A[k], A[i] = A[i], A[k]
            A[k], A[j] = A[j], A[k] 
        elif A[i] == x:
            k+=1
            A[k], A[i] = A[i], A[k]
    # swapping x and A[j]
    A[j], A[l] = A[l], A[j]
    return j,k


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')