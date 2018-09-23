"""
https://leetcode.com/problems/generate-parentheses/description/
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]


"""
from itertools import combinations


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lists = [c for c in combinations(range(2*n),n)]
        retn = []
        for l in lists:
            s = 0
            for i in range(2*n):
                if i in l:
                    s = s+1
                else:
                    s= s-1
                if s<0:
                    break
            if s ==0:
                retn.append(l)
        rets = []
        for i in retn:
            s= ""
            for m in range(2*n):
                if m  in i:
                    s = s+"("
                else:
                    s = s + ")"
            rets.append(s)
        
        return rets