# 산술평균 : N까지의 합을 N으로 나눈값
# 중앙값 : 중앙에 위치한 값
# 최빈값 : 가장 많이 나타낸 값
# 범위 : 최대 최소값 차이

import sys
r=range;input=sys.stdin.readline
num=sorted([int(input()) for _ in r(int(input()))])

print(round(sum(num)/len(num)))

print(num[len(num)//2])

cnt={}
for i in num:
    cnt[i]=cnt[i]+1 if i in cnt else 1
max_cnt = max(cnt.values())
max_arr = sorted([k for k,n in cnt.items() if n == max_cnt])
if len(max_arr)>1:
    print(max_arr[1])
else:
    print(max_arr[0])
    
print(max(num)-min(num))