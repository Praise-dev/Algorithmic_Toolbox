
def pasc_tri(row,col):
    if row == 0:
        return 0

    if col == 1:
        return 1
    return pasc_tri(row-1, col-1) + pasc_tri(row-1,col) 

    

print(pasc_tri(3,1))




#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1