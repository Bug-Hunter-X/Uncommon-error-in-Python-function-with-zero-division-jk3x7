def improved_function(a, b):
    if b == 0:
        if a == 0:
            return 0 # Handle the case where both are zero
        else:
            return float('inf') # Or raise an exception for better error handling
    else:
        return a / b

result = improved_function(10, 0)
print(result) # Output: inf
result = improved_function(0, 20)
print(result) # Output: 0.0
result = improved_function(0,0)
print(result) #Output: 0