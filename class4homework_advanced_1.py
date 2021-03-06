
# Write another script that prints the double of all values
# between 4 and 8 on the list [1,2,3,4,5,6,7,8,9]


my_list = [1,2,3,4,5,6,7,8,9]

# method 1 : for loop
for num in my_list[4:7]:
    print(num*2)


# method 2: List Comprehensions
DoubleValList = [num*2 for num in my_list[4:7]]
print(DoubleValList)