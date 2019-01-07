import redis
import time

MONTH_HASH= "Months"
DAY_HASH = "Day"
r = redis.StrictRedis(host="127.0.0.1", port="6379")
r.flushall()

start_time = time.time()


r.hset(MONTH_HASH,"January" ,"1")
r.hset(MONTH_HASH,"February" ,"2")
r.hset(MONTH_HASH,"March" ,"3")
r.hset(MONTH_HASH,"April" ,"4")

r.hset(DAY_HASH, "Sunday", "1")
r.hset(DAY_HASH, "Monday", "2")
r.hset(DAY_HASH, "Tuesday", "3")
r.hset(DAY_HASH, "Wednesday", "4")

time_for_insert = time.time() - start_time
print("time for insert" , time_for_insert)

print(r.hgetall(MONTH_HASH))
print(r.hgetall(DAY_HASH))
print(r.hkeys(MONTH_HASH))
print(r.hget(DAY_HASH, "Sunday"))
