word=input("enter a word:")
l=['a','e','i','o','u','A','E','I','O','U']
count=0
for i in word:
    if i in l:
        count=count+1
print(count)
