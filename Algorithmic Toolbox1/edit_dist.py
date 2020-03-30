def edit_dist(A, B):
    length = max(len(A), len(B))
    col, row = length, length
    D = [[0 for i in range(col)] for j in range(row)]
    for j in range(0,len(B)):
        for i in range(0,len(A)):
            print(i,j)
            if j and i == 0:
                D[i][j] = j
            elif i and j==0:
                D[i][j] = i 
            else:
                insertion = D[i][j-1] +1
                deletion = D[i-1][j] + 1
                match    = D[i-1][j-1]
                mismatch  = D[i-1][j-1] + 1 
                if A[i] == B[j]:
                    D[i][j] = min(insertion,deletion,match)
                else:
                    D[i][j] = min(insertion,deletion,mismatch)
                print(D)
    return(D[len(A)-1][len(B)-1])

print(edit_dist("distance", "editing"))


