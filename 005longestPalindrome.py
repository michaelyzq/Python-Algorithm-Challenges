#https://leetcode.com/problems/longest-palindromic-substring/
nput= "babbad"
input2 = "abcbae"
import operator

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        palin_dict = {}
        for n in xrange(len(s)-1):
            i = 1
            text = s[n]
            if s[n] <> s[n+1]:
                while n-i>=0 and n+i<=len(s)-1:            
                    if s[n-i] == s[n+i]:
                        text = s[n-i] + text +s[n+i]
                        palin_dict[n] = text
                    else:
                        break
                    i = i+1    
            else:
                 text = s[n]+ s[n+1]
                 while n-i>=0 and n+i<=len(s)-1:            
                    if s[n-i] == s[n+1+i]:
                        text = s[n-i] + text +s[n+1+i]
                        palin_dict[n] = text
                    else:
                        break
                    i = i+1 
                
         
        output = ""
        for item in palin_dict.items():
            if len(item[1]) > len(output):
                output = item[1]
        print output
 
s = Solution()
s.longestPalindrome(input2)
