def factorial(n):
    """Calculate the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def permutation(n, r):
    """Calculate the permutation of n items taken r at a time.
    Formula: P(n,r) = n!/(n-r)!
    """
    if n < r:
        raise ValueError("n must be greater than or equal to r")
    if n < 0 or r < 0:
        raise ValueError("n and r must be non-negative")
    
    return factorial(n) // factorial(n - r)

# Example usage
if __name__ == "__main__":
    try:
        n = int(input("Enter the total number of items (n): "))
        r = int(input("Enter the number of items to arrange (r): "))
        
        result = permutation(n, r)
        print(f"The number of permutations P({n},{r}) is: {result}")
        
    except ValueError as e:
        print(f"Error: {e}")