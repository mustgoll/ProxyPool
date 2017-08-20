import requests
from bs4 import BeautifulSoup
import re
base_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}
bds = re.compile('(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
class ADD_GET_IPMetaclass(type):#上层metaclaass类，例子可见元类的介绍
    def __new__(cls, *args):
        count=0
        args[2]['def_list']=[]
        for k,v in args[2].items():
            if 'getIP_' in k:
                args[2]['def_list'].append(k)
                count+=1
        args[2]['def_count']=count
        return type.__new__(cls,*args)
class Get_IP(metaclass=ADD_GET_IPMetaclass):#通过定义metaclass和eval可以自定义增加相关网络url获取ip
    def eval_get(self,callback):
        proxys=[]
        for i in eval('self.{}()'.format(callback)):
            # print(i)
            proxys.append(i)
        return proxys
    def getIP_goubanjia(self):
        url='http://www.goubanjia.com/free/gngn/index.shtml'
        html=BeautifulSoup(requests.get(url,headers=base_headers).text,'lxml')
        list=html.select('#list > table > tbody > tr')
        for i in list:
            item=i.contents
            dis_none=item[1].find_all("p")#发现用select筛选的话会有遗漏
            for i in dis_none:
                i.decompose() #删除网站诱惑爬虫的多余字段
            yield item[1].get_text()
    # def getIP_goubanjia2(self):
    #     url='http://www.goubanjia.com/free/gngn/index2.shtml'
    #     html=BeautifulSoup(requests.get(url,headers=base_headers).text,'lxml')#这个获取页面模块应该独立出来，防止被网站屏蔽，代码异常
    #     list=html.select('#list > table > tbody > tr')
    #     for i in list:
    #         item=i.contents
    #         dis_none=item[1].find_all("p")
    #         for i in dis_none:
    #             i.decompose() #删除网站诱惑爬虫的多余字段
    #         yield item[1].get_text()
    def getIP_ipxici(self):
        url='http://www.xicidaili.com/nn/'
        html=BeautifulSoup(requests.get(url,headers=base_headers,timeout=5).text,'lxml')
        list=html.select('#ip_list > tr')
        # prox_ip = bds.findall(list)
        for i in list[1:len(list)]:
            prox_ip = bds.findall(str(i))[0]
            prox_port=i.contents[5].get_text()
            yield prox_ip+':'+prox_port

if __name__=='__main__':
    a=Get_IP()
    for i in a.def_list:
        print(a.eval_get(i))