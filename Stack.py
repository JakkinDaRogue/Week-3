class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list_x = []

    def addList(self, list):
        


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.list_x.append([x])

    def pop(self):

        pop = self.list_x[len(self.list_x) - 1]
        self.list_x = self.list_x[0 : (len(self.list_x)) - 1]
        return pop

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        pop = self.list_x[len(self.list_x) - 1]
        return pop


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.list_x) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
x = 15, 14, 13, 12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1
obj.push(x)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()

obj.peek()
print(obj.list_x)
obj.pop()
print(obj.list_x)
obj.pop()
print(obj.list_x)
obj.pop()
print(obj.list_x)
obj.pop()
print(obj.list_x)
obj.peek()
print(obj.list_x)
obj.empty()
print(obj.list_x)
