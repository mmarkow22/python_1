def time_measure(func):
    import time
    def wrapper(*args, **kwargs):
        print(f"Starting execution of {func.__name__}, time: {time.strftime('%X')}")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Ended execution of {func.__name__}, time: {time.strftime('%X')}, took: {end_time - start_time} seconds")
        return result
    return wrapper