def gcd(m,n):
	i = min(m,n)
	while i>0 :
		if m%i == 0 and n%i == 0:
			return (i)
		else:
			i=i-1

m=int(input("Enter the value of m: "))
n=int(input("Enter the value of n: "))

print("The gcd is: "+str(gcd(m,n)))