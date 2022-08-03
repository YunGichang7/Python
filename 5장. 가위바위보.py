import random

srp = input("나의 가위/바위/보 ==> ")
com = random.choice(["가위", "바위", "보"])
print("컴퓨터의 가위/바위/보 ==> ", com)
if srp == "가위" :
    if com == '가위' :
        print("비겼습니다.")
    elif com == '바위' :
        print("졌습니다.")
    elif com == '보' :
        print("이겼습니다.")
elif srp == '바위' :
    if com == '가위' :
        print("이겼습니다.")
    elif com == '바위' :
        print("비겼습니다.")
    elif com == '보' :
        print("졌습니다.")
elif srp == '보' :
    if com == '가위' :
        print("졌습니다.")
    elif com == '바위' :
        print("이겼습니다.")
    elif com == '보' :
        print("비겼습니다.")
else :
    print("Error")
