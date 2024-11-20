def calculate_probability(favorable_outcomes, total_outcomes):
    """
    Calculate the probability of an event occurring
    
    Args:
        favorable_outcomes (int): Number of favorable outcomes
        total_outcomes (int): Total number of possible outcomes
    
    Returns:
        float: Probability as a decimal between 0 and 1
    """
    if total_outcomes <= 0:
        raise ValueError("Total outcomes must be greater than 0")
    
    return favorable_outcomes / total_outcomes

def main():
    try:
        # Get user input
        favorable = int(input("Enter the number of favorable outcomes: "))
        total = int(input("Enter the total number of possible outcomes: "))
        
        # Calculate probability
        probability = calculate_probability(favorable, total)
        
        # Display results
        print(f"\nProbability: {probability:.4f}")
        print(f"Percentage: {probability * 100:.2f}%")
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()