print("## 택배를 보내기 위한 정보를 입력하세요. ##")
Name = input("받는 사람 : ")
Adress = input("주소 : ")
weight = int(input("무게(g) : "))
fee = weight * 5
print("** 받는 사람 ==> ", Name)
print("** 주소 ==> ", Adress)
print("** 배송비 ==> ", fee,"원")


