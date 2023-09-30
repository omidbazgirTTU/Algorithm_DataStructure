def edit_distance(str1, str2):
    len1, len2 = len(str1), len(str2)

    # Create a 2D table to store the edit distances
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # Initialize the table with base cases
    for i in range(len1 + 1):
        dp[i][0] = i
    for j in range(len2 + 1):
        dp[0][j] = j

    # Fill in the table using dynamic programming
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],      # Deletion
                                   dp[i][j - 1],      # Insertion
                                   dp[i - 1][j - 1])  # Substitution

    # The bottom-right cell contains the minimum edit distance
    return dp[len1][len2]


if __name__ == '__main__':
    string_1 = list(input())
    string_2 = list(input())
    print(edit_distance(string_1, string_2))