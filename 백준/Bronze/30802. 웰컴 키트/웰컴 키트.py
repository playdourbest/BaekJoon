import sys
input = sys.stdin.readline

def baekjoon_30802(N, sizes, T, P):
    S, M, L, XL, XXL, XXXL = sizes
    tshirt = 0
    for count in sizes:
        tshirt += (count + T - 1) // T
    print(tshirt)

    pen = N // P
    pen_num = N % P
    print(pen, pen_num)

N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())
baekjoon_30802(N, sizes, T, P)
