class Interpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, code):
        tokens = code.split()
        if len(tokens) < 3:
            raise SyntaxError("Invalid syntax")

        if tokens[1] != "=":
            raise SyntaxError("Invalid assignment")

        variable = tokens[0]
        operator = tokens[2]
        value = int(tokens[3])

        if operator == "+":
            self.variables[variable] = self.variables.get(variable, 0) + value
        elif operator == "-":
            self.variables[variable] = self.variables.get(variable, 0) - value
        elif operator == "*":
            self.variables[variable] = self.variables.get(variable, 0) * value
        elif operator == "/":
            self.variables[variable] = self.variables.get(variable, 0) / value
        else:
            raise SyntaxError("Invalid operator")

        return self.variables[variable]
 

interpreter = Interpreter()
code = input("Enter code: ")
result = interpreter.interpret(code)
print("Result:", result)

