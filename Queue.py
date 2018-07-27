class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list_x = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.list_x.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        #print(self.list_x[0])
        #return self.list_x[0]
        #self.list_x.remove(self.list_x[0])
        pop = self.list_x[0]
        self.list_x = self.list_x[1:]
        return pop

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        pop = self.list_x[0]
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
obj.push(1)
print(obj.list_x)
obj.push(2)
print(obj.list_x)
obj.push(3)
print(obj.list_x)
obj.push(4)
print(obj.list_x)
obj.push(5)
print(obj.list_x)
obj.push(6)
print(obj.list_x)
obj.push(7)
print(obj.list_x)
obj.push(8)
print(obj.list_x)
obj.push(9)
print(obj.list_x)
obj.push(10)
print(obj.list_x)
obj.push(11)
print(obj.list_x)
obj.push(12)
print(obj.list_x)
obj.push(13)
print(obj.list_x)
obj.push(14)
print(obj.list_x)
obj.push(15)

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
