# Uses python3
import sys

def get_change(m):
    #write your code here
    #1, 5, 10
    coins = [1, 10, 5]
    change = 0
    while(coins):
        change += m // max(coins)
        if m % max(coins):
            m = m % max(coins)
            coins.pop(coins.index(max(coins)))
        else: return change 
    return change

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))


