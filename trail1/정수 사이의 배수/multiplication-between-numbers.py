a, b = map(int, input().split())
sum_val = 0
mean_val = 0
cnt = 0
for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        cnt += 1
        sum_val += i
        mean_val = sum_val / cnt
print(f'{sum_val} {mean_val:.1f}')