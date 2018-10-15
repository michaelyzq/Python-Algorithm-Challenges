"""
https://leetcode.com/problems/count-and-say/hints/
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.
"""
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        ret_list = []
        previousn = self.countAndSay(n-1)
        for i in range(len(previousn)):
            if i ==0:
                ret_list.append([previousn[i],1])
            elif previousn[i] == previousn[i-1] :
                temp = ret_list.pop()
                ret_list.append([temp[0], temp[1]+1])
            else:
                ret_list.append([previousn[i],1])
        retstr = ""
        for i in ret_list:
            retstr = retstr + str(i[1])+i[0]
        return retstr