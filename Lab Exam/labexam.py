
def list_utils(data):
    try:
        if not isinstance(data, list):
            raise ValueError("Please provide a list input")
        
        total_sum = sum(data)
        reversed_list = list(reversed(data))
        max_value = max(data)
        
        return (total_sum, reversed_list, max_value)
    
    except ValueError as e:
        print(e)
        return None
    
# Example usage:
result = list_utils([1, 2, 3, 4, 5])    
print(result)  # Output: (15, [5, 4, 3, 2, 1], 5)
result = list_utils("not a list") # This will trigger the exception handling
print(result)  # Output: Please provide a list input

