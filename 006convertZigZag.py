"""
https://leetcode.com/problems/zigzag-conversion/
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows ==1:
            return s
        elif numRows ==2:
            count = len(s)
            return "".join([s[i] for i in range(len(s)) if i%2 ==0])+\
            "".join([s[i] for i in range(len(s)) if i%2 ==1])
        column = []
        row_n = 1
        direction = 'Down'
        final_list = []
        down_list = []
        for a in range(len(s)):
            print direction, str(row_n)
            i =  s[a]
            if direction == 'Down':    
                down_list.append(i)
                row_n = row_n +1
                if row_n > numRows or a == len(s)-1:
                    final_list.append(down_list)
                    direction = 'Up'
                    row_n = row_n-2
                                  
            else:      
                temp_list = [None]*numRows
                temp_list[row_n-1] = i
                final_list.append(temp_list)
                row_n = row_n -1 
                if row_n ==1:
                    direction = 'Down'  
                    down_list = []
         
        #print final_list  
        final_str = ""
        for n in  range(numRows):
            for i in final_list:
                if len(i)-1>=n and i[n] != None:
                    final_str = final_str + i[n]
        return final_str
                    
            