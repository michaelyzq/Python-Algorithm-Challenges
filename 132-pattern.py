
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

def find_pattern(input):
    for i in n:
        if input[i]< input[i+2] <input[i+1]:
            return True
            break
    return False

print find_pattern(input)