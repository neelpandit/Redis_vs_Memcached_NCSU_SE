import redis
import time

TEST_HASH= "TestHash"
r = redis.StrictRedis(host="127.0.0.1", port="6379")
r.flushall()

start_time = time.time()

# Testing the memory required to add 500k list entries
for i in range(100000,600000):
    key = "key" + str(i)
    val = "val" + str(i)
    r.lpush(TEST_HASH, key+val)

time_for_insert = time.time() - start_time
print("time for insert" , time_for_insert)

# Memory used : 10.58 MB
# Time taken : 51.97s
