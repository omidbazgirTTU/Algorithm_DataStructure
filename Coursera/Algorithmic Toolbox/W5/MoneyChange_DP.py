def MoneyChangeDP(coins, amount):
    # Initialize a table to store minimum coin counts for each amount
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins are needed to make change for 0
    
    # Iterate through each coin denomination
    for coin in coins:
        # Update dp table for each amount from coin to the target amount
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    # If dp[amount] remains unchanged (still float('inf')), it's not possible to make change
    if dp[amount] == float('inf'):
        return -1
    else:
        return dp[amount]


if __name__ == '__main__':
    Money = list(map(int, input().split()))[0]
    Coins = [1,3,4]
    result = MoneyChangeDP(Coins, Money)
    print(result)