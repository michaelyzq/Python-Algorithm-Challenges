"""
https://leetcode.com/problems/perfect-squares/description/
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

"""
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        if n ==1:
            return 1
        coin_list = []
        while i**2 <=n:
            coin_list.append(i**2)
            i = i+1
        mem = [0]* (n+1)
        for i in range(1, n+1):
            choices = [t for t in coin_list if t <= i]
            mem[i] = 1 + min(mem[i-t] for t in choices)
        return mem[n]
