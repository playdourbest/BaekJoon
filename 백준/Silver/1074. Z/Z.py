import sys
input=sys.stdin.readline

def baekjoon_1074(N, r, c):
    if N==0:
        return 0
    fourth = 2**(N-1)
    if r < fourth and c < fourth:
        return baekjoon_1074(N-1, r, c)
    elif r < fourth and c >= fourth:
        return fourth * fourth + baekjoon_1074(N-1, r, c-fourth)
    elif r>= fourth and c < fourth:
        return fourth * fourth * 2 + baekjoon_1074(N-1, r-fourth, c)
    else:
        return fourth * fourth * 3 + baekjoon_1074(N-1, r-fourth, c-fourth)

N, r, c = map(int, input().split())
print(baekjoon_1074(N, r, c))