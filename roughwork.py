def sqrt(x):
    """
    A function to calculate the square root of a number x:
    """
    # Initial guess for the square root z:
    z = x / 2
    # Loop until we're happy with the accuracy.
    while abs(x - (z * z)) > 0.000001:
        # Calculate a better guess for the square root.
        z -= (z*z - x) / (2 * z)
    # Return the approximate square root of x.
    return (z)
# Show the square root of 2
r = sqrt(2.0)

print(f'{r:.100f}')