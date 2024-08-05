# 나무의 수 N, 가져가려는 나무의 길이 M, 절단기 길이 H
# ex) H=15, 나무 : 20, 15, 10, 17 -> 5, 0, 0, 2 -> M=7
# 이진분류 문제로 해결

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

# 시간초과
# def cut(H):
#     return sum(max(0, tree - H) for tree in trees) >= M

# left, right, result = 0, max(trees), 0
# while left <= right:
#     mid = (left + right) // 2
#     if cut(mid):
#         result, left = mid, mid + 1
#     else:
#         right = mid - 1

# print(result)

def cut(H):
    total = 0
    for tree in trees:
        if tree > H:
            total += tree - H
        if total >= M:
            return True
    return total >= M

left, right = 0, max(trees)
result = 0
while left <= right:
    mid = (left + right) // 2
    if cut(mid):
        result = mid
        left = mid + 1
    else:
        right = mid - 1
print(result)