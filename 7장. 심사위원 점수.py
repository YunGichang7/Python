name = input("선수 이름을 입력하세요 : ")
"""
print(name, " 선수 경기 끝났습니다~~ 짝짝짝\n 심사위원 분들은 점수를 입력해 주세요.")
score1 = int(input("평가 점수 ==> "))
score2 = int(input("평가 점수 ==> "))
score3 = int(input("평가 점수 ==> "))
score4 = int(input("평가 점수 ==> "))
score5 = int(input("평가 점수 ==> "))
avg = (score1 + score2 + score3 + score4 + score5)/5
print("심사위원 평균 점수 : ", avg)
"""

score = []
for i in range(5) :
    sc = int(input("평가 점수 ==> "))
    score.append(sc)

scoresum = sum(score)
scorecount = len(score)
print("심사위원 평균 점수 : ", scoresum/scorecount)
