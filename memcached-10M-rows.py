from pymemcache.client import base
import time

r = base.Client(('localhost', 11211))
start_time = time.time()

# Inserting 10M rows of key size 13 bytes and value size 13 bytes
for i in range(10000000,20000000):
	a = "keys:"+ str(i)
	v = "vals:" + str(i)
	r.set(a,v)

time_for_insert = time.time() - start_time
print("time for insert" , time_for_insert)
