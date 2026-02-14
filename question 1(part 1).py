"""
question 6
part 1: String manipulation
"""

# Step1 input string as list of characters
a= input("Enter the string : ")
char_list = list(a)  # converts string to list of characters
print("Original list of characters:", char_list)

# Step2 delete at least 2 characters
# remove 1st and last characters
del char_list[0]   
del char_list[-1]
print("List after deleting 2 characters:", char_list)

# Step3 reverse the list
revers = char_list[::-1]  # slicing with step -1 reverses the list
print("Reversed list:", revers)

# Step4 convert back to string
final = ''.join(revers)  # join list elements to make string
print("Final output string:", final)
