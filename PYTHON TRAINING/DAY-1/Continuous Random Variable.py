import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def calculate_probability(mean, std_dev, lower_bound, upper_bound):
    """
    Calculate probability between two numbers in a normal distribution
    """
    # Calculate the probability using cumulative distribution function (CDF)
    prob = norm.cdf(upper_bound, mean, std_dev) - norm.cdf(lower_bound, mean, std_dev)
    return prob

def plot_distribution(mean, std_dev, lower_bound, upper_bound):
    """
    Plot the normal distribution and shade the area between bounds
    """
    x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
    y = norm.pdf(x, mean, std_dev)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', label='Normal Distribution')
    
    # Shade the area between bounds
    x_shade = np.linspace(lower_bound, upper_bound, 100)
    y_shade = norm.pdf(x_shade, mean, std_dev)
    plt.fill_between(x_shade, y_shade, color='red', alpha=0.3)
    
    plt.title(f'Normal Distribution (μ={mean}, σ={std_dev})')
    plt.xlabel('Value')
    plt.ylabel('Probability Density')
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    # Get user input
    mean = float(input("Enter the mean (μ): "))
    std_dev = float(input("Enter the standard deviation (σ): "))
    lower_bound = float(input("Enter the lower bound: "))
    upper_bound = float(input("Enter the upper bound: "))
    
    # Calculate probability
    probability = calculate_probability(mean, std_dev, lower_bound, upper_bound)
    print(f"\nProbability between {lower_bound} and {upper_bound}: {probability:.4f}")
    
    # Plot the distribution
    plot_distribution(mean, std_dev, lower_bound, upper_bound)

if __name__ == "__main__":
    main()