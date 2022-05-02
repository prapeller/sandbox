import threading

print(threading.active_count())
current_thread = threading.current_thread()
print(current_thread)
print(current_thread.name)
print(current_thread.is_alive())

try:
    current_thread.start()
except RuntimeError as e:
    print(f"error: {e}")
current_thread.name = "SuperThread"
print(current_thread.name)
print(threading.enumerate())

# thread safety local storage
thread_local = threading.local()
thread_local.value = 5


def print_thread_local_value():
    print(f"local storage value in {threading.current_thread()}: {thread_local.value}")
    print(f"thread_local has attr 'value': {hasattr(thread_local, 'value')}")


def counter(value_from, value_to):
    print(f"thread_local has attr 'value': {hasattr(thread_local, 'value')}")
    thread_local.value = value_from
    for i in range(value_to):
        thread_local.value += 1
    print_thread_local_value()

thread_1 = threading.Thread(target=counter, args=(0, 10000000), name="Thread1")
thread_2 = threading.Thread(target=counter, args=(10000000000, 30000000), name="Thread2")

thread_1.start()
thread_2.start()

print_thread_local_value()

thread_1.join()
thread_2.join()

print_thread_local_value()
