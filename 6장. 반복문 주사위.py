import random
i, j, k = 0, 0, 0
count = 0

while True :
    count += 1
    i = random.randint(1,6)
    j = random.randint(1,6)
    k = random.randint(1,6)
    if i == j== k :
        break

print("3개 주사위는 모두 ", i, "입니다.\n" "같은 숫자가 나오기까지 ", count, "번 던졌습니다.")
