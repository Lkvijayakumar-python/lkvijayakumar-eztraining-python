def lemons():
    n=int(input("enter number of lemons:"))
    if  n==21:
        print("lemons are enough:")
    elif n<21:
        m=21-n
        print(m,"lemons is needed")
    elif n>21:
        o=n-21
        print(o,"lemons is exceeded")
lemons()
    
