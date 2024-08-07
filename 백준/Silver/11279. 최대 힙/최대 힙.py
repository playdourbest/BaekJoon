import sys
import heapq

r=range;input=sys.stdin.readline
N = int(input())
heap, results = [], []
for i in r(1, N+1):
    x = int(input())
    if x == 0:
        results.append(-heapq.heappop(heap) if heap else 0)
    else:
        heapq.heappush(heap, -x)
#     if x > 0:
#         heapq.heappush(heap, -x)
#     else:
#         if heap:
#             results.append(-heapq.heappop(heap))
#         else:
#             results.append(0)
print('\n'.join(map(str, results)))