"""
https://leetcode.com/problems/implement-stack-using-queues/description/
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.

"""
class MyStack(object):

    def __init__(self):
        self.items = []
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.items.append(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.items.pop()
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.items[len(self.items)-1]
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.items) ==0