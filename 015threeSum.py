'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.


'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return_list = []
        nums = sorted(nums)
        new_nums = [(v, index) for index, v in enumerate(nums)]
        ms = range(len(nums))
        ns = range(len(nums))[1:]
        m =0
        n=0
        while m <len(nums):
            n =m+1
            while n <len(nums):
                if nums[n] + nums[m] >0:
                    break
                t = 0 - nums[n] - nums[m]
                if t in nums[n+1:]:
                    a = sorted((nums[n], nums[m], t))

                    if not a in return_list:
                        return_list.append(a)                
                n = n+1
            m = m+1
        return return_list