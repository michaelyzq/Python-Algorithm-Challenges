"""
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.

"""
from itertools import combinations
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        average_val = sum(nums)/k
        print average_val
        if max(nums) >average_val:
            return False
        nums.sort(reverse = True)
        #print nums
        nums = filter(lambda x: x != average_val, nums)
        
        def recur_Subset(nums, a):
            if len(nums) == 0: return True
            #print nums
            
            for k in range(1, len(nums)+1, 1):
            #for k in range(len(nums),0,-1):
                for i in list(combinations (range(len(nums)),k)):                    
                    if sum(list(nums[i2] for i2 in i)) ==a:   
                        if recur_Subset(list(nums[m] for m in range(len(nums)) if m not in i )  ,a):
                            return True
            return False
        return recur_Subset(nums, average_val )
   