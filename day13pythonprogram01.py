##inpL=['apple','mango','guava']
##res_inpL=list(map(len,inpL))
##print(res_inpL)


inp=input()
temp=inp.split()
ans=[len(i)for i in temp]
print(*ans)
