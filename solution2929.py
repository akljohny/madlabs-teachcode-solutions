d = {}
x = int(input())
for i in range(x):
	a = input().split()
	d[a[0]] = sum(map(float,a[1:]))/3
print ('%.2f' % d[input()])
