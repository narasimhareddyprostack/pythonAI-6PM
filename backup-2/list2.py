numbers=[10,20,30,40]
#index   0   1  2  3

#read list element- using indexing
print(numbers[0])  #10
print(numbers[1])  #20
print(numbers[2])  #30
print(numbers[3])  #40
#print(numbers[13]) #IndexError - List Index out of range
#update  & Delete 
numbers[2] = 33   
del numbers[3]   # deleting the element using index

print(numbers)