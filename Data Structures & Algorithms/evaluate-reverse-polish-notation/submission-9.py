class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        vals = []
        operators = {"+", "/", "*", "-"}
        for i in tokens:
            if i in operators:
                num2 = vals.pop()
                num1 = vals.pop()
                if i == "+":
                    vals.append(num1+num2)
                elif i == "*":
                    vals.append(num1*num2)
                elif i == "-":
                    vals.append(num1-num2)
                elif i == "/":
                    vals.append(int(num1/num2))
            else:
                vals.append(int(i))
        return int(vals[0])