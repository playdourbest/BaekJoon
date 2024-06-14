a, b = input().split()

try:
    a = int(a)
    b = int(b)

    print(abs(a-b))

except:
    a = float(a)
    b = float(b)

    print(abs(a-b))