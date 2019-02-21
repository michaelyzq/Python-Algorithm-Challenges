"""
https://leetcode.com/problems/combination-sum/
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #global final_result 
        final_result = []
        candidates.sort()
        def findCom(target, temp_list):
            if target in candidates:
                a = temp_list + [target]
                if sorted(a) not in final_result:
                    final_result.append(a)
            for i in [n for n in candidates if n < target]:
                #print (i, target,temp_list)
                a = temp_list + [i]
                findCom(target -i, a)
        
        t = []
        findCom(target, t)
        #print final_result
        return final_result
                            