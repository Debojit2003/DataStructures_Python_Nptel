def gcd(m,n):
	#Assume m >= n
	if(m<n):
		(m,n) = (n,m)
	if(m%n) == 0:
		return n
	else:
		diff = m-n
		#diff > n? possible!
	return(gcd(max(n,diff),min(n,diff)))

m=int(input("Enter the value of m: "))
n=int(input("Enter the value of n: "))

print("The gcd is: "+str(gcd(m,n)))
