a, b = input().split()
try:
    a = int(a)
    b = int(b)
    print(a*b)
except:
    a = float(a)
    b = float(b)
    print(a*b)