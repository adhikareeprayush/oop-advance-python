import argparse


# does the math based on the operation passed from command line
def calculate(number1, number2, operation):
    if operation == "add":
        return number1 + number2
    elif operation == "subtract":
        return number1 - number2
    elif operation == "multiply":
        return number1 * number2
    else:
        return "Unsupported operation"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple CLI Calculator")
    parser.add_argument("--number1", help="First number", type=float, default=10)
    parser.add_argument("--number2", help="Second number", type=float, default=5)
    parser.add_argument("--operation", help="Operation (add, subtract, multiply)", default="add")

    args = parser.parse_args()
    result = calculate(args.number1, args.number2, args.operation)
    print(f"Result of {args.operation}({args.number1}, {args.number2}) = {result}")
