arr = [1,3,7,2,12]

target = 10
# Return indices of number that sums to 10


# Brute force
def twoSum(arr, target):
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      if(arr[i]+arr[j]==target):
        return [i,j]

# Time complexity is O(n²) — nested loops over n elements.        
print(twoSum(arr,target))


# python decorator