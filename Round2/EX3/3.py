cash = list(map(int, input().split()))
money = int(input())


cash.sort(reverse=True)

print(cash)
if money % cash[len(cash) - 1]:
    print("Can not give money. Sorry!")
else:
    countMoney = [0]*len(cash)
    for i in range(len(cash)):
        if money > cash[i]:
            k = money // cash[i]
            money -= k*cash[i]
            countMoney[i] = k

for i in range(len(cash)):
    if(countMoney[i]):
        print(f"{cash[i]}x{countMoney[i]}")


