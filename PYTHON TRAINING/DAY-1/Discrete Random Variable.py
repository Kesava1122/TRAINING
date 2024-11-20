class DiscreteRandomVariable:
    def __init__(self):
        self.outcomes = {}  # Dictionary to store outcomes and their probabilities
        
    def add_outcome(self, value, probability):
        """Add an outcome and its probability to the random variable"""
        if probability < 0 or probability > 1:
            raise ValueError("Probability must be between 0 and 1")
        self.outcomes[value] = probability
        
    def validate_probabilities(self):
        """Check if the sum of all probabilities equals 1"""
        total_prob = sum(self.outcomes.values())
        return abs(total_prob - 1.0) < 1e-9  # Using small epsilon for floating point comparison
    
    def expected_value(self):
        """Calculate the expected value (mean) of the random variable"""
        return sum(value * prob for value, prob in self.outcomes.items())
    
    def variance(self):
        """Calculate the variance of the random variable"""
        mean = self.expected_value()
        return sum(((value - mean) ** 2) * prob for value, prob in self.outcomes.items())
    
    def standard_deviation(self):
        """Calculate the standard deviation of the random variable"""
        return self.variance() ** 0.5

# Example usage
if __name__ == "__main__":
    # Create a discrete random variable (e.g., rolling a fair die)
    die = DiscreteRandomVariable()
    
    # Add outcomes for a fair six-sided die
    for i in range(1, 7):
        die.add_outcome(i, 1/6)
    
    # Verify probabilities sum to 1
    print(f"Probabilities are valid: {die.validate_probabilities()}")
    
    # Calculate statistics
    print(f"Expected Value: {die.expected_value()}")
    print(f"Variance: {die.variance()}")
    print(f"Standard Deviation: {die.standard_deviation()}")