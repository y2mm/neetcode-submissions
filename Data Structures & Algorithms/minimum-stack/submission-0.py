class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        if self.minstack:
            if self.minstack[-1] >= val:
                self.minstack.append(val) 
        else:
            self.minstack.append(val)
        self.stack.append(val)


    def pop(self) -> None:
        if self.minstack:
            if self.stack[-1] == self.minstack[-1]:
                self.minstack.pop()

        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]

        
