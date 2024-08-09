import sys
import heapq
r=range;input=sys.stdin.readline

lst, output = [], []

for i in r(1, int(input())+1):
    x = int(input())
    if x != 0:
        heapq.heappush(lst, (abs(x), x))
    else:
        if lst:
            output.append(heapq.heappop(lst)[1])
        else:
            output.append(0)
print("\n".join(map(str, output)))