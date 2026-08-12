class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack = []
        wild_stack = []
        for i, c in enumerate(s):
            if c == "*": wild_stack.append(("*", i))
            elif c == "(": open_stack.append(("(", i))
            else:
                if len(open_stack)>0: open_stack.pop()
                elif len(wild_stack)>0: wild_stack.pop()
                else: return False
        while open_stack:
            if len(wild_stack)==0: return False
            if wild_stack.pop()[1]<open_stack.pop()[1]: return False

        return True