#Find the last position of a given substring

str1 = "Pavan is a data scientist who knows Python. Pavan works at google."
print("Original String is:", str1)

index = str1.rfind("Pavan")
print("Last occurrence of Pavan starts at index:", index)