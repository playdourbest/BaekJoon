N=int(input()); r=range
w=[str(input()) for i in r(N)]
w=list(set(w)); w.sort(); w.sort(key=len)
for i in w:
    print(i)