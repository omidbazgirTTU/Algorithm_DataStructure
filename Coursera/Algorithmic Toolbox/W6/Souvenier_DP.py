
def can_partition_souvenirs(souvenirs):
    total_value = sum(souvenirs)
    
    # If the total value is not divisible by 3, it's impossible to partition
    if total_value % 3 != 0:
        return 0
    
    target_sum = total_value // 3
    n = len(souvenirs)
    
    # Create a 2D table to store whether it's possible to get a sum using a subset of souvenirs
    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]
    
    # Initialize the first column (using no souvenirs) as True
    for i in range(n + 1):
        dp[i][0] = True
    
    # Fill the table
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            # Exclude the current souvenir
            dp[i][j] = dp[i - 1][j]
            
            # Include the current souvenir if its value is less than or equal to j
            if souvenirs[i - 1] <= j:
                dp[i][j] = dp[i][j] or dp[i - 1][j - souvenirs[i - 1]]
    
    # The result is True if we can achieve a sum of target_sum three times
    if dp[n][target_sum]:
        return 1
    else:
        return 0

if __name__ == '__main__':
    #input = sys.stdin.read()
    n = list(map(int, input().split()))[0]
    A = list(map(int, input().split()))

    print(can_partition_souvenirs(A))