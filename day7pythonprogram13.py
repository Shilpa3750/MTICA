dict1={"Sedan":1500,"SUV":2000,"Pickup":2500,"Minivan":1600,
       "Van":13600,"Bicycle": 7,"Motorcycle": 110}
##ans=[]
##for i in dict1:
##    if dict1[i]<5000:
##        ans.append(i.upper())
##print(ans)

ans=[i.upper() for i in dict1 if dict1[i]<5000]
print(ans)
