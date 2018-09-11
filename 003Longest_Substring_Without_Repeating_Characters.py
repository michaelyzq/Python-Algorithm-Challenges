#Given a string, find the length of the longest substring without repeating characters.

input = ["bbbbb","abcabcbb","pwwkew"]

import operator
class Solution(object):
    @classmethod
    def lengthOfLongestSubstring(cls, s):
        """
        :type s: str
        :rtype: int
        """
        ns = xrange(len(s))
        char_dict = {}
        out_put = ""
        output_dict = {}
        for i in ns:
            if char_dict.has_key(s[i]):
                char_dict = {}
                char_dict[s[i]] = s[i]
                output_dict[out_put] = len(out_put)
                out_put =  s[i]
            else:
                char_dict[s[i]] = s[i]
                out_put = out_put + s[i]
                if i  == len(s) -1:
                    output_dict[out_put] = len(out_put)
        #print output_dict
        print sorted(output_dict.items(), key=operator.itemgetter(1), reverse=True)[0][1]

for i in input:
    Solution().lengthOfLongestSubstring(i)
        
        
        

