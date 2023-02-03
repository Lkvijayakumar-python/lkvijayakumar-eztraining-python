def factors():
    for i in range(1,n+1):
        n=int(input("enter a number: "))
        if n%i==0:
            return(i)
i=factors()
print(i)
