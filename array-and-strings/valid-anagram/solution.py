class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string_list = list(s)
        anagram_list = list(t)

        for char in string_list[:]:
            if(char in anagram_list):
                string_list.remove(char)
                anagram_list.remove(char)
        return len(string_list) == len(anagram_list) and string_list == anagram_list

# Mistake 1
# Didn't know how  to split words to char in python
    # 1. Use list(string) => ['h','i']
    # 2  Use use a list comprehension => chars = [char for char in word]

# Mistake 2
# didn't know to remove item from list without index
    # Use remove(item)

# Mistake 3
# only use length check after loop without content check
# len(string_list) == len(anagram_list) and string_list == anagram_list

# Mistake 4
# The mistake is a classic gotcha: you're modifying a list (string_list) while iterating over it, which can lead to unexpected behavior — some elements get skipped.
# make shallow copy with [:]:

# Passing but slows
# You can sort string on python

#https://neetcode.io/solutions/valid-anagram

#https://neetcode.io/solutions/group-anagrams