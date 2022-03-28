#Initialize dictionary with default values

employees = ['pavan', 'kumar' , 'bhoom']
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults)
print(res)

# Individual data
print(res["pavan"])