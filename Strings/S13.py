#Split a string on hyphens

str1 = "kumar-is-a-data-scientist"
print("Original String is:", str1)

# split string
sub_strings = str1.split("-")

print("Displaying each substring")
for sub in sub_strings:
    print(sub)