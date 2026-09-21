N, M = map(int,input().split())
num = list(map(int, input().split()))
cnt = 0
for char in range(N):
    if num[char] == M:
       cnt += 1
print(cnt) 