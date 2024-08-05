import sys
r = range;input = sys.stdin.readline

N, M = map(int, input().split())
N_lst = list(map(int, input().split()))

# 시간초과
# for _ in r(M):
#     i, j = map(int, input().split())
#     output = N_lst[i-1:j]
#     result = sum(output)
#     print(result)

lst = [0] * (N + 1)
for i in r(1, N + 1):
    lst[i] = lst[i - 1] + N_lst[i - 1]

for _ in r(M):
    i, j = map(int, input().split())
    print(lst[j] - lst[i - 1])