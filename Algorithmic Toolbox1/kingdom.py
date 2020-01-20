def kingdom(n, king_A, king_B, k):
    names = [king_A, king_B]
    i = 1
    while i <n:
        new_name = names[i-1] + (names[i]*2)
        names.append(new_name)
        i+= 1
    
    new_kingdom = names[n-1]
    
    if (new_kingdom[k-1]):
        return new_kingdom[k-1]
    else:
        return -1



