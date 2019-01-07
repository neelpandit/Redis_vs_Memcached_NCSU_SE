import redis
import time
import random

r = redis.StrictRedis(host="127.0.0.1", port="6379")
start_time = time.time()

# CACHE SIZE IS INITALLY SET TO 64 MB.

# add 500k rows to redis
for i in range(500000):
	a = "keys:"+ str(i)
	v = "vals:" + str(i)
	r.set(a,v)

time_ins = time.time()
time_for_insert = time_ins - start_time
print("time for insert" , time_for_insert)

# hit the first 100k rows
for i in range(100000):
	a = "keys:"+ str(i)
	r.get(a)

# hit the first 50k rows
for i in range(50000):
	a = "keys:"+ str(i)
	r.get(a)

# hit the first 25k rows.
for i in range(25000):
	a = "keys:"+ str(i)
	r.get(a)

# At the end of above steps, we would have hit the first 25k rows 3 timesself.
# On adding more elements, test that these 25k elements should not be deleted.

# Add 500k more elements to overflow cache size, leading to key evictions.
for i in range(500000,1000000):
	a = "keys:"+ str(i)
	v = "vals:" + str(i)
	r.set(a,v)

# Access the first 25k rows and see how many hits were obtained.
for i in range(25000):
	a = "keys:"+ str(i)
	r.get(a)

# We used redis-cli info to obtain hits and misses after this
# Result : Total gets : 200000
# Total hits : 199379
# Total miss : 621
# Analysis : These misses occur from the misses in the section to get the first 25k
# elements after the cache was evicted of some keys. Ideally these 25k should not
# have been evicted since they were accessed 3 times, but they were since redis uses
# an approximate LRU algorithm.
