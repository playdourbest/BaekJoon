n = int(input())
fix = 666
cnt = 0

while True:
    if '666' in str(fix):
        cnt+=1
    if cnt == n:
        print(fix)
        break
    fix+=1