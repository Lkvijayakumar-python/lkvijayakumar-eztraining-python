
c=10
d=0
try :
    print("resource open")
    print(c/d)
except Exception as e :
    print("don't give second no. as zero",e)
finally :
    print("resource closed")
