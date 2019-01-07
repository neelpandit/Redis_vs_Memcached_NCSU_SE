import redis
import time

r = redis.StrictRedis(host="127.0.0.1", port="6379")
r.flushall()

start_time = time.time()

# key size of 9 bytes and value size of 9 bytes
for i in range(100000,300000):
	a = "key" + str(i)
	v = "val" + str(i)
	r.set(a,v)

time_for_insert = time.time() - start_time
print("time for insert" , time_for_insert)
