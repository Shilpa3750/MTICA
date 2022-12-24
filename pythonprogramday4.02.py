'''student=[[44,'prasad',75,87],[13,'gangully',82,79],[53,'sashikala',72,80],[35,'monohar',86,85]]
student.sort()
print(student)
student.sort(key=lambda temp:temp[2])
print(student)
student.sort(key=lambda temp:temp[3])
print(student)
'''
def greet(inpstr):
    inpstr=input("Enter your name:")
    outstr="hello"+""+inpstr
    print(outstr)
    greet()
    
