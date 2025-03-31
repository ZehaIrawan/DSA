I forgot how to get index with loops in python

1. for Loop with enumerate()

Python's built-in enumerate() function allows you to iterate over an iterable while also keeping track of the index.

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
```

2. Using a for Loop with range(len(iterable))
If you need just the index and access the elements using indexing:

```python
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")
```

Use this when you specifically need the index and prefer explicit indexing.

    # day is index + 1
    # price is array[index] value
    # iterate through the day
    # can use two loops for implementing two pointers
    # can also use hashmap

    # mistake 1
    # using enumerate where i should use range(len(nums))
    # enumerate() only gives you the current index and value—it doesn't provide a way to  iterate over the remaining elements.
    # you can't look ahead via index+1
    # with range you can specify which index to start the loop

    # mistake 2
    # Wrong Profit Calculation
    # prices[i] is the buy price, prices[j] is the sell price
    # should have been prices[j] - prices[i] instead of  prices[i] - prices[j] 

    # mistake 3
    # nested loops has  O(n²) time complexity, so ran into Time Limit Exceeded
    #
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                current_profit = prices[j] - prices[i] 
                if current_profit > max_profit:
                    max_profit = current_profit
        if max_profit > 0:
            return max_profit
        return 0