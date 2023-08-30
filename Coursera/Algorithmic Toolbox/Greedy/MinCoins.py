def min_coins_greedy(amount):
    coins = [1,5,10]
    coins.sort(reverse=True)  # Sort coins in descending order
    coin_count = 0

    for coin in coins:
        while amount >= coin:
            amount -= coin
            coin_count += 1

    return coin_count

if __name__ == '__main__':
    N = list(map(int, input().split()))[0]
    print(min_coins_greedy(N))