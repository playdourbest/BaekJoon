# N개 주어짐
# x먼저 비교하고 그다음 y 비교해야함 -> tuple 사용해야함
N=int(input());r=range
points=[tuple(map(int, input().split())) for _ in r(N)]
for x, y in sorted(points):
    print(x,y)