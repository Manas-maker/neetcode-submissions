class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        vals = []
        operators = {"+", "/", "*", "-"}
        for i in tokens:
            if i in operators:
                num2 = vals.pop()
                num1 = vals.pop()
                if i != "/":
                    vals.append(str(eval(num1 + i + num2)))
                else:
                    vals.append(str(int(int(num1)/int(num2))))
            else:
                vals.append(i)
        return int(vals[0])