# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_A&lang=jp


if __name__ == '__main__':
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    dp = [float('inf') for _ in range(n+1)]
    dp[0] = 0
    for i in range(n+1):
        for j in range(m):
            if i - c[j] >= 0:
                dp[i] = min(dp[i-c[j]]+1, dp[i])

print(dp[n])
