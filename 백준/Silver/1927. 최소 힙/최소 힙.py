import sys
import heapq
input = sys.stdin.readline

N = int(input())
min_heap, result = [], []

for i in range(1, N + 1):
    x = int(input())
    if x == 0:
        if min_heap:
            result.append(heapq.heappop(min_heap))
        else:
            result.append(0)
    else:
        heapq.heappush(min_heap, x)

# print(result)
for results in result:
    print(results)
