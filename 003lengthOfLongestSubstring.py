"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==1:
            return 1
        elif not s:
            return 0
        elif s[-1]== s[-2]:
            return self.lengthOfLongestSubstring(s[:-1])
        dp = [1]*len(s)
        for i in range(len(s)-2, -1,-1):
            temp_str = s[i+1:i+1+dp[i+1]]
            while temp_str: 
                if s[i] not in temp_str:
                    dp[i] = len(temp_str)+1
                    break
                else:
                    temp_str = temp_str[:-1]
           
        print dp   
        return max(dp)
