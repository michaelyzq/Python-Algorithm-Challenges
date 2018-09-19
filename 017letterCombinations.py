'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''
class Solution(object):
    def __init__(self):
        self.d = {}
        self.d[1] = []
        self.d[2] = ["a","b","c"]
        self.d[3] =  ["d", "e", "f"]
        self.d[4] = ["g", "h", "i"]
        self.d[5] = ["j","k","l"]
        self.d[6] = ["m","n","o"]
        self.d[7] = ["p","q","r","s"]
        self.d[8] = ["t", "u", "v"]
        self.d[9] = ["w","x","y", "z"]
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        rets = self.d[int(digits[0])]
        return self.returnCombs(rets, digits[1:])
    def returnCombs(self, rets, digits):
        if digits == "" :
            return rets
        else:
            newrets = []
            for i in rets:
                for m in self.d[int(digits[0])]:
                    newrets.append(i+m)
        return self.returnCombs(newrets, digits[1:])