

try:
    first_number = input("Enter first number: ")  
    result = 10/first_number            
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("Invalid Input")   
except TypeError:
    print("Type Error")                                                   
except Exception as e:
     print("Exception raised ", e)
     print("Exception type ", type(e))
else:
    print("No exception occurred")
finally:
    print("Finally block is always executed")    
print("This is the end of the program")
