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

"""
Explanation:

1. Define a function named square_sum. 

2. Initialize a variable:

total = 0: This variable will hold the sum of the squares.

3. Iterate through each number in the list:

for number in numbers: Loop through each number in the input list numbers.

4. Square each number and add it to the total:

total += number ** 2: Square the current number (number ** 2) and add it to the total.
Return the total sum:

return total: After the loop finishes, return the total which now contains the sum of the squares of the numbers.
"""

# Example usage
if __name__ == "__main__":
    example_list = [1, 2, 2]
    result = square_sum(example_list)
    print(f"The square sum of {example_list} is {result}")

# Source: CodeWars
