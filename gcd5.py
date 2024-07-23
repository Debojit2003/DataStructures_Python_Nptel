def gcd(m,n):
	if m<n:
		(m,n)=(n,m)
	if(m%n)==0:
		return n

	else:
		return(gcd(n,m%n))

m=int(input("Enter the value of m: "))
n=int(input("Enter the value of n: "))

print("The gcd of "+str(m)+" and "+str(n)+" is: "+str(gcd(m,n)))
