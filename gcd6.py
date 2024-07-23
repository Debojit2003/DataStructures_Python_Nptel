def gcd(m,n):
	if m<n:
		(m,n)=(n,m)
	while (m%n)!=0:
		(m,n)=(n,m%n)

	return n

m=int(input("Enter the value of m: "))
n=int(input("Enter the value of n: "))

print("The gcd of the values are: "+str(gcd(m,n)))