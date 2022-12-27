string='''practice problems for list.'''
ans=[]
for i in string:
    if i not in 'AEIOUaeiou':
        ans.append(i)
print(*ans)
        
