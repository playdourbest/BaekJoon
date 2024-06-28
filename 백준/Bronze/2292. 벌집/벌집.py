# 육각형 벌집 -> 한칸당 6 배수씩 차이
# ex) 1 -> 1+6 -> 7+12 ->....
import sys
input=sys.stdin.readline
N=int(input())
num,cnt=1,1
while N>num:
    num+=(6*cnt)
    cnt+=1
print(cnt)