def count_spchar(s):
    spchar=0
    temp='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwyz0123456789'
    for i in s:
        if i not in temp:
            spchar+=1
    return spchar
str1=input()
a=count_spchar(str1)
print("No of special character in:",str1,"' is",a)
 