

🥈 2. Better Approach: Sliding Window with Set
🎯 Idea:
Use a sliding window and expand it until you see a duplicate. If you see a duplicate, shrink the window from the left.

🧠 Logic:
Use two pointers left and right.

Use a set to store characters in the current window.

Move right to expand the window.

If character is repeated, move left until there are no duplicates.

🧪 Complexity:
Time: O(2N) → each character is visited at most twice

Space: O(min(N, M)) where M = charset size

🥇 3. Optimal Approach: Sliding Window with HashMap
🎯 Idea:
Instead of moving left one by one, jump it directly after the last occurrence of the duplicate character using a map.

🧠 Logic:
Use a dict to store the last index of each character.

When you encounter a duplicate, move left to max(left, last_index + 1).

🧪 Complexity:
Time: O(N) — each character processed once

Space: O(min(N, M))

===

```py
    def lengthOfLongestSubstring(self, s: str) -> int:

        for i in range(len(s)):
            for j in range(len(s)-1):
                print(s[i],s[j])
```
