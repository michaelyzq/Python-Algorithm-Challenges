"""
https://leetcode.com/problems/implement-strstr/description/
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        n = len(haystack)-len(needle)+1
        for i in range(n):
            if haystack[i:i+len(needle)] == needle:
                return i
        
        return -1
        