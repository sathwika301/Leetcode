class MinStack:

    def __init__(self):
        self.stack=[]
        

    def push(self, value: int) -> None:
       
        if self.stack:
            m=min(self.stack[-1][1],value) 
        else :
            m=value
        self.stack.append((value,m))
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()