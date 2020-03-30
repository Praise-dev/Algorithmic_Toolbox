def prim_calc(n):
    num_operations = dict([(1,0)])
    seq = []
    if n == 1:
        return num_operations[n]
    for i in range(2, n+1):
        if i%3 ==0:
                num_operations[i] = min(num_operations[i//3] + 1, num_operations[i-1]+1)
        elif i%2 ==0:
                num_operations[i] = min(num_operations[i//2] + 1, num_operations[i-1] + 1)
        else:
            num_operations[i] = num_operations[i-1] + 1
    min_operations = num_operations[n]

    
    while n > 1:
        seq.append(n)
        if n%3 ==0 and num_operations[n//3] == num_operations[n]-1:
            n = n//3
        elif n%2 ==0 and num_operations[n//2] == num_operations[n] -1:
            n = n//2
        elif num_operations[n-1] == num_operations[n] - 1:
            n-= 1
    seq.append(1)
    seq = seq[::-1]
    return min_operations, seq


