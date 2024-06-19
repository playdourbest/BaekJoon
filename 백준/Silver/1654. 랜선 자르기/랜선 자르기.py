N,K=map(int,input().split());r=range
LAN_tnt=[int(input()) for _ in r(N)]
s,e=1,max(LAN_tnt)
while s<=e:
    mid=(s+e)//2
    if sum(i//mid for i in LAN_tnt)>=K:
        s=mid+1
    else:
        e=mid-1
print(e)