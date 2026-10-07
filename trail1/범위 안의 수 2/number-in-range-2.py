num = 0
cnt = 0
for i in range(10):
    n = int(input())
    if 0 <= n <= 200:
        cnt += 1
        num += n
c = num / cnt
print(f'{num} {c:.1f}')