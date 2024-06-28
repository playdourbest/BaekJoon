# 오름차순정렬

# 메모리초과
import sys
r=range;input=sys.stdin.readline
# lst=[int(input()) for _ in r(int(input()))]
# sort_lst=sorted(lst)
# print(*(j for j in sort_lst), sep='\n')

# 해결하기 위해 append 사용X
lst=[0]*10001
for _ in r(int(input())):
    lst[int(input())] += 1
for i in r(10001):
    if lst[i] != 0:
        for j in r(lst[i]):
            print(i)