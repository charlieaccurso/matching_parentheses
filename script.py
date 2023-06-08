class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        brackets_map = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in '({[':
                stack.append(c)
            elif c in ')}]':
                if not stack or stack[-1] != brackets_map[c]:
                    return False
                stack.pop()

        return not stack
