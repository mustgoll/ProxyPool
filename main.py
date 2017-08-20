from www_get_ip import Get_IP
from redis_fun import RedisClient
from test_ip import Test_url
from config import *
from  multiprocessing import Process
import time
class Run(object):
    @staticmethod
    def check_r():
        r=RedisClient()
        test=Test_url()
        while True:
            print('代理ip数量:%s  开始筛选...' %r.rlen)
            for i in range(r.rlen//GET_REDIS_LIST+1):
                redis_list=r.get_list(GET_REDIS_LIST)#这个循环同样可以筛选，而且速度要快些
                test.test_list(redis_list)
            # for i in range(r.rlen):
            #     redis_list=r.get_one()
            #     test.test_list(redis_list)
            print('数据库筛选完成共:%s，等待下次筛选...' %r.rlen)
            time.sleep(REDIS_IP_CHECK)
    @staticmethod
    def add_r():
        r=RedisClient()
        test=Test_url()
        proxies=Get_IP()
        while True:
            if MIN>r.rlen:
                print('正在添加来着互联网的IP')
                for i in range(proxies.def_count):
                    test.test_list(proxies.eval_get(proxies.def_list[i]))
                    if MAX<r.rlen:
                        break
            time.sleep(REDIS_IP_CHECK//3)
    def run_start(self):
        add = Process(target=Run.add_r)
        check = Process(target=Run.check_r)
        add.start()
        check.start()
if __name__=='__main__':
    r=Run()
    r.start()