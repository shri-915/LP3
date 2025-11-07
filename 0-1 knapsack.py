def knapSack(W, wt, val, n):
    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            if wt[i-1] <= w:
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][W]

n = int(input("Enter number of items: "))
wt = [int(input(f"Weight {i+1}: ")) for i in range(n)]
val = [int(input(f"Value {i+1}: ")) for i in range(n)]
W = int(input("Enter capacity of knapsack: "))
print("Maximum Profit:", knapSack(W, wt, val, n))