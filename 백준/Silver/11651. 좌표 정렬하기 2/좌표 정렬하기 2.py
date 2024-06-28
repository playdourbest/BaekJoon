# N개 주어짐
# y먼저 비교하고 그다음 x 비교해야함 -> tuple 사용해야함
import sys
r=range;input=sys.stdin.readline
points=[tuple(map(int, input().split())) for _ in r(int(input()))]
for x, y in sorted(points,key=lambda x : (x[1],x[0])):
    print(x,y)