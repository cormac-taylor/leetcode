from typing import List

class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        len = 0

        for t in tokens:
            if t == "+" or t == "-" or t == "*" or t == "/":
                res = 0
                
                temp = stack.pop()
                if t == "+":
                    res = stack.pop() + temp
                elif t == "-":
                    res = stack.pop() - temp
                elif t == "*":
                    res = stack.pop() * temp
                else:
                    res = int(stack.pop() / temp)                    
                len -= 2

                stack.insert(len, res)
            else:
                stack.insert(len, int(t))
            len += 1
        return stack.pop()
