import threading
import time


def handler(value_start=0, value_finish=0):
    print("handler is working")
    result = 0
    for i in range(value_start, value_finish):
        result += 1
    print("Result: ", result)


params_1 = {"value_finish": 2 ** 26}
task_1 = threading.Thread(target=handler, kwargs=params_1)

print("starting task_1")
time_start = time.time()
task_1.start()
print("joining task_1 to main thread")
task_1.join()     # <-- this line joins task_1 thread to main thread (main thread cant continue till task_1 finish its work)
print(f"time for task_1: {time.time() - time_start}")

print("\nstarting handler")
time_start = time.time()
handler(**params_1)
print(f"time for task_1: {time.time() - time_start}")
