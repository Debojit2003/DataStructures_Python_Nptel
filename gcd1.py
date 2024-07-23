def gcd(m, n):
    # Initialize list to store common factors
    cf = []

    # Find common factors
    for i in range(1, min(m, n) + 1):
        if m % i == 0 and n % i == 0:
            cf.append(i)

    # Return the greatest common factor
    return cf[-1] if cf else None

# Take user input
m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

# Calculate and print the GCD
print("The GCD is: " + str(gcd(m, n)))
