"""
https://leetcode.com/problems/multiply-strings/description/
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

"""
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = len(num1) -1
        a1 = 0
        for i in num1:
            a1 = a1+ int(i)*(10**n1)
            n1 = n1-1
        n2 = len(num2) -1
        a2 = 0

        for i in num2:
            a2 = a2+ int(i)*(10**n2)
            n2 = n2-1       
        return str(a1*a2)