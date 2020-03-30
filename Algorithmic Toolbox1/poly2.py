def recursive_change(money, coins):
    if money == 0:
        return 0 
    Min_num_coins = 0
    for i in range(len(coins)):
        if money >= coins[i]:
            num_coins = recursive_change(money-coins[i], coins)
            if num_coins+1 < Min_num_coins:
                Min_num_coins = num_coins+1
    return Min_num_coins


print(recursive_change(9, [1,5,6]))
