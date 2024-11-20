def calculate_dependent_probability():
    # Get the first event probability
    prob_A = float(input("Enter the probability of first event (between 0 and 1): "))
    
    # Get the conditional probability of second event
    prob_B_given_A = float(input("Enter the probability of second event given first event occurred: "))
    
    # Calculate the dependent probability (P(A and B) = P(A) × P(B|A))
    dependent_prob = prob_A * prob_B_given_A
    
    # Display results
    print("\nResults:")
    print(f"Probability of first event (P(A)): {prob_A}")
    print(f"Probability of second event given first event (P(B|A)): {prob_B_given_A}")
    print(f"Probability of both events occurring (P(A and B)): {dependent_prob}")

# Main program
if __name__ == "__main__":
    print("Dependent Probability Calculator")
    print("-------------------------------")
    
    try:
        calculate_dependent_probability()
    except ValueError:
        print("Please enter valid numerical probabilities between 0 and 1")