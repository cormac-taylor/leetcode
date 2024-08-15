class MinStack:

    """
    Time complexity: O(1)
    Space complexity: O(1)
    """
    def __init__(self):
        self.lastIndex = -1
        self.stack = []
        self.minStack = []

    """
    Time complexity: O(1)
    Space complexity: O(1)
    """
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.lastIndex == -1:
            self.minStack.append(val)
        else:
            self.minStack.append(min(self.getMin(), val))
        self.lastIndex += 1

    """
    Time complexity: O(1)
    Space complexity: O(1)
    """
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        self.lastIndex -= 1

    """
    Time complexity: O(1)
    Space complexity: O(1)
    """
    def top(self) -> int:
        return self.stack[self.lastIndex]
    
    """
    Time complexity: O(1)
    Space complexity: O(1)
    """
    def getMin(self) -> int:
        return self.minStack[self.lastIndex]
