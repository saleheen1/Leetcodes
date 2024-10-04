class MinStack:

    def __init__(self):
        self.stack = []
        self.mStack = []
        

    def push(self, val):
        self.stack.append(val)

        if not self.mStack:
            self.mStack.append(val)
        else:
            lastMStackValue = self.mStack[-1]
            minValue = min(lastMStackValue, val)
            self.mStack.append(minValue)

        

    def pop(self):
        self.stack.pop()
        self.mStack.pop()
        

    def top(self):
      return  self.stack[-1]
        

    def getMin(self):
     return self.mStack[-1]
