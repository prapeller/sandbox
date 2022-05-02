import threading
import time


def producer(name):

    print(f"{name} is trying to acquire lock")
    with lock:
        print(f"lock is acquired by {name}")
        print(f"lock have free workers yet: {lock._value}")

        print(f"{name} is trying to acquire lock again")
        with lock:
            print(f"lock have free workers yet: {lock._value}")
            print(f"lock is acquired by {name}")
    print(f"lock released by {name}")
    # lock.release() # <- you should control number of releasing (ValueError: Semaphore released too many times)


max_workers = 2
lock = threading.BoundedSemaphore(value=max_workers)    # <-- control acquiring and releasing:  yes
# lock = threading.Semaphore(value=max_workers)           # <-- control acquiring and releasing:  no
# __enter__ => lock.acquire()
# __exit__ => lock.release()

thread_1 = threading.Thread(target=producer, kwargs={"name": "thread_1"})
thread_2 = threading.Thread(target=producer, kwargs={"name": "thread_2"})

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()