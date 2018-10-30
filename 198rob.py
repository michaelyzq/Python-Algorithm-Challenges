"""
https://leetcode.com/problems/house-robber/description/
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        if 0<len(nums) <=2:
            return max(nums)
        elif len(nums) == 0:
            return 0
        else:
            return max(nums[0]+self.rob(nums[2:]), self.rob(nums[1:]))
        """
        if not nums:
            return 0
        cach = [0]*len(nums)
        for i in reversed(range(len(nums))):
            if i >=len(nums) -2:
                cach[i] = max(nums[i:])
            else:
                cach[i] = max(nums[i] + cach[i+2], cach[i+1])
        return cach[0]
            