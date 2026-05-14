import threading
import time
from concurrent.futures import ThreadPoolExecutor

def waiting(seconds):
    print(f"This process is waiting for {seconds} seconds")
    time.sleep(seconds)
    return seconds
def main():
    start_time= time.perf_counter()
    # Normal method of calling function to run in series
    # waiting(4)
    # waiting(2)
    # waiting(1)

    # declaring threads
    t1= threading.Thread(target=waiting, args=[4] )
    t2= threading.Thread(target=waiting, args=[2] )
    t3= threading.Thread(target=waiting, args=[1] )

    # to start thread manually
    t1.start()
    t2.start()
    t3.start()

    #  to ask other thread to wait till others finished
    t1.join()
    t2.join()
    t3.join()
    # total time taken calculation
    end_time = time.perf_counter()
    print(f"\ntotal time taken {end_time - start_time} seconds")

def pooling_demo():
    start_time= time.perf_counter()
    with ThreadPoolExecutor(max_workers=3) as executors:
        # future1 = executors.submit(waiting,4)
        # future2 = executors.submit(waiting, 3)
        # future3 = executors.submit(waiting, 2)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        l= [3,4,1,5]
        result = executors.map(waiting,l)
        for i in result:
            print(i)
    end_time = time.perf_counter()
    print(f"\ntotal time taken {end_time - start_time} seconds")
# main()
pooling_demo()
