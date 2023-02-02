a=input("enter a string:").split( )
b=input("enter a character:")
for i in  range(len(a)):
    if b==a[i]:
        print("char is there")
    else:
        print("character is not there")
