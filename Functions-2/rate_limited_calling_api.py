def create_rate_limited_caller(limit_per_minute):
    from time import time, sleep
    call_times = []
    
    # Inner function that enforces rate limiting
    def make_call(api_function, *args):
        nonlocal call_times
        now = time()
        
        # Remove calls older than 1 minute
        call_times = [t for t in call_times if now - t < 60]
        
        if len(call_times) >= limit_per_minute:
            sleep_time = 5 - (now - call_times[0])
            print(f"Rate limit reached. Sleeping for {sleep_time:.1f} seconds")
            sleep(sleep_time)
            call_times = []
            now = time()
        
        call_times.append(now)
        return api_function(*args)
    
    return make_call

# Create a rate-limited caller (max 5 calls per minute)
limited_call = create_rate_limited_caller(5)

# Now we can use it to safely call APIs
def mock_api_request(url):
    print(f"Calling {url}")
    return f"Response from {url}"

for i in range(10):
    print(limited_call(mock_api_request, f"api/data/{i}"))