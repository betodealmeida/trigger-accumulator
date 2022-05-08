import math
import random
import time

counter = 0

# how many notes we can accumulate before a sure trigger
CAPACITY = 8  # default 8? 1-32?

# trigger happiness
PROBABILITY = 1  # default 1

# curve
curve = 1  # default 1, 0.25-4

# >1 will make triggers sparse
# <1 will make triggers clustered
CLUSTERING = 1  # default 1, 0.25-4


while True:
    trigger = random.random() / PROBABILITY
    threshold = counter ** curve / CAPACITY ** curve
    if trigger < threshold:
        print("tsch")
        counter -= 1 / CLUSTERING
    else:
        print("-")
        counter += 1 * CLUSTERING

    if counter < 0:
        counter = 0
    elif counter > CAPACITY:
        counter = CAPACITY

    time.sleep(0.25)
