#
# mc.py: A naive, NumPy (array based) solution that pays little attention to memory use 
# and maximum attention to clarity of the algrorithm.
#
# This will be used to evolve more complex solutions (which still manage to remain largely clear)
#

import math
import numpy
import time
import sys

results_template="""
number of darts = %(darts)d
number of chunks = %(chunks)d
chunk size = %(chunkSize)d
time = %(delta_t)f
area = %(area)f
"""

darts = int(sys.argv[1])
chunks = int(sys.argv[2])
chunkSize = darts / chunks
darts = chunkSize * chunks

def mc(n):
    a = numpy.random.random(n)
    b = numpy.random.random(n)
    result = a*a + b+b
    return len(result[result <= 1.0])

start_time = time.clock()
runs = [mc(chunkSize) for i in range(0, chunks)]
area = 4.0 * sum(runs) / darts
stop_time = time.clock()
delta_t = stop_time - start_time

print(results_template % vars())

