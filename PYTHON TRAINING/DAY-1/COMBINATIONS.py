def factorial(n):
    """Calculate factorial of a number"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def combination(n, r):
    """Calculate combination (nCr) - number of ways to choose r items from n items"""
    if n < r:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))

def main():
    # Example usage
    try:
        n = int(input("Enter the total number of items (n): "))
        r = int(input("Enter the number of items to choose (r): "))
        
        result = combination(n, r)
        print(f"\nNumber of combinations C({n},{r}) = {result}")
        
    except ValueError:
        print("Please enter valid integer numbers")

if __name__ == "__main__":
    main()