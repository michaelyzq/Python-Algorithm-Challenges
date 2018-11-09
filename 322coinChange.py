"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.

"""



class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins:
            return -1
        mem =[-1]* (amount+1)
        mem[0] = 0
        for i in range(1, amount+1):
            if i in coins:
                mem[i] = 1
                continue
            pre_list = [mem[i - c] for c  in coins if c <=i and mem[i-c]>=0]
            mem[i] = 1+min(pre_list) if len(pre_list) >0 else -1
        return mem[amount]
