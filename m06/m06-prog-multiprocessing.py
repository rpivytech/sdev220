import random
import time
import multiprocessing
from datetime import datetime

def random_float_generator():
    random_float = random.uniform(0, 1)
    return random_float

def time_thing():
    wait_time = random_float_generator()
    time.sleep(wait_time)
    timething = datetime.now()
    timething = timething.strftime("%Y-%m-%d %H:%M:%S.%f")
    print(timething)

if __name__ == "__main__":
    n = 0
    for n in range(3):
        p = multiprocessing.Process(target=time_thing,
          args=())
        p.start()