# 2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수
# <경우의 수>
# 2×0 직사각형은 1가지 방법 (아무것도 없음)
# 2×1 직사각형은 1가지 방법 (1×2 타일 하나)

import sys
input = sys.stdin.readline

def baekjoon_11727(n):
    num = 10007 # 문제에서 주어진 수
    dp = [0] * (n + 1)

    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 2]) % num
    
    return dp[n]

n = int(input())
print(baekjoon_11727(n))