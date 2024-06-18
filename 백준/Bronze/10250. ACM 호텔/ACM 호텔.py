t = int(input())
room_num = []

for i in range(t):
    h, w, n = map(int, input().split())
    room_num.clear()
    
    for j in range(1, w+1):
        for k in range(1, h+1):
            k *= 100
            k += j
            room_num.append(k)
    print(room_num[n-1])

# for _ in range(int(input())):
#  a,b,c=map(int,input().split())
#  print(((c-1)%a+1)*100+(c-1)//a+1)
