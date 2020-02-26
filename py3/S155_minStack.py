'''
155. Min Stack
Easy

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.internal = []      #main stack, stores element
        self.fmin=[]            #min function stack, fmin(top) == min(self.internal), store the cached minimal of current snapshot of the internal stack
        

    def push(self, x: int) -> None:
        self.internal += [x]
        if len(self.fmin) == 0 or x <= self.fmin[-1]:       # only store fmin when "x <= fmin(top)", pay attention to "less equal", 可用于max情况
            self.fmin += [x]

    def pop(self) -> None:
        top = self.internal.pop()
        if top == self.fmin[-1]:
            self.fmin.pop()
        

    def top(self) -> int:
        return self.internal[-1] if self.internal else None

    def getMin(self) -> int:
        return self.fmin[-1] if self.fmin else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

