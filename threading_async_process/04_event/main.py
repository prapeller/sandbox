import threading
import time


def producer():
    time.sleep(1)
    print("producer is producing event 1st time!")
    event.set()

    # time.sleep(1)
    print("producer is clearing event")
    event.clear()

    # time.sleep(1)
    # print("producer is producing event 2nd time!")
    # event.set()


def consumer():
    print("concumer is waiting for event 1st time...")
    event.wait()
    print("consumer found event 1st time!")

    print("concumer is waiting for event 2nd time...")
    event.wait()
    print("consumer found event 2nd time!")


event = threading.Event()

thread_producer = threading.Thread(target=producer)
thread_consumer = threading.Thread(target=consumer)

thread_producer.start()
thread_consumer.start()

thread_producer.join()
thread_consumer.join()
