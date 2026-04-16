class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # the difference with two sum 1 is that the input array is sorted
        # so if the current number is already doesnt match we can skip the iteration of the rest of the array
        # mistake 1
        # forgot to read that has to add index by 1

        # mistake 2 order matter
        # wrong : [i + index_inc,hashmap[complement]+index_inc]
        # right = [hashmap[complement]+index_inc, i + index_inc]

        # how to remove items from hashmap
        # pop with key
        hashmap = {}
        index_inc = 1

        #numbers = [2,7,11,15], target = 9
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if(complement in hashmap):
                return [hashmap[complement]+index_inc, i + index_inc]
                # remove from hashmap if already used
                hashmap.pop(numbers[i])
            hashmap[numbers[i]] = i

# Optimize

# https://youtu.be/cQ1Oz4ckceM

# def twoSum(self, numbers: List[int], target: int) -> List[int]:
#   l, r = 0, len(numbers) - 1
#
#  while l < r:
#       curSum = numbers[l] + numbers[r]
#
#       if curSum > target:
#           r -= 1
#       elif curSum < target:
#           l += 1
#       else:
#           return [l + 1, r + 1]
# guaranteed solution so no need return []


# minimal form
left,right = 0, len(numbers) - 1

while left < len(numbers):
    print(left,right)
    left += 1

# this is just moving the left pointer until it reaches the end of the array, and the right pointer is not moving at all.


# passing test cases but time limit exceeded

        left,right = 0, len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] == target:
                return [left+1,right+1] 


# feedback
Your loop can get **stuck forever**.

You only move `right` when the sum is too big, and you return when it matches.

But you **never move `left`** when the sum is too small.

So if:

```py
numbers[left] + numbers[right] < target
```

nothing changes → infinite loop.

Fix:

```py
left, right = 0, len(numbers) - 1

while left < right:
    s = numbers[left] + numbers[right]

    if s > target:
        right -= 1
    elif s < target:
        left += 1
    else:
        return [left + 1, right + 1]
```

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    # since the requirement is no extra space we can't use hashmap
    # brute force with nested loop can work but that will have O2(n) time complexity
    # we need  to use two pointer solution
    # the way that it works is by iterating from leftmost and rightmost at the same time
    # and then move the index after each loop

    # define left and right pointer
    # later adjust the index 0 to 1 based
  
    # since it's 0 based index 
    # need to decrease 1 from the length of the input array
    # otherwise it will read 4 in array that mas index of 3

    # we need to move the right pointer to the left before increasing the left pointer
    # the sum of the left and right pointer is greater then target, move the right pointer to left by 1

    # tweak needed is to handle move the left if total is smaller than target

        left,right = 0, len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left+1,right+1] 