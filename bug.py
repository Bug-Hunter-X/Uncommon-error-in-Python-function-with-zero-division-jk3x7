def function_with_uncommon_error(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

result = function_with_uncommon_error(10, 0)
print(result) # this will raise ZeroDivisionError
result = function_with_uncommon_error(0, 20)
print(result) # this will print 20
result = function_with_uncommon_error(0,0) #this will print 0