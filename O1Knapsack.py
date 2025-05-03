"""
  DP bottom up approach.
  Construct a dp array where the rows are the items and the columns are different capacities up to and including the max capacity.
  Return max for the capacity given after dp array has been populated accordingly from capacity 1 to max capacity.
  Detailed video solution can be found here: https://www.youtube.com/watch?v=cJ21moQpofY&t.
  O(N * C) time O(N * C) space.
  """

weights = [1, 2, 3]
values = [10, 20, 30]

def knapsack(w, v, capacity):
    dp = [[0 for i in range(capacity + 1)] for j in range(len(w) + 1)]
    # Populating dp array
    for i in range(1, len(w) + 1):
        for j in range(1, capacity + 1):
            wt = w[i - 1]
            val = v[i - 1]
            if wt <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wt] + val)
    # Finding all items we chose
    chose = []
    i = len(w)
    j = capacity
    while i >= 1:
        if dp[i][j] != dp[i - 1][j]:
            chose.append(i)
            j -= w[i - 1]
        i -= 1
    print(chose[::-1])
    # Printing Dp Array
    for i in dp:
        print(i)
    # Return max
    return dp[-1][-1]
print(knapsack(weights, values, 6))
