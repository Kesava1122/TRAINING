def calculate_conditional_probability(event_a, event_b, total_outcomes):
    """
    Calculate P(A|B) - Probability of A given B
    Formula: P(A|B) = P(A and B) / P(B)
    """
    # Calculate intersection of A and B
    intersection_a_b = len(set(event_a) & set(event_b))
    
    # Calculate probability of B
    prob_b = len(event_b) / total_outcomes
    
    # Calculate conditional probability
    if prob_b == 0:
        return 0
    
    conditional_prob = (intersection_a_b / total_outcomes) / prob_b
    return conditional_prob

def main():
    # Example usage
    print("Conditional Probability Calculator")
    print("--------------------------------")
    
    # Sample data: Rolling two dice
    total_outcomes = 36  # 6 x 6 possible outcomes
    
    # Event A: Sum is greater than 7
    event_a = [(i, j) for i in range(1, 7) for j in range(1, 7) if i + j > 7]
    
    # Event B: First die is 4
    event_b = [(4, j) for j in range(1, 7)]
    
    # Calculate P(A|B)
    result = calculate_conditional_probability(event_a, event_b, total_outcomes)
    
    print(f"\nExample: Rolling two dice")
    print(f"Event A: Sum is greater than 7")
    print(f"Event B: First die is 4")
    print(f"\nP(A|B) = {result:.3f}")
    print(f"This means the probability of getting a sum greater than 7,")
    print(f"given that the first die shows 4, is {result:.1%}")

if __name__ == "__main__":
    main()