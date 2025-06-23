class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # iterate through the string
        # find longest substring that is not repeated
        # define the substring

        # [a,b,c]
        #  "abcbb"
        #
        storage = []

        for i in range(len[s]):
            if s[i] not in storage:
                storage.append(s[i])

        print(storage)


#