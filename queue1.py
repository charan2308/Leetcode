class MyQueue:

    def __init__(self):
        self.mylist=[]
    def push(self, x: int) -> None:
        self.mylist.append(x)

    def pop(self) -> int:
        p=self.mylist[0]
        self.mylist=self.mylist[1:]
        return p
    
    def peek(self) -> int:
        return self.mylist[0]

    def empty(self) -> bool:
        if self.mylist:
            return False
        else:
            return True
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()