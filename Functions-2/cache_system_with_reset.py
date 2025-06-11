# Cache System with Reset Capability

def create_cached_calculator():
    cache = {}
    
    # Inner function to calculate and cache results
    def calculate(key, computation_func):
        if key not in cache:
            cache[key] = computation_func()
        return cache[key]
    
    # Inner function to reset cache
    def reset_cache():
        nonlocal cache
        cache = {}
        print("Cache cleared")
    
    # Expose both inner functions
    return calculate, reset_cache

# Get references to the inner functions
compute, reset = create_cached_calculator()

# Now we can use them from outside
result1 = compute('square_5', lambda: 5**2)  # Calculates and caches
result2 = compute('square_5', lambda: 5**2)  # Uses cached value
print(result1, result2)  # 25 25

reset()  # Clears the cache
result3 = compute('square_5', lambda: 5**2)  # Recalculates
print(result3)  # 25