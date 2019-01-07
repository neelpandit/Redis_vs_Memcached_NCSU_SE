import redis
import time

TEST_KEY= "TestKey"
r = redis.StrictRedis(host="127.0.0.1", port="6379")
r.flushall()

start_time = time.time()

# Testing the memory required to add 500k sorted set entries
for i in range(600000,100000, -1):
    score = i
    val = "val" + str(i)
    r.sadd(TEST_KEY, score, val)

time_for_insert = time.time() - start_time
print("time for insert" , time_for_insert)

# Memory used : 54.77 MB
# Time taken : 65.02s
