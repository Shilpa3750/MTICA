'''def checkArmstrongNumber(num):
     num=str(num)
     n=len(num)
     total=0
     for i in num:
         total+=int(i)**n
         if int(num)==total:
             return 1
         else:
             return 0
inpNum=int(input())
if checkArmstrongNumber(inpNum):
    print("yes")
else:
    print("no")'''
'''def replace1by0(n):
    n=str(n)
    n=n.replace('1','0')
    return n
inp=int(input())
print(replace1by0(inp))'''
def interchange3and5(n):
    n=str(n)
    n=n.replace('3','.')
    n=n.replace('5','3')
    n=n.replace('.','5')
    return n     
inp=int(input())
print(interchange3and5(inp))
