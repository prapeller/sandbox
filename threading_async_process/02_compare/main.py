import threading
import time


def handler(value_start=0, value_finish=0):
    print("handler is working...")
    result = 0
    for i in range(value_start, value_finish):
        result += 1
    results.append(result)
    print("Results: ", sum(results))



params_1 = {"value_finish": 2 ** 25}
task_1 = threading.Thread(target=handler, kwargs=params_1)
params_2 = {"value_start": 2 ** 25, "value_finish": 2 ** 26}
task_2 = threading.Thread(target=handler, kwargs=params_2)

results = []
print("starting task_1, task_2")
time_start = time.time()
task_1.start()
task_1.join()
task_2.start()
task_2.join()
print(f"time for handler in task_1 + task_2: {time.time() - time_start}")

results = []
print("\nstarting handler")
time_start = time.time()
handler(value_finish=2 ** 26)
print(f"time for handler in main thread: {time.time() - time_start}")
