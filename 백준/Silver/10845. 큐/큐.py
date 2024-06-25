# N 개의 명령 실행
# push 1 -> 값이 2개(push 랑 1)가 list에 저장
# [0] 값을 입력으로 받고 [1] 값을 삽입하도록 설정
import sys
r=range;input=sys.stdin.readline
list=[]
for _ in r(int(input())):
    f=input().split()
    if f[0]=='push':list.append(f[1])
    elif f[0]=='pop':
        if len(list)>0:print(list[0]);del list[0]
        else:print(-1)
    elif f[0]=='size':print(len(list))
    elif f[0]=='empty':
        if len(list)==0:print(1)
        else:print(0)
    elif f[0]=='front':
        if len(list)>0:print(list[0])
        else:print(-1)
    elif f[0]=='back':
        if len(list)>0:print(list[-1])
        else:print(-1)