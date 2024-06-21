# 직각삼각형 - 피타고라스 정리 사용
while 1:
    A,B,C=sorted(map(int,input().split()))
    if A==B==C==0: break
    print('right' if (A*A)+(B*B)==C*C else 'wrong')