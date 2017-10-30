x = input()
y = int(input())
z = int(input())
a = x[y].upper()
b = x[z].lower()
print(a)
print(b)
sum = 0
for counter in x:
  sum +=  ord(counter)
print(sum)
