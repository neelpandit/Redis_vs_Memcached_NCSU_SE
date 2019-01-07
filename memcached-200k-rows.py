from pymemcache.client import base
import time

r = base.Client(('localhost', 11211))
start_time = time.time()

# Inserting 200k rows of key size 9 bytes and value size 9 bytes
for i in range(100000,300000):
	a = "key"+ str(i)
	v = "val" + str(i)
	r.set(a,v)

time_for_insert = time.time() - start_time
print("time for insert" , time_for_insert)
