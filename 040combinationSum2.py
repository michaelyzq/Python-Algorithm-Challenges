"""
https://leetcode.com/problemset/all/
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""



class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.final_result = []
        candidates.sort()

        t = []
        self.findCom(target, t, candidates)
        #print final_result
        return self.final_result
    def findCom(self,target, temp_list,new_candidates):
        if target in new_candidates:
            a = temp_list + [target]
            if sorted(a) not in self.final_result:
                self.final_result.append(a)
        for x in list(xrange(len(new_candidates))):
            i = new_candidates[x]
            if i > target:
                return
            #print (i, target,temp_list)
            a = temp_list + [i]
            self.findCom(target -i, a,new_candidates[0:x]+ new_candidates[x+1:(len(new_candidates))])
