# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수

# <경우의 수>
# 1. 마지막 타일이 2x1 인 경우
# 세로 길이가 2 이기 때문에 무조건 1개만 채워짐 -> 2 x (n-1) 만큼 더 채워야함
# 2. 마지막 타일이 1x2 인 경우
# 세로 길이가 1 이기 때문에 무조건 2개가 채워져야됨 -> 2 x (n-2) 만큼 더 채워야함

# dp[N] = 2xN
# dp[1] = 1
# dp[2] = 2 (1×2 두개 또는 2×1 두개)
# dp[n] = dp[n-1] + dp[n-2]

# <input>
# N=세로 길이
# <output>
# dp[n]%10007

import sys
r=range;input=sys.stdin.readline

def baekjoon_11726(n):
    if n==1:
        return 1
    if n==2:
        return 2
    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=2
    for i in r(3,n+1):
        dp[i]=(dp[i-1]+dp[i-2])%10007
    return dp[n]
    
n=int(input())
print(baekjoon_11726(n))