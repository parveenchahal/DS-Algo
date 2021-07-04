# https://leetcode.com/problems/min-stack/

class MinStack:
    def __init__(self):
        self.st = []
        self.min = None
        

    def push(self, val: int) -> None:
        if len(self.st) <= 0:
            self.st.append(val)
            self.min = val
            return
        if val >= self.min:
            self.st.append(val)
            return
        self.st.append(2 * val - self.min)
        self.min = val

    def pop(self) -> None:
        if len(self.st) <= 0:
            return
        if self.min < self.st[-1]:
            self.st.pop()
            return
        self.min = self.min * 2 - self.st.pop()

    def top(self) -> int:
        if self.min <= self.st[-1]:
            return self.st[-1]
        return self.min

    def getMin(self) -> int:
        if len(self.st) <= 0:
            return
        return self.min
