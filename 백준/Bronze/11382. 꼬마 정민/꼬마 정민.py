a, b, c = input().split()
try:
    a = int(a)
    b = int(b)
    c = int(c)
    print(a+b+c)
except:
    a = float(a)
    b = float(b)
    c = float(c)
    print(a+b+c)