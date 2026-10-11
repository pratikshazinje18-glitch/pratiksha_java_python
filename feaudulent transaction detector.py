count = 0
total = 0
for i in range (8):
    amount = int(input("entetr transaction amount"))
    if amount > 100000:
        count +=1
        total = total + amount
        print("suspicious transaction:",count)
        print("total suspicious transaction value:",total)
