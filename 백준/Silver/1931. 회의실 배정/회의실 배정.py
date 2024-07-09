# 겹치지 않고 할수있는 회의 최대 개수 구하기
# 회의가 끝나는 동시에 다음 회의가 시작가능

# <input>
# N=회의의 수
# 다음줄부터 = 시작시간 + 끝나는 시간
# <output>
# 회의의 최대 개수

import sys
r=range;input=sys.stdin.readline

def baekjoon_1931(n):
    global end,output
    time=[list(map(int,input().split())) for _ in r(n)]
    time.sort(key=lambda x:(x[1],x[0]))
    for n_start, n_end in time:
        if end <= n_start:
            output += 1
            end = n_end
    print(output)
    
if __name__=='__main__':
    end,output=0,0
    n=int(input())
    baekjoon_1931(n)