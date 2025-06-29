from enum import Enum

class Operation(Enum):
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4

def calculate(a, b, operation):
    if operation == Operation.ADD:
        return a + b
    elif operation == Operation.SUBTRACT:
        return a - b
    elif operation == Operation.MULTIPLY:
        return a * b
    elif operation == Operation.DIVIDE:
        if b != 0:
            return a / b
        else:
            return "❌ Cannot divide by zero!"
    else:
        return "Unknown operation"

# Example usage
print("Result:", calculate(10, 5, Operation.ADD))       # 15
print("Result:", calculate(10, 5, Operation.SUBTRACT))  # 5
print("Result:", calculate(10, 5, Operation.MULTIPLY))  # 50
print("Result:", calculate(10, 0, Operation.DIVIDE))    # Cannot divide by zero!
