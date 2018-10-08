"""
https://leetcode.com/problems/task-scheduler/description/
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

"""
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        tasksn =len(tasks)
        d = collections.Counter(tasks)
        cool = {key[0]:0 for key in d.items()}
        t = 0
        while tasksn >0:            
            pendings = sorted(d.items(), key=lambda x:x[1], reverse = True)  
            coollist = [k for k, v in cool.items() if v > 0]           
            pendinglist2 = [k[0] for k in pendings if (k[0] not in coollist) and d[k[0]] >0]
            task = None
            if len(pendinglist2) >0:
                task = pendinglist2[0]
                d[task] = d[task] -1
                cool[task] = n+1
                tasksn  = tasksn -1
            t = t +1
            #print pendings, task
            for i in cool:
                cool[i] = max(0, cool[i]-1)
        #print q.items
        return t