def count_spchar(s):
    spchar=0
    for i in s:
        if i in'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwyz':
            spchar+=1
    return spchar
str1=input()
a=count_spchar(str1)
print("No of special character in:",str1,"' is",a)
 
