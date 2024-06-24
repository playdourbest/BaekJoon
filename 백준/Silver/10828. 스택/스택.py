# 실행시킬 수 N
# N 개의 명령어 추가
# 1 < < 100,000 -> 실행횟수가 많음 - sys.stdin.readline써야함

import sys
r=range;input=sys.stdin.readline
list=[]
for _ in r(int(input())):
    command=input().split()
    if command[0]=='push':list.append(command[1])
    elif command[0]=='pop':
        if len(list)>0:print(list.pop())
        else:print(-1)
    elif command[0]=='size':print(len(list))
    elif command[0]=='empty':
        if len(list)==0:print(1)
        else:print(0)
    elif command[0]=='top':
        if len(list)>0:print(list[-1])
        else:print(-1)
    