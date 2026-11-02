def minimum_coins(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount:
                dp[current_amount] = min(
                    dp[current_amount],
                    dp[current_amount - coin] + 1
                )

    if dp[amount] == float("inf"):
        return -1

    return dp[amount]


print(minimum_coins([1, 2, 5], 11))
print(minimum_coins([1, 3, 4], 6))   
print(minimum_coins([2], 3))         