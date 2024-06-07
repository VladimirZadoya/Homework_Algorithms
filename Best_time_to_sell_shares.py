def maxProfitII(prices):
    max_profit = 0

    for i in range(1, prices.length):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]

    return max_profit
print(maxProfitII([7, 1, 5, 3, 6, 4]))  
print(maxProfitII([1, 2, 3, 4, 5]))  
print(maxProfitII([7, 6, 4, 3, 1])) 
