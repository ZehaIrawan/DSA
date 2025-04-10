class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        write = 1  # First element is always unique

        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1

        return write

    # https://chatgpt.com/share/67f745a3-8c38-800c-bb4a-ce6f83bcc655   

    # sorted in increasing value 0,1,3
    # modify array in place without chaning the relative order
    # leave the unique element at the start of array
    # return the modified array not the length of th earray

    # Mistake 1 
    # returning the number instead of the array


    # for i in range(len(nums)):
    #     if nums[i] <= len(nums) - 1 :
    #         if nums[i] == nums[i+1]:
    #             nums.pop(nums[i+1])
    

 

