varOne = int(input())
varTwo = int(input())
for n in range(varOne,varTwo):
	prime = 0
	if n==1:
		continue
	else:
		for i in range(2,n):
			if n % i == 0:
				prime = 1
		if prime==0:
			print(n)
