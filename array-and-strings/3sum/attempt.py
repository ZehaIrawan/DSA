class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # iterate through the array, find 3 combination that equals to 0
        # brute force with three nested loops won't work
        # order of output doesn't matter
        # format of output is an array containing all triplets arrays
        # my first thought is to use nums[i+1] and nums[i+2], but the problem is i need to do checking if the index is at the end of array, otherwise i will get error: IndexError: list index out of range
        target = 0   
        result = []
        hashmap = {}
        for i in range(len(nums)):
            hashmap[i] = nums[i]
            second_number = nums[i+1]
            if(nums[i] + hashmap[i+1]):
              return
            # save in hashmap
            # somehow check the if 2 items in the object amount to 0
            # sliding window doesnt work because the combination can be in one end and the other end
        return hashmap


# two pointer
        
        l = 0
        r = len(nums) - 4

        res = []

        while l < r:
            # this works but it doesnt need to be sequential
            # need another way to reiterate remaining item
            if((nums[l] + nums[l+1] + nums[l+2]) == 0):
                res.append([nums[l], nums[l+1], nums[l+2]])
            l += 1
            # after looking at the solution the key is to sort the array first
            # why sort? because then you don't have to check all item in the array
        return res
