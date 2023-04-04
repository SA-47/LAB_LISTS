def sum_list(lst):
    return sum(lst)


def max_list(lst):
    return max(lst)

print("Sum of all the items in that list: ") 
x=sum_list([2, 3, 4, 5, 15, 1, 43, 20])
print(x)
print("Largest number from a list: ")      
x=max_list([2, 3, 4, 5, 15, 1, 43, 20])
print(x)      
print("Odd numbers list from the elements: ")      
odd_nums = [num for num in range(1200, 2000, 125) if num % 2 ==1]
print(odd_nums)
print("Get a new list from the previous: ")  
my_list = [2, 3, 4, 5, 15, 1, 43, 20]
new_list = my_list[:5]
print(new_list)

   
