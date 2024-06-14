# if m < 45:
#     if h == 0:
#         print(f'23 {m+15}')
#     else:
#         print(f'{h-1} {m+15}')
# else:
#     if h == 0:
#         print(f'23 {m-45}')
#     else:
#         print(f'{h-1} {m-45}')

h, m = map(int, input().split())

if m < 45:
    if h == 0:
        h = 23
        m += 60
    else :
        h -= 1	
        m += 60
        
print(h, m-45)	