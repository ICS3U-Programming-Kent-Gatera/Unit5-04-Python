#!/usr/bin/env python3
# Created By: Kent Gatera
# Date: 10.26.22
# Does basic math operations using operation signs and user input.


def calculate(a: float, b: float, sign: str) -> float:

    # Using a switch case to separate all the equations.
    if sign == "+":
        sum_num = a + b
        return sum_num
    elif sign == "-":
        difference_num = a - b
        return difference_num
    elif sign == "/":
        quot_num = a / b
        return quot_num
    elif sign == "*":
        prod_num = a * b
        return prod_num
    elif sign == "%":
        modNum = a % b
        return modNum


def main():
    # Telling the type of operation we can do.
    oper_sign = str(input("Pick an operation sign (+, -, *, /, %) : "))
    # Error checking...
    try:
        user_num1 = float(input("What is the first number?: "))
        user_num2 = float(
            input("What is the second number?: ")
        )  #  Calling the calcNum function.
        ans_num = calculate(sign=oper_sign, a=user_num1, b=user_num2)

        # Output of every case/ operation.
        if oper_sign == "+":
            print(f"The sum of {user_num1} and {user_num2} is {ans_num}")
        elif oper_sign == "-":
            print(f"The difference of {user_num1} and {user_num2} is {ans_num}")
        elif oper_sign == "/":
            print(f"{user_num1} divided by {user_num2} is {ans_num}.")
        elif oper_sign == "*":
            print(f"{user_num1} multiplied by {user_num2} is {ans_num}.")
        elif oper_sign == "%":
            print(f"{user_num1} modulus by {user_num2} is {ans_num}.")
        # Error checking for the operation sign.
        else:
            print("Invalid operation sign.")
    except:
        print("Invalid number.")


# Running the main Function.
if __name__ == "__main__":
    main()
