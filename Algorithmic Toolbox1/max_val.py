import math
def max_val(D):
    sign = []
    digits = []
    for i in range(len(D)):
        if i%2 != 0:
            sign.append((D[i]))
        else:
            digits.append(int(D[i]))
    n  = len(digits)
    print(sign,digits)
    m, M = [[0 for i in range(n)] for j in range(n)], [[0 for i in range(n)] for j in range(n)]
    
    for i in range(n):
        m[i][i], M[i][i] = digits[i], digits[i]


    for s in range(1,n):
        for i in range(n-s):
            j = i+s
            print(i,j)
            m[i][j],M[i][j] = min_max(i,j,m,M,sign)
    return M[0][n-1]


def min_max(i,j,m,M,sign):
    minimum = math.inf
    maximum = -math.inf
    for k in range(i,j):
        a = operation(i,j,M,M,k,sign) 
        b=   operation(i,j,M,m,k,sign) 
        c=  operation(i,j,m,M,k,sign) 
        d=  operation(i,j,m,m,k,sign) 
        minimum = min(minimum,a,b,c,d)
        maximum = max(maximum,a,b,c,d)
    return minimum,maximum

def operation(i,j,t1,t2,k,sign):
    if sign[k] == "-":
        return t1[i][k]-t2[k+1][j]
    if sign[k] == "+":
        return t1[i][k]+t2[k+1][j]
    if sign[k] == "*":
        return t1[i][k]*t2[k+1][j]
            
