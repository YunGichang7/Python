buy_coffee = int(-500)
buy_riceroll = int(-900)
buy_milk = int(-800)
buy_box = int(-3500)
buy_coke = int(-700)
buy_snack = int(-1000)
sell_coffee = int(+1800)
sell_riceroll = int(+1400)
sell_milk = int(+1800)
sell_box = int(+4000)
sell_coke = int(+1500)
sell_snack = int(+2000)


today = buy_riceroll*10 + sell_milk*2 + buy_box*5 + sell_box*4 + sell_coke + sell_snack*4 + sell_coffee*5
print("오늘 총 매출액은 ", today, "원입니다.")
