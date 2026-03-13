# 17626 Four Squares
# dp[i] = i를 만들기 위한 제곱수 개수의 최소값

n = int(input().strip())

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = i
    j = 1
    while j * j <= i:
        val = dp[i - j * j] + 1
        if val < dp[i]:
            dp[i] = val
        j += 1

print(dp[n])
