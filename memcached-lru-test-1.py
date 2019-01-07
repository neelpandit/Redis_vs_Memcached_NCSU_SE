from pymemcache.client import base
import time

r = base.Client(('localhost', 11211))

# CACHE SIZE IS INITALLY SET TO 64 MB.

start_time = time.time()
# add 500k rows to memcached
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

# We used telnet on localhost:11211 with stats command to obtain hits and misses after this
# Result : Total gets : 200000
# Total hits : 200000
# Total miss : 0
# Analysis : There are no misses. Memcache's LRU algorithm did not evict the first
# 25k keys as it observed them to be last used.
