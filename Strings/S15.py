#Remove special symbols / punctuation from a string

import string

str1 = "/*kumar is @developer & musician"
print("Original string is ", str1)

new_str = str1.translate(str.maketrans('', '', string.punctuation))

print("New string is ", new_str)