'''
Given a 32-bit signed integer, reverse digits of an integer.
Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21


'''
inputs = [123,-123,120]
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_convert = str(x)
        negative = False
        if str_convert [0] == "-":
            negative = True
            str_convert = str_convert[1:len(str_convert)]
        output_str = ""
        n = list(reversed(xrange(len(str_convert))))
        for i in n:
            output_str = output_str + str_convert[i]
        output_int = int(output_str)
        if negative:
            output_int = -output_int
        return output_int
            
        
        
s = Solution()
for i in inputs:
    print s.reverse(i)