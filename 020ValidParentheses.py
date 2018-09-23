class Stack():
    def __init__(self):
        self.items = []
    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()
    def push(self, item):
        self.items.append(item)
    def size(self):
        return len(self.items)


        
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d_c = {}
        d_c[")"] = "("
        d_c["}"] = "{"
        d_c["]"] = "["
        st = Stack()
        for i in s:
            if i in d_c.keys():
                if st.pop() != d_c[i]:
                    return False
            else:
                st.push(i)

        return st.size() == 0
