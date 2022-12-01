import operations


def perform_operation_with_two_nums(num1, num2, operation):
    """
    Performs mathematical operations with two numbers

    :param num1: float
    :param num2: float
    :param operation: string
    """
    if operation == "addition":
        return operations.addition(num1, num2)
    if operation == "subtraction":
        return operations.subtraction(num1, num2)
    if operation == "multiplication":
        return operations.multiplication(num1, num2)
    if operation == "division":
        return operations.division(num1, num2)
    if operation == "exponent":
        return operations.exponentiation(num1, num2)
    if operation == "modulo":
        return operations.modulo(num1, num2)
    else:
        raise ValueError("Invalid operation")
