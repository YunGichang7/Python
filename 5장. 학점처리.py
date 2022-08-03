score = int(input("점수를 입력하세요 : "))
if score < 90 :
    if score < 80 :
        if score < 70 :
            if score < 60 :
                print("F", end=' ')
            else :
                print("D", end=' ')
        else :
            print("C", end=' ')
    else :
        print("B", end=' ')
else :
    print("A", end=' ')

print("학점입니다.")
