def extract_constant(s):
    constant=0
    for i in s:
        if i in 'bcdfghjklmnpqrstvwxyz':
            constant=1
    return constant
str1=input()
a=extract_constant(str1)
print("No of constants in:",str1,"' is",a)
 
