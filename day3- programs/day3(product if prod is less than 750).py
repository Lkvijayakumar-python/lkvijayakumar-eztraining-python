l=list(map(int,input("enter a number:").split()))
sum=0
prod=1
for i in range(len(l)):
    prod=l[i]*prod
    sum=sum+l[i]
if prod<750:
    print(prod)
else:
    print(sum)
    
