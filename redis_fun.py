import redis
import random
from config import PWD,HOST,PORT,DB,NAME
class RedisClient(object):
    def __init__(self):
        self.pool=redis.ConnectionPool(host=HOST,port=PORT,password=PWD,db=DB)
        self.r=redis.Redis(connection_pool=self.pool)
        self.name=NAME
    @property
    def get(self):
        if self.rlen==0:
            return '无法获取ip...'
        prox=self.r.lindex(self.name,random.randint(self.rlen//2,self.rlen-1))
        return prox.decode()
    def get_one(self):
        l=[]
        l.append(self.r.lpop(self.name))
        return l
    def put(self,*value):
        self.r.rpush(self.name,*value)
    @property
    def rlen(self):
        return self.r.llen(self.name)
    @property
    def rdel(self):
        return self.r.delete(self.name)
    def get_list(self,value):
        pro=self.r.lrange(self.name,0,value-1)
        self.r.ltrim(self.name,value,-1)
        return pro

if __name__=='__main__':
    client=RedisClient()
    print(client.get_list(1))