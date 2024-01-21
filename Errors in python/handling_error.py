def division(num,denum):
    try :
        result = num / denum
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")


division(10,0)