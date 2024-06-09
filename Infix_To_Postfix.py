def precedence(operator):
    precedence_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    return precedence_dict.get(operator, 0)

def infix_to_postfix(infix_expression):
    output = []
    operator_stack = []
    postfix_steps = []  # To keep track of the steps in transformation to postfix

    for token in infix_expression.split():
        if token.isnumeric():  # Operand
            output.append(token)
        elif token in {'+', '-', '*', '/', '^'}:  # Operator
            while operator_stack and precedence(operator_stack[-1]) >= precedence(token):
                output.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':  # Left parenthesis
            operator_stack.append(token)
        elif token == ')':  # Right parenthesis
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()  # Remove the corresponding left parenthesis

        postfix_steps.append(f"Step {len(postfix_steps) + 1}: {' '.join(output)} {' '.join(operator_stack)}")

    while operator_stack:
        output.append(operator_stack.pop())

    postfix_steps.append(f"Step {len(postfix_steps) + 1}: {' '.join(output)}")

    return ' '.join(output), postfix_steps

def evaluate_postfix(postfix_expression):
    operand_stack = []
    stack_history = []  # To keep track of the stack and operations at each step

    for token in postfix_expression.split():
        if token.isnumeric():
            operand_stack.append(int(token))
            stack_history.append((list(operand_stack), f"Pushed {token} to stack"))
        else:
            if len(operand_stack) < 2:
                raise ValueError("Invalid postfix expression: Not enough operands.")
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()

            if token == '+':
                result = operand1 + operand2
                operation = f"Addition: {operand1} + {operand2}"
            elif token == '-':
                result = operand1 - operand2
                operation = f"Subtraction: {operand1} - {operand2}"
            elif token == '*':
                result = operand1 * operand2
                operation = f"Multiplication: {operand1} * {operand2}"
            elif token == '/':
                if operand2 == 0:
                    raise ValueError("Division by zero is not allowed.")
                result = operand1 / operand2
                operation = f"Division: {operand1} / {operand2}"
            elif token == '^':
                result = operand1 ** operand2
                operation = f"Exponentiation: {operand1} ^ {operand2}"
            else:
                raise ValueError(f"Unknown operator: {token}")

            operand_stack.append(result)
            stack_history.append((list(operand_stack), operation))

    if len(operand_stack) != 1:
        raise ValueError("Invalid postfix expression: Too many operands.")

    return operand_stack.pop(), stack_history

def main():
    infix_expression = input("Enter the infix expression: ")
    try:
        postfix_expression, postfix_steps = infix_to_postfix(infix_expression)
        

        print("\nStep-by-step transformation to postfix:")
        for step in postfix_steps:
            print(step)
        print("Postfix expression:", postfix_expression)
        result, evaluation_steps = evaluate_postfix(postfix_expression)  # Get the result and evaluation steps

        print("\nStep-by-step evaluation:")
        for idx, (stack, operation) in enumerate(evaluation_steps):
            formatted_stack = ' '.join(str(item) if isinstance(item, int) else item for item in stack)
            print(f"Step {idx + 1}: Stack = [{formatted_stack}], Operation = {operation}")

        print("\nFinal Result:", result)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
