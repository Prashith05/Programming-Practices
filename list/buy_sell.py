# xyz wantsto buy a stock with minimum prize and he need to sellthe stock toget the maximum profit.. help him when to buy a stock and when to sell to get the maximum profit based on the values given in a list

# price = [10,8,1,3,4,9,2]
# buy = 2(index)  --> stock price = 1
# sell = 5(index)  --> stock price = 9
# max-profit = 9-1 = 8

# l = [7,5,3,2,1]
# 0 

# p = [1,3,6,8,10,12]
# buy = 0(index)  --> stock price = 1
# sell = 5(index)  --> stock price = 12
# max-profit = 12-1 = 11

price = [10,8,1,3,4,9,2]
# price = [1,3,6,8,10,12]
# price = [7,5,3,2,1]
# price = [12]
# price = [12,12]
buy = price[0]
buy_index = 0
for i in range(len(price)):
    if buy > price[i]:
        buy = price[i]
        buy_index = i
sell = price[buy_index]
for i in range(buy_index,len(price)):
    if sell < price[i]:
        sell = price[i]
max_profit = sell - buy
print(f"buy: {buy}\nsell: {sell}\nmax_profit: {max_profit}")

print("------------------------------------------------------")

def stocks(price):
    if len(price) == 0:
        return 0
    else:
        maxProfit = 0
        for i in range(len(price)):
            for j in range(i+1,len(price)):
                current_profit = price[j] - price[i]
                if current_profit > maxProfit:
                    maxProfit = current_profit
        return max_profit

price = [10,8,1,3,4,9,2]
# price = [1,3,6,8,10,12]
# price = [7,5,3,2,1]
# price = [12]
# price = [12,12]
print("max_profit: ",stocks(price))