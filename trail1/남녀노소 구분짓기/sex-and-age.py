N = int(input())
age = int(input())
if N == 0 and age >= 19:
    print("MAN")
elif N == 0 and age <= 19:
    print("BOY")
elif N == 1 and age >= 19:
    print("WOMAN")
elif N == 1 and age <= 19:
    print("GIRL")