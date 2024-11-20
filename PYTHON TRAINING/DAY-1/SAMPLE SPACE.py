def create_sample_space(experiment):
    """
    Creates a sample space for common probability experiments
    
    Args:
        experiment (str): Type of experiment ('coin', 'dice', or 'cards')
    
    Returns:
        list: All possible outcomes in the sample space
    """
    if experiment.lower() == 'coin':
        return ['Heads', 'Tails']
    
    elif experiment.lower() == 'dice':
        return list(range(1, 7))  # Returns [1, 2, 3, 4, 5, 6]
    
    elif experiment.lower() == 'cards':
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        return [f'{rank} of {suit}' for rank in ranks for suit in suits]
    
    else:
        return []

# Example usage
if __name__ == "__main__":
    # Try different experiments
    print("Coin flip outcomes:", create_sample_space('coin'))
    print("Dice roll outcomes:", create_sample_space('dice'))
    print("First 5 cards in deck:", create_sample_space('cards')[:5])