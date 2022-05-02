from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


def handler(value_from=0, value_to=0):
    # print("VALUES", value_from, value_to)
    result = 0
    for i in range(value_from, value_to):
        result += 1
    return result


def run_by_executor(executor_class, max_workers=4):
    executor = executor_class(max_workers=max_workers)
    time_start = time.time()
    future_1 = executor.submit(handler, value_from=0, value_to=2 ** 26)
    future_2 = executor.submit(handler, value_from=2 ** 26, value_to=2 ** 28)

    result = sum((future_1.result(), future_2.result()))
    print("{executor} result: {result}\ntime: {spent_time}".format(
        executor=executor_class.__name__,
        result=result,
        spent_time=time.time() - time_start
    ))


def run_by_executor_map(executor_class, max_workers=4):
    executor = executor_class(max_workers=max_workers)
    time_start = time.time()
    params = (
        [0, 2 ** 26],
        [2 ** 26, 2 ** 28],
    )
    result = sum(executor.map(handler, *params))
    print("{executor} result: {result}\ntime: {spent_time}".format(
        executor=executor_class.__name__,
        result=result,
        spent_time=time.time() - time_start
    ))


print("execute using submit...")
run_by_executor(ThreadPoolExecutor)
run_by_executor(ProcessPoolExecutor)

print("execute using map...")
run_by_executor_map(ThreadPoolExecutor)
run_by_executor_map(ProcessPoolExecutor)
