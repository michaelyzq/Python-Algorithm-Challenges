"""
https://leetcode.com/problems/employee-importance/description/
You are given a data structure of employee information, which includes the employee's unique id, his importance value and his direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all his subordinates.

Example 1:
Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
Explanation:
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        items = []
        self.visitids = []
        self.importance =0
        self.employees = employees
        self.ids = [i.id for i in employees]
        if id not in self.ids:
            return  self.importance
        else:
            curr = employees[self.ids.index(id)]
        self.addOrdinates(curr)
        return self.importance
    def addOrdinates(self,curr):
        if curr.id not in self.visitids:
             self.visitids.append(curr.id)
             self.importance =  self.importance + curr.importance
            
        if curr.subordinates != None:
            for i in curr.subordinates:
                self.addOrdinates(self.employees[self.ids.index(i)])
            