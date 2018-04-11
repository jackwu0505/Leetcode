# Loop through "nums" and find the indices by searching a
# hash table with (key, value) = (nums[i], index of nums[i]) 
# Time Complexity: O(n)
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numDict = {}
        # loop through each element in "nums"
        for i in range(len(nums)):
            # if current element's complement exeist in 
            # numDict, return the found indices
            if (target - nums[i]) in numDict:
                return [numDict[target-nums[i]], i]
            # add entry to numDict with (key, value) = 
            # (nums[i], index of nums[i])
            else:
                numDict[nums[i]] = i