def gcd(m, n):
    # Find factors of m
    fm = []
    for i in range(1, m + 1):
        if m % i == 0:
            fm.append(i)

    # Find factors of n
    fn = []
    for j in range(1, n + 1):
        if n % j == 0:
            fn.append(j)

    # Find common factors
    cf = []
    for f in fm:
        if f in fn:
            cf.append(f)

    # Return the greatest common factor
    return cf[-1] if cf else None

# Take user input
m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))

# Calculate and print the GCD
print("The GCD is: " + str(gcd(m, n)))
