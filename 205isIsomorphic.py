"""
https://leetcode.com/problems/isomorphic-strings/description/
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.transferStrToNum(s) == self.transferStrToNum(t)
    def transferStrToNum(self, s):
        ng = numger_generators()
        tempDict = {}
        output = ""
        if s in (None, ""):
            return ""
            
        for i in s:
            if i in tempDict:
                pass
            else:
                number = ng.next()
                tempDict[i] = str(number)
            output = output+ tempDict[i]
        return output
        

def numger_generators():
    i = 0
    while True:
        yield i
        i = i+1