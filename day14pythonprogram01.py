##def solveproblems(s):
##    list=s.split()
##    return [len(i)for i in lst]
##inp=input()
##solveproblems={i:i[::-1]for i in list}
##print(*solvsproblems(inp))
##

def reverseString(s):
    ans=[i[::-1]for i in s]
    ans=[len(i)for i in s]
    return ans
inp=input().split()
print(inp)
print(reverseString(inp))

