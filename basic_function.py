import ray
import time
import os


# Ray dashboard: http://localhost:8265

# compute intensive function
def fibonacci(n):
    f = []
    for i in range(0, n):
        if i < 2:
            f.append(i)
            continue
        f.append(f[i - 1] + f[i - 2])
    return n


# normal function
def fibonacci_local(n):
    return fibonacci(n)


# ray function, decorated with annotation
@ray.remote
def fibonacci_remote(n):
    return fibonacci(n)


# Ray
def run_remote(sequence_size):
    # Starting Ray
    ray.init()
    start_time = time.time()
    results = ray.get([fibonacci_remote.remote(sequence_size) for _ in range(os.cpu_count())])
    duration = time.time() - start_time
    print('The number to calculate fibonacci: {}, Remote execution time: {}'.format(sequence_size, duration))
    #ray.shutdown()


def run_local(sequence_size):
    start_time = time.time()
    results = [fibonacci_local(sequence_size) for _ in range(os.cpu_count())]
    duration = time.time() - start_time
    print('The number to calculate fibonacci: {}, Local execution time: {}'.format(sequence_size, duration))


if __name__ == '__main__':
    run_local(100000)
    run_remote(100000)
