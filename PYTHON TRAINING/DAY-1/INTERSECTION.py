def find_intersection(list1, list2):
    """
    Find the intersection of two lists.
    Returns a list containing elements present in both lists.
    """
    return list(set(list1) & set(list2))

# Example usage
if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    result = find_intersection(list1, list2)
    print(f"Intersection of {list1} and {list2} is: {result}")