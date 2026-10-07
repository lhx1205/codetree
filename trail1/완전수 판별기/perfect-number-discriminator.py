N = int(input())
a = 0 # 약수들의 합을 담는 값
for i in range(1,N+1): # 1부터 N까지
    if N % i == 0 and i != N: # i가 N의 약수이면
        a += i
if a == N:
    print("P")
else:
    print("N")