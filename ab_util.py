import os
import datetime
import time

IDLE_TIME = 2 * 60 
STRESS_ITERATION_TIME = 10 * 60

STRESS_LEVELS = [2,10,25,50,75,100]

# ENDPOINTS = ["http://10.102.44.201/index.php/Special:Random", "http://10.102.44.202/index.php/Special:Random", "http://10.102.44.203/index.php/Special:Random"]

def do_stress():
    print("{0}: Starting idle time for {1} seconds".format(datetime.datetime.now(), IDLE_TIME))
    time.sleep(IDLE_TIME)
    for stress_level in STRESS_LEVELS:
        Timestamp = datetime.datetime.now()
        print("{0}: Starting stress level {1} for {2} secs".format(
            datetime.datetime.now(), stress_level, STRESS_ITERATION_TIME))
        os.system("ab -c {0} -s {1} -n 900000 -l -r http://10.102.44.202/index.php/Special:Random".format(
            stress_level, STRESS_ITERATION_TIME))
        pass
    
    print("{0}: Stress finished after {1} iterations".format(
        datetime.datetime.now(), len(STRESS_LEVELS)))
    return

if __name__ == '__main__':
    do_stress()