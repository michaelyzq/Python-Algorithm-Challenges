"""
https://leetcode.com/problems/reverse-integer/description/
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if x<0:
            negative = True
            x = -x
        s = str(x)
        n10 = 0
        ret = 0
        for i in range(len(s)):
            ret = ret + int(s[i])*(10**n10)
            n10 = n10+1
        if ret < (-2)**(31):
            return 0
        if ret > (2)**(31)-1:
            return 0
        return -ret if negative else ret