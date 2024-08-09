import sys
r=range;input=sys.stdin.readline

def baekjoon_2630(paper, x, y, size):
    color = paper[x][y]
    for i in r(x, x + size):
        for j in r(y, y + size):
            if paper[i][j] != color:
                white1, blue1 = baekjoon_2630(paper, x, y, size // 2)
                white2, blue2 = baekjoon_2630(paper, x, y + size // 2, size // 2)
                white3, blue3 = baekjoon_2630(paper, x + size // 2, y, size // 2)
                white4, blue4 = baekjoon_2630(paper, x + size // 2, y + size // 2, size // 2)
                return (white1 + white2 + white3 + white4, blue1 + blue2 + blue3 + blue4)

    if color == 0:
        return (1, 0)  # 하얀색
    else:
        return (0, 1)  # 파란색

N = int(input())
paper = [list(map(int, input().split())) for _ in r(N)]
white_count, blue_count = baekjoon_2630(paper, 0, 0, N)
print(white_count)
print(blue_count)