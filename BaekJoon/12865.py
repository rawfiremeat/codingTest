n, k = map(int, input().split())
cases = [[0,0]] + [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        w = cases[i][0]
        h = cases[i][1]
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(h + dp[i-1][j - w],dp[i - 1][j])

print(dp[n][k])