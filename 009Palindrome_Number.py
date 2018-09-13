'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <0:
            return True
        a = 0
        x_copy = x
        first_loop = True
        while True:
            curr = x%10         
            a = a*10 +curr
            if x <10:
                break
            x = x/10
            
            
        
s = Solution()
print s.isPalindrome("12321")
        