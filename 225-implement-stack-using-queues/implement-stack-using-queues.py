from collections import deque 
class MyStack:

    def __init__(self):
        self.q=deque()

    def push(self, x: int) -> None:
        self.q.append(x)
    # This is a push-costly approach using only one queue.
    # After each push, we rotate the queue to place the newest element at the front.
        
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        '''
        After rotation:
        - The most recently added element becomes the front of the queue.
        - So it behaves like the top of a stack.
        '''

    def pop(self) -> int:
        return self.q.popleft()
        

    def top(self) -> int:
        return self.q[0]
        

    def empty(self) -> bool:
        return not self.q
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()