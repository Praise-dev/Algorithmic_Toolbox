def knapsack_dp2(W,V,weight):
    row,col = len(W)+1, weight+1
    value = [[0 for x in range(col)] for y in range(row)]
    optimal = []
    for j in range(row):
        for w in range(col):
            if j and w==0 or j==0 and w==0:
                value[j][w] = 0
            if w and j==0 or w==0 and j==0:
                value[j][w] = 0

    for i in range(1, row):
        for w in range(1, col):
            value[i][w] = value[i-1][w]
            if W[i-1] <= w:
                val = value[i-1][w-W[i-1]] + V[i-1]
                if value[i][w] < val:
                    value[i][w] = val
    soln = value[row-1][col-1]
    
    a,b = row-1,col-1
    for i in range(1, row):
        option= max(value[a-1][b-W[i-1]] + V[i-1], value[a-1][b])
        if value[a][b] > option:
            optimal.append(1)
            a = a-1 
            b = b- W[a-1]
        else:
            optimal.append(0)
            a= a-1
    
    return soln, optimal[::-1]


print(knapsack_dp2([6,3,4,2],[30,14,16,9],10))