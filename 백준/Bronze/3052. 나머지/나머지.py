out = []
for _ in range(10):
    a = int(input())
    out.append(a%42)
print(len(set(out)))