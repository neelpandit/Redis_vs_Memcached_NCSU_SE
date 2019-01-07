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

# hit the first 250k rows
for i in range(250000):
	a = "keys:"+ str(i)
	r.get(a)


# At the end of above steps, we would have hit the first 250k rows once.
# On adding more elements, test that these 250k elements should not be deleted.

# Add 500k more elements to overflow cache size, leading to key evictions.
for i in range(500000,1000000):
	a = "keys:"+ str(i)
	v = "vals:" + str(i)
	r.set(a,v)

# Access the first 250k rows and see how many hits were obtained.
for i in range(250000):
	a = "keys:"+ str(i)
	r.get(a)
