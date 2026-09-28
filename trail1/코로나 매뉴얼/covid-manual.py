data = [input().split() for _ in range(3)]  # 세 줄 입력받아 리스트로 저장
count = sum(1 for x, y in data if x == 'Y' and int(y) >= 37)  # 조건에 맞는 경우 카운트

print("E" if count >= 2 else "N")

