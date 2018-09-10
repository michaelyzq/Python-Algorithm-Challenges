
# 
# Given a sequence of n integers a1, a2, ..., an,
# a 132 pattern is a subsequence ai, aj, ak such that i < j < k and
# ai < ak < aj. Design an algorithm that takes a list of n numbers as
# input and checks whether there is a 132 pattern in the list.
#
# Note: n will be less than 15,000.
#
# Example 1:
# Input: [1, 2, 3, 4]
#
# Output: False
#
# Explanation: There is no 132 pattern in the sequence.
# Example 2:
# Input: [3, 1, 4, 2]
#
# Output: True
#
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
# Example 3:
# Input: [-1, 3, 2, 0]
#
# Output: True

input = [1, 2, 3, 4]

n = xrange(len(input)-2)
class Solution(object):
    @classmethod
    def find_pattern_input(cls, input):
        return cls.find_pattern(input[1:len(input)],input[0])
    @classmethod
    def find_pattern(cls,input, a):
        if len(input)<2:
            return False
        maxA = float("-inf")
        for n in input:
            if n > maxA and n >a:
                maxA = n
            if n> a and n < maxA:
                return True

        return cls.find_pattern(input[1:len(input)],input[0])

		
##
class Solution2(object):
    @classmethod
    def find_pattern_input(cls, input):
		m = xrange(len(input)-2)
		for a in m:
			maxA = float("-inf")
			for n in input[a:len(input)]:
				if n > maxA and n >a:
					maxA = n
				if n> a and n < maxA:
					return True
		return False
		
print Solution2.find_pattern_input([3, 100, 4, 2,1])
print Solution2.find_pattern_input([1,2,3,4,5])
