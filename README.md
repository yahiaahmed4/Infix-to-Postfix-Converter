# Infix to Postfix Converter

This Python script converts infix expressions to postfix notation and evaluates the resulting postfix expression.

## Overview

The script implements the Shunting Yard algorithm for converting infix expressions to postfix notation. It then evaluates the postfix expression using a stack-based approach.

## Functions

### 1. `precedence(operator)`

This function returns the precedence of an operator according to the following dictionary:

```python
precedence_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
```

### 2. `infix_to_postfix(infix_expression)`

This function takes an infix expression as input and returns the equivalent postfix expression. It also provides step-by-step transformation details in the form of postfix steps.

### 3. `evaluate_postfix(postfix_expression)`

This function evaluates the given postfix expression and returns the result. It also provides step-by-step evaluation details, including the stack status and operations performed.

### 4. `main()`

This function serves as the entry point of the script. It takes user input for an infix expression, converts it to postfix notation, evaluates it, and displays the result along with the transformation and evaluation steps.

## Usage

1. Run the script.
2. Enter an infix expression when prompted.
3. The script will convert the infix expression to postfix notation and evaluate it.
4. It will display the postfix expression, step-by-step transformation, and evaluation details, including the final result.

## Note

- The script handles basic arithmetic operators: `+`, `-`, `*`, `/`, and `^` (exponentiation).
- Parentheses `(` and `)` are supported for grouping expressions.
- Division by zero is not allowed and will raise an error.

--- 
