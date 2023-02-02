n=int(input("enter a number:"))
for i in range(1,n+1):
    if i==n:
        print("* "*i)
    elif i==1:
        spaces=" "*(n-i)
        stars="* "*i
        print(spaces+stars)
    else:
        spaces=" "*(n-i)
        hallow_spaces="  "*(i-2)
        print(spaces+"* "+hallow_spaces+"* ")

