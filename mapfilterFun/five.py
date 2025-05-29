""" numbers=[78,45,67,87,98,10]
def even_numbers(num):
    return num%2 ==0

even_numbers=list(filter(even_numbers,numbers))
print(numbers)
print(even_numbers) """


numbers=[78,45,67,87,98,10]
even_numbers=list(filter(lambda num:num%2 ==0,numbers))
print(even_numbers)