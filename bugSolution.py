def my_function(x):
    if x == 0:
        return float('inf')  # or raise an exception: raise ZeroDivisionError("Cannot divide by zero")
    else:
        return 1 / x

result = my_function(0)
print(result) # Output: inf 