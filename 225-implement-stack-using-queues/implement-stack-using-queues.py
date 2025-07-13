from collections import deque

'''
We are using q1 as the main stack —
it always holds the current stack elements in correct order (top at front).
During push(x), we temporarily use q2 to rearrange elements.
'''

class MyStack:
    # This is a push-costly approach where push will have O(n) time,
    # and pop and top will have O(1) time.

    def __init__(self):
        self.q1 = deque()  # main queue that always has the top element at q1[0]
        self.q2 = deque()  # helper queue used during the push operation

    def push(self, x: int) -> None:
        self.q2.append(x)  # append to helper queue first

        # Move all elements from q1 to q2 to maintain stack order
        while self.q1:
            self.q2.append(self.q1.popleft())  # transfer elements from main to helper

        '''
        We swap so that:
        - q1 always contains the current valid stack
        - q2 becomes empty and ready for the next operation
        '''
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()  # remove and return the top element (front of q1)

    def top(self) -> int:
        return self.q1[0]  # return the top element without removing it

    def empty(self) -> bool:
        return not self.q1  # return True if q1 is empty, False otherwise


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
