def count_constant(s):
    constant=0
    for i in s:
        if i in 'bcdfghjklmnpqrstvwxyz':
            constant=1
    return constant
str1=input()
a=count_constant(str1)
print("No of constants in:",str1,"' is",a)
 
