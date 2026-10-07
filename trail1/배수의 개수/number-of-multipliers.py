thr_cnt = 0
fif_cnt = 0
for i in range(10):
    num = int(input())
    if num % 3 == 0:
        thr_cnt += 1
    if num % 5 == 0:
        fif_cnt += 1
print(f'{thr_cnt} {fif_cnt}')