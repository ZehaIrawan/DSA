# prices = [7, 1, 5, 3, 6, 4]
# Iteration 1 (price = 7):
# min_price = float('inf')

# max_profit = 0

# min_price = min(float('inf'), 7) = 7

# max_profit = max(0, 7 - 7) = 0 (No profit yet)

# Iteration 2 (price = 1):
# min_price = 7 from the previous iteration.

# max_profit = 0

# min_price = min(7, 1) = 1 (We update min_price to 1, since it's lower than the previous price)

# max_profit = max(0, 1 - 1) = 0 (Still no profit)

# Iteration 3 (price = 5):
# min_price = 1 from the previous iteration.

# max_profit = 0

# min_price = min(1, 5) = 1 (No change in min_price since 1 is still the lowest)

# max_profit = max(0, 5 - 1) = 4 (Profit of 4 if we sell at price 5)

# Iteration 4 (price = 3):
# min_price = 1 from the previous iteration.

# max_profit = 4

# min_price = min(1, 3) = 1 (No change in min_price)

# max_profit = max(4, 3 - 1) = 4 (Still max profit of 4)

# Iteration 5 (price = 6):
# min_price = 1 from the previous iteration.

# max_profit = 4

# min_price = min(1, 6) = 1 (No change in min_price)

# max_profit = max(4, 6 - 1) = 5 (Profit of 5 if we sell at price 6)

# Iteration 6 (price = 4):
# min_price = 1 from the previous iteration.

# max_profit = 5

# min_price = min(1, 4) = 1 (No change in min_price)

# max_profit = max(5, 4 - 1) = 5 (Still max profit of 5)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf') 
        max_profit = 0 
        
        for price in prices: 
            min_price = min(min_price, price) 
            max_profit = max(max_profit, price - min_price) 
        
        return max_profit