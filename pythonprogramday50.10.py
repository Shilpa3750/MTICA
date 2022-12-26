def extractspecialcharacters(s):
    
    for i in s:
        if i in '012345789':
            extract_digit+=1
    return extract_digit
str1=input()
a=extract_digits(str1)
print("No of digit in:",str1,"' is",a)
 
