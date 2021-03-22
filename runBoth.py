import time
import os
from threading import Thread

def singleT():
    start1 = time.perf_counter()
    os.system('python webscraper.py')
    finish1 = time.perf_counter()
    print(f'Single-threaded webscraper finished in {round(finish1-start1,2)} second(s)')

def multiT():
    start2 = time.perf_counter()
    os.system('python MTwebscraper.py')
    finish2 = time.perf_counter()
    print(f'Multi-threaded webscraper finished in {round(finish2-start2,2)} second(s)')


threads = []

t = Thread(target=singleT)
t.start()
threads.append(t)

t = Thread(target=multiT)
t.start()
threads.append(t)

for thread in threads:
    t.join()

