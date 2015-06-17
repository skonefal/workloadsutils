import datetime
import os
import time

IDLE_TIME = 1#10 * 60 
STRESS_ITERATION_TIME = 5#10 * 60
STRESS_LEVEL_BEGINING = 1 # stress level in the begining of test
STRESS_ITER_INCREMENT = 2 #in each iteration stress will increase X times
NUM_OF_ITERATIONS = 4

def do_stress():
    print("{0}: Starting idle time for {1} seconds".format(datetime.datetime.now(), IDLE_TIME))
    time.sleep(IDLE_TIME)
    cpu_stress_level = STRESS_LEVEL_BEGINING
    for iter in range(0, NUM_OF_ITERATIONS):
        print("{0}: Starting stress level {1} for {2} secs | Iteration #{3}".format(
            datetime.datetime.now(), cpu_stress_level, STRESS_ITERATION_TIME, iter))
        os.system("stress -c {0} -t {1}".format(cpu_stress_level, STRESS_ITERATION_TIME))
        cpu_stress_level = cpu_stress_level * STRESS_ITER_INCREMENT
        pass
    
    print("{0}: Stress finished after {1} iterations".format(datetime.datetime.now(), NUM_OF_ITERATIONS))
    return

if __name__ == '__main__':
    do_stress()