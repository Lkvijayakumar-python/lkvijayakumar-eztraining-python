n = input()
l =(len(n))

b= 0

for i in range(l):
    k = int(n[i])
    a = k**2
    b = b+a
    if b == 1:
        print("happy number")
        break
    else:
        a1 = 0
        c = str(b)
        d = len(c)
        for i in range(d):
            if b!=0:
                e = int(c[i])
                f = e**2
                g = a1 + f
                print(g)
            

        
   
    
    
