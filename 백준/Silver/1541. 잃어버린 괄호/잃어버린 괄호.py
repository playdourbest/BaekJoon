# 연속해서 두개 이상 연산자 x
# 5자리보다 많이 연속되는 숫자 x
# 작은값이 나오려면 큰수로 빼주는 형태가 되어야한다.
# ex) 55-(50+40) 이면 무려 90으로 빼주는 형태가 된다.

# '-'단위로 끊어주고 '+' 단위로 끊어 묶어서 계산 후 빼주면 된다
import sys
r=range;input=sys.stdin.readline

negative=input().split('-')
cal=[]
for i in negative:
    sum=0
    plus=i.split('+')
    for j in plus:
        sum+=int(j)
    cal.append(sum)

n=cal[0]
for i in r(1,len(cal)):
    n-=cal[i]
print(n)