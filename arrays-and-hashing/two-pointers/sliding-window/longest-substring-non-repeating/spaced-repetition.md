1. set
2. left & right pointer
3. for loop
3. while loop
4. check in set
5. max min



===
attempt 1

# Mistake 1

the adding of the right should be outside of the while loop

# Mistake 2

the max length should also be outside of the while loop

# Mistake 3
should be returning the max_length instead of the max comparison

```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()

        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in unique:
                unique.remove(s[left])
                unique.add(s[right])
                left += 1
                max_length = right - (left + 1)
        return max(max_length,right - (left + 1))
```

===
create a set to hold the unique chars

start from the left, which is index 0

set max_length to 0

iterate through the string, use right as the index
	inside the loop, create a condition for a while loop
	when the character is found in the char set
	we remove the leftmost chacter
	and move the left poitner by 1
	then we add the string to the right
	then we compare if the current max_length is bigger or not than the current length of the string

