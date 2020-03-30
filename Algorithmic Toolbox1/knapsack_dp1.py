def knapsack_dp1(W, V, weight):
    n = len(V)
    value = [0 for i in range(weight+1)]
    for w in range(1,weight+1):
        value[w] = 0
        for i in range(n):
            if W[i] <= w:
                val = value[w-W[i]]+ V[i]
                if val > value[w]:
                    value[w] = val
    return value[weight]
        