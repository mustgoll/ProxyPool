from config import *
import asyncio
import aiohttp
from redis_fun import RedisClient
import traceback
class Test_url(object):
    def __init__(self):
        self.url=TEST_URL
        self.r=RedisClient()
    # @asyncio.coroutine
    async def test_single(self,proxy,id):
        async with aiohttp.ClientSession() as session:
            if isinstance(proxy,bytes):
                proxy=proxy.decode()
            real_proxy='http://'+proxy
            try:
                async with session.get(self.url,proxy=real_proxy,timeout=5) as response:
                    if response.status==200:
                        print(proxy,'success',id)
                        self.r.put(proxy)
                        return True
                    else:
                        print(proxy,response.status,id)
                        return False
            except (asyncio.TimeoutError,aiohttp.client_exceptions.ClientOSError,aiohttp.client_exceptions.ClientConnectorError,aiohttp.client_exceptions.ClientResponseError,aiohttp.client_exceptions.ServerDisconnectedError):
                print(proxy,'超时',id)
                return False
    def test_list(self,proxies):
        try:
            id=traceback.extract_stack()[-2][2]
            loop=asyncio.get_event_loop()
            tasks=[self.test_single(proxy,id) for proxy in proxies]
            loop.run_until_complete(asyncio.wait(tasks))
        except ValueError:
            print('TEST列表为空')
        # loop.close()
if __name__=='__main__':
    a=['111.6.184.35:8081']
    test=Test_url()
    test.test_list(a)


