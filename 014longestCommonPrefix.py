'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.



'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) ==0:
            return ""
        lens =[ (len(v),index)for index, v in enumerate(strs)]
        pattern = strs[sorted(lens)[0][1]]
        return self.findprefix(strs, pattern)
        
    def findprefix(self, list_input, pattern):
        if pattern == "":
            return ""
        match = True
        for i in list_input:
             if i[:len(pattern)] != pattern:
                match = False
                break
        if not match:
            return self.findprefix(list_input, pattern[:len(pattern)-1])
        else:
            return pattern 
        
