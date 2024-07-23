def f(n): 
    s=0
    for i in range(1,n+1):
        if n//i == i and n%i == 0:
           s = 1
    return(s%2 == 1)

#n=3
#n = 5
#n = 16
n = 6
print("The value is: "+str(f(n)))
