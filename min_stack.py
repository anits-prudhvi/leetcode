class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.len = -1

    def push(self, x: int) -> None:
        if self.len == -1:
            self.stack.append([x,x])
        else:
            self.stack.append([x,min(x,self.stack[self.len][1])])
        self.len += 1

    def pop(self) -> None:
        del self.stack[self.len]
        self.len -= 1

    def top(self) -> int:
        return self.stack[self.len][0]

    def getMin(self) -> int:
        return self.stack[self.len][1]


inp1=["MinStack","push","push","push","getMin","pop","top","getMin"]
inp2=[[],[-2],[0],[-3],[],[],[],[]]

stack = None
for i,j in zip(inp1,inp2):
    #print(i)
    if i == "MinStack":
        stack = MinStack()
    if i == "push":
        stack.push(j[0])
    if i == "pop":
        stack.pop()
    if i == "getMin":
        print(stack.getMin())
    if i == "top":
        print(stack.top())
