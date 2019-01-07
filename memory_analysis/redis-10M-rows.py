import redis
import time

r = redis.StrictRedis(host="127.0.0.1", port="6379")
r.flushall()

start_time = time.time()

# 10,000,000 rows - key size of 13 bytes and value size of 13 bytes
for i in range(10000000,20000000):
	a = "keys:" + str(i)
	v = "vals:" + str(i)
	r.set(a,v)

time_for_insert = time.time() - start_time
print("time for insert" , time_for_insert)
