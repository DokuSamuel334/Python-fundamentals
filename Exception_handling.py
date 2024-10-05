try :
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number : "))
    result = num1/num2
    print(f"results is {result}")
except ZeroDivisionError :
    print(f"Error cant divide by zero")
except ValueError :
    print(f"Error cant divide by a value or string")
finally:
    print(f"Well done or opertion complete")

