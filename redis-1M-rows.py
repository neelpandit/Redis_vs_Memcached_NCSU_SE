import redis
import time

r = redis.StrictRedis(host="127.0.0.1", port="6379")
r.flushall()

start_time = time.time()

# 1,000,000 rows - key size of 10 bytes and value size of 10 bytes
for i in range(1000000,2000000):
	a = "key" + str(i)
	v = "val" + str(i)
	r.set(a,v)

time_for_insert = time.time() - start_time
print("time for insert" , time_for_insert)
