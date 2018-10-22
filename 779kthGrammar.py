"""
https://leetcode.com/problems/k-th-symbol-in-grammar/description/
On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).
"""
class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N ==1 and K == 1:
            return 0
        cols = 2**(N-1)
        if K > cols /2:
            return abs(1-self.kthGrammar( N-1, K- cols /2))
        else:
            return self.kthGrammar( N-1, K)
                