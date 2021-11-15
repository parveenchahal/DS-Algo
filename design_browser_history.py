# https://leetcode.com/problems/design-browser-history/


class BrowserHistory:

    def __init__(self, homepage: str):
        self._back_history = [homepage]
        self._forward_history = []
        
    def visit(self, url: str) -> None:
        self._back_history.append(url)
        self._forward_history = []
        
    def back(self, steps: int) -> str:
        for _ in range(steps):
            if len(self._back_history) <= 1:
                break
            self._forward_history.append(self._back_history.pop())
        return self._back_history[-1]
        
    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if len(self._forward_history) <= 0:
                break
            self._back_history.append(self._forward_history.pop())
        return self._back_history[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
