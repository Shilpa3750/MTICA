num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))

try:
    res=(num1)/ int(num2)
except ZeroDivisionError:
    print("Exception handled by silpa")
except ValueError:
    print("Exception handled by nithya")
except Exception as ob:
    print(ob)
else:
    print(num1,'/',num2,'=',res)
finally:
    print("Thanks")
    
print("Visit again at python class at MTICA") 
