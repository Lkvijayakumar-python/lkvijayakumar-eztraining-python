a=10
try :
    b=int(input("enter a number:"))
    print("resource open")
    print(a/b)
except ZeroDivisionError as e:
    print("please note number cant be divided by zero")
except ValueError as e:
    print("invalid input",e)
except Exception as e:
    print("other error",e)
finally :
    print("resourse closed")
