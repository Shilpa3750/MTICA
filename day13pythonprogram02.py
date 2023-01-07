##inp=input()
##temp=inp.split()
##ans=[len(i)for i in temp]
##print(*ans)


def solveproblem(s):
    lst=s.split()
    return[len(i)for i in lst]

inp=input()
print(*solveproblem(inp))
