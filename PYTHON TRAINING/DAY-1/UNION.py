# Demonstrate different ways to perform unions in Python using sets

# Create two sample sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Method 1: Using the union() method
union_result1 = set1.union(set2)
print("Union using union() method:", union_result1)

# Method 2: Using the | operator
union_result2 = set1 | set2
print("Union using | operator:", union_result2)