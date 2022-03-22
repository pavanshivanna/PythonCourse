#Find all occurrences of a substring in a given string by ignoring the case

str1 = "Welcome to INDIA. India is awesome, isn't it?"
sub_string = "INDIA"

# convert string to lowercase
temp_str = str1.lower()

# use count function
count = temp_str.count(sub_string.lower())
print("The INDIA count is:", count)