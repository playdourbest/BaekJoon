a, b = input().split()

try:
    a = int(a)
    b = int(b)

    if a > b:
        print('>')
    elif a < b:
        print('<')
    elif a == b:
        print('==')

except:
    a = float(a)
    b = float(b)

    if a > b:
        print('>')
    elif a < b:
        print('<')
    elif a == b:
        print('==')