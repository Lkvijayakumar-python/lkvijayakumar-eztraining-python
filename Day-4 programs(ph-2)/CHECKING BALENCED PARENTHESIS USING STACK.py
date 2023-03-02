# CHECKING BALENCED PARENTHESIS USING STACK
s = input()
st = []
balanced = True
for char in s:
    if (char=='{' or char=='[' or char == '('):
        st.append(char)
    elif(char==')'):
        if (len(st) and st.pop()!='('):
            balanced = False
            break
    elif(char=='}'):
        if (len(st) and st.pop()!='{'):
            balanced = False
            break
    elif(char==']'):
        if (len(st) and st.pop()!='['):
            balanced = False
            break
    else:
        balanced = False
        break

if (balanced==False or len(st)):
    print("Not balanced")
else:
    print("Balanced")
        
