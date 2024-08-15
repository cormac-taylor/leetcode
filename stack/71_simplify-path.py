class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def simplifyPath(self, path: str) -> str:
        items = path.split("/")
        stack = []
        for item in items:
            if item == "" or item == ".":
                continue
            elif item == "..":
                if stack != []:
                    stack.pop()
            else:
                stack.append(item)
        return "/" + "/".join(stack)
