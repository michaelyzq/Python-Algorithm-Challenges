'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        con_list =  [(v, index) for index, v in enumerate(height)]
        n =0
        m = 0
        max_area = 0
        while n < len(con_list) :
            m=n+1

            while m< len(con_list):
                if n>=m:
                    continue
                value = min(con_list[m][0],con_list[n][0])*\
                (abs(con_list[n][1]-con_list[m][1]))
                if max_area<value:
                    max_area =value
                m = m+1
                
            n = n+1

        return max_area
