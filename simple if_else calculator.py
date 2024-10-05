# This is a sample Python script.
from jinja2.compiler import operators

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# A SIMPLE PYTHON CALCULATOR
#import maths
first_number= float(input("Please Enter your First Number : "))
operators=input("Please Enter An Operator(- + * ** / %) : ")
second_number= float(input("Please Enter your Second Number : "))
if operators == "-":
    sum = first_number - second_number
    print(f"{sum} is your answer")
elif operators == "+":
    sum = first_number + second_number
    print(f"{sum} is your answer")
elif operators == "*":
    sum = first_number * second_number
    print(f"{sum} is your answer")
elif operators == "**":
    sum = first_number ** second_number
    print(f"{sum} is your answer")
elif operators == "/":
    sum = first_number / second_number
    print(f"{sum} is your answer")
elif operators == "%":
    sum = first_number % second_number
    print(f"{sum} is your answer")
else :
    print(f" Is Not Part Of My Mathematical Formulas")

