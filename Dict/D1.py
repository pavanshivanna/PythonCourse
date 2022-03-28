#Convert two lists into a dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res_dict = dict(zip(keys, values))
print(res_dict)

#or

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# empty dictionary
res_dict = dict()

for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})
print(res_dict)