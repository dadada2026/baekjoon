# 11727 2×n 타일링 2
# DP로 경우의 수를 센다 (mod 10007)

n = int(input().strip())

if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 10007
    print(dp[n])
