class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        # array of strings
        # iterate through array
        # check the char on each item
        # compare the char to other item
        hashmap = {}

        # create array to hold
        # group array
        for index in range(len(strs)):
            chars = strs[index]
            sorted_chars = ''.join(sorted(strs[index]))
            if(sorted_chars in hashmap.keys()):
                hashmap[sorted_chars].append(strs[index])
            else:
                hashmap[sorted_chars] = [strs[index]]

        result = []
        
        for item in hashmap:
            result.append(hashmap[item])

        return result   
                
        
        # after 15
        # key for anagram is sort and compare
        # hint 1: A naive solution would be to sort each string and group them using a hash map

        # mistake 1
        # sort(item) is wrong, correct is .sort() in PY

        # mistake 2
        # sorted is for chars

        # mistake 3
        # reversed logic when to append and when to create array

        # mistake 4
        # there are no push method in python list, only insert or append

        # mistake 5
        # stroring index in dict instead of actual strings

        # mistake 6
        # returning keys instead of value of the hashmap