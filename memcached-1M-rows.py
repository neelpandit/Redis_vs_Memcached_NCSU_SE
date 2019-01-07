from pymemcache.client import base
import time

r = base.Client(('localhost', 11211))
start_time = time.time()

# Inserting 1M rows of key size 10 bytes and value size 10 bytes
for i in range(1000000,2000000):
	a = "key"+ str(i)
	v = "val" + str(i)
	r.set(a,v)

time_for_insert = time.time() - start_time
print("time for insert" , time_for_insert)
