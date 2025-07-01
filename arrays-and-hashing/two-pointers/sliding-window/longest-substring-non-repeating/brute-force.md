1. Brute Force Approach

🎯 Idea:
Try all possible substrings and check if all characters are unique.

🧠 Logic:
- For every starting index i, try every possible ending index j.
- Check if the substring s[i...j] has all unique characters.
- Track the maximum length of such substrings.

🧪 Complexity:
Time: O(N³) — O(N²) substrings × O(N) check

Space: O(N) for checking uniqueness


# Mistake 1
Forgot that you can specify which index to start with range

Should be
```py
 for j in range(i+1,len(s)):
```

# Mistake 2
Don't know that you can check uniqueness by create a set and comparing the length

 Check if substring s[i...j-1] is unique

```py
def lengthOfLongestSubstring(s: str) -> int:
    def all_unique(sub):
        return len(set(sub)) == len(sub)

    max_len = 0
    n = len(s)

    for i in range(n):
        for j in range(i + 1, n + 1):
            if all_unique(s[i:j]):
                max_len = max(max_len, j - i)

    return max_len
```