# Use a nested loop to loop through elements in "nums" 
# to find the indices
# Time Complexity: O(n^2)
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # loop through each element in "nums"
        for i in range(len(nums)):
            # loop through elements after index i+1
            for j in range(i+1, len(nums)):
                # if the two elements equal to the target
                if (nums[i]+nums[j]) == target:
                    # return the found indices
                    return [i,j]