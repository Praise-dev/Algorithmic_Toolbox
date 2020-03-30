import math
def dp_change(money, coins):
    min_coins = dict([(0,0)])
    for m in range(1, money+1):
        min_coins[m] = math.inf
        for i in coins:
            if m >= i:
                num_coins = min_coins[m-i] + 1
                if num_coins< min_coins[m]:
                    min_coins[m] = num_coins
    return min_coins[money]

print(dp_change(34,[1,3,4]))