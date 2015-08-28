import redis

class Redis:

    def __init__(self):

        self.host ='localhost'
        self.port = 6379
        self.db = 0

    def connect(self):

        try:
            self.r = redis.StrictRedis(host=self.host, port=self.port, db=self.db)

        except:
            print "Unable to establish connection to Redis server on {}".format(self.host)

    def redis_set(self, key, value):

        result = self.r.hmset(key, value)

        if result:
            print "key {} updated".format(key)
        else:
            print "Unable to update key {}".format(key)



    def redis_get(self, key):

        return self.r.hgetall(key)

