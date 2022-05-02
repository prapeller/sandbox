import threading
import time


def producer(name):
    print(f"{name} is trying to acquire lock")
    with lock:
        print(f"lock is acquired by {name}")

        print(f"{name} is trying to acquire lock again")
        with lock:
            print(f"lock is acquired by {name}")
    print(f"lock released by {name}")


lock = threading.RLock()
# __enter__ => lock.acquire()
# __exit__ => lock.release()

thread_1 = threading.Thread(target=producer, kwargs={"name": "thread_1"})
thread_2 = threading.Thread(target=producer, kwargs={"name": "thread_2"})

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()