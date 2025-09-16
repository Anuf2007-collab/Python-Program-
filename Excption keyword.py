try:
    n1=int(input("enter a number:"))
    n2=int(input("enter a number:"))
    result=n1/n2
    print(result)
except ZeroDivisionError:
    print("you can't divide by zero")
except ValueError:
    print("enter a valid integer")
except NameError:
    print("u have used a variable which is not defined")
except TypeError:
    print("invalid input")
finally:
    print("program completed")