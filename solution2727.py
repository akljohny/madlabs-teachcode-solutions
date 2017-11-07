var = []
x = int(input())
for i in range(x):
    s = input().split()
    for i in range(1,len(s)):
        s[i] = int(s[i])
        
    if s[0] == "append":
        var.append(s[1])
    elif s[0] == "extend":
        var.extend(s[1:])
    elif s[0] == "insert":
        var.insert(s[1],s[2])
    elif s[0] == "remove":
        var.remove(s[1])
    elif s[0] == "pop":
        var.pop()
    elif s[0] == "index":
        print(var.index(s[1]))
    elif s[0] == "count":
        print(var.count(s[1]))
    elif s[0] == "sort":
        var.sort()
    elif s[0] == "reverse":
        var.reverse()
    elif s[0] == "print":
        print(var)
