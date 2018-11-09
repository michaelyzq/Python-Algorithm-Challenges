"""
https://leetcode.com/problems/integer-break/description/
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.

"""
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+2)
        dp[1] =1
        dp[2] =1
        dp[3] =2
        if n<=3:
            return dp[n]
        for i in range(4,n+1):
            temp_max = 0
            for k in range(2,i/2+1):
                if temp_max< (k)*dp[i-k]:
                    temp_max = (k)*dp[i-k]
                if temp_max < k* (i-k):
                    temp_max = k*(i-k)
            #print temp_max
            dp[i] = temp_max
        #print dp       
        return dp[n]  