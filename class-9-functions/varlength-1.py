def sum_all(*args):
    """Function to sum any number of arguments."""
    total = 0
    for num in args:
        total = total+num
    return total

print("Sum of 1, 2, 3:", sum_all(1, 2, 3))
print("Sum of 5, 10, 15, 20:", sum_all(5, 10, 15, 20))
print("Sum of no arguments:", sum_all())