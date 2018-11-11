"""
https://leetcode.com/problems/longest-palindromic-substring/description/
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        longest = s[0]
        i = 0
        while i < len(s):
            p =1
            while i+p <len(s) and s[i] == s[i+p]:
                p = p+1
            temp_s = s[i:i+p]
            if len(temp_s) > len(longest):
                longest = temp_s
            k=1
            while i+p-1+k <len(s) and i-k >=0:
                if s[i-k]== s[i+p-1+k]:
                    temp_s = s[i-k]+temp_s+s[i+p-1+k]
                    if len(temp_s) > len(longest):
                        longest = temp_s
                else:
                    break
                k = k+1
            i = i+p
              
        return longest
        