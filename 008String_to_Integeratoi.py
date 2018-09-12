
"""

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

"""

    
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip()
        negative = False
        if len(str) == 0:
            return 0
        if str[0] == "-":
            negative = True
            str = str[1:len(str)]
        elif str[0] == "+":
            str = str[1:len(str)]
        if len(str) == 0:
            return 0
      
        output_int = 0
        for i in xrange(len(str)):
            try:
                if float( output_int*10+int(str[i])) >= float(2147483648):
                    output_int = 2147483648 if negative else 2147483647
                    break
                output_int  = output_int*10 +int(str[i])
            except ValueError:
                break
        if negative:
             output_int = - output_int
        return output_int
            
        
        
        

