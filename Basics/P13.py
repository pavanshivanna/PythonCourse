#define function to check length of string and return true if length is 8 and false if length is less or more

def foo(password):
    if len(password) >= 8:
        return True
    else:
        return False

print(foo('pavans'))