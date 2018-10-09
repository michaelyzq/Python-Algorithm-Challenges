"""
https://leetcode.com/problems/implement-queue-using-stacks/description/
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
"""
class MyQueue(object):

    def __init__(self):
        self.queue = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.queue.pop(0)
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.queue) == 0
        