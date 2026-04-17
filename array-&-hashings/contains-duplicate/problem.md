class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        holder = {}

        # since we dont need the index maybe array is better?
        # mistake #1. forgot to do the assigment
        # mistake #2. syntax for true and false are capitalized in Python
        # mistake #3. don't use enum if you don't need index, since it's returning both index and the value
        # #4 time limit exceed
        for i, num in enumerate(nums):
            if holder[num] in holder:
                return True
            holder[num] = i
        return False

    You’re very close, but your check is backwards and will crash.

### What’s wrong

This line:

```py
if holder[num] in holder:
```

tries to access `holder[num]` **before** confirming it exists.
So the first time you see a number, you get a `KeyError`.

Also the logic is incorrect: you want to check if **num** is already a key.

### Fix (dictionary / set approach)

#### Best solution (use a set)

```py
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
```

### Fix using your dictionary style

```py
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        holder = {}

        for num in nums:
            if num in holder:
                return True
            holder[num] = True

        return False
```

### Complexity

* Time: **O(n)**
* Space: **O(n)**

Your “time limit exceed” comment is probably from using nested loops before, but this version is fast enough.

        