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
