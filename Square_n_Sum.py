"""
Squares each number in the list and then sums the results together.

Args:
numbers (list of int): A list of integers.

Returns:
int: The sum of the squares of the integers.
    
Example:
>>> square_sum([1, 2, 2])
9
"""

def square_sum(numbers):
    total = 0
    for number in numbers:
        total = total + number **2
    return total
    
# Example usage
if __name__ == "__main__":
    example_list = [1, 2, 2]
    result = square_sum(example_list)
    print(f"The square sum of {example_list} is {result}")

# Source: CodeWars
