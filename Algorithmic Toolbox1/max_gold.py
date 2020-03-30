def max_gold(W,G):
    row,col = len(G)+1, W+1
    weight  = [[0 for i in range(col)] for j in range(row)]

    for w in range(row):
        for j in range(col):
            if j and w==0 or j==0 and w==0:
                weight[w][j] = 0
            if w and j==0 or w==0 and j==0:
                weight[w][j] = 0
    
    
    for i in range(1,row):
        for j in range(1,col):
            weight[i][j] = weight[i-1][j]
            if G[i-1] <= j:
                w = weight[i-1][j-G[i-1]] + G[i-1]
                if w > weight[i][j]:
                    weight[i][j]= w
        print(weight)
    return weight[row-1][W]

print (max_gold(9,[1,4,8]))