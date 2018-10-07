"""
https://leetcode.com/problems/next-permutation/description/
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1


"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return nums
        partn = 0
        part = nums[partn]
        
        for i in reversed(range(len(nums))):
            if nums[i] > nums[i-1]:
                part, partn = nums[i-1],i-1
                break

        for i in reversed(range(len(nums))):
            if nums[i] >part:
                nums[partn],nums[i] = nums[i] ,nums[partn]
                break
        tempList = nums[0:partn+1]
        nums[0:partn+1] =[-1]*(partn+1)
        nums.sort()
        nums[0:partn+1] = tempList