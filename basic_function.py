import ray
import time


# Ray dashboard: http://localhost:8265

# simple function
@ray.remote
def square(n):
    return n * n

# compute intensive function

if __name__ == '__main__':
    futures = [square.remote(i) for i in range(200)]
    results = ray.get(futures)
    print(results)
