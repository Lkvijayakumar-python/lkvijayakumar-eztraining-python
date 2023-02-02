a,b=int(input("enter a number a:")),int(input("enter a number b:"))
if a and b <=15:
    c=a&b
    d=a|b
    e=a^b
    print("Bitwise AND operator is:",c)
    print("Bitwise OR operator is:",d)
    print("Bitwise XOR operator is:",e)
else:
    print("number is out of range") 
