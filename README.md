# proxypool

## 使用方法

### 安装Python

至少Python3.5以上

### 安装Redis

安装好之后将Redis服务开启

### 配置config相关内容

```
config.py
```

PWD为Redis密码，如果为空，则设置为None

#### 安装依赖

```
pip3 install -r requirements.txt
```

#### 打开代理池和API

```
python run.py
```


## 各模块功能

* www_get_ip.py

  > 从互联网获取代理IP

    class Get_IP(metaclass=ADD_GET_IPMetaclass)

    > 先定义了一个元类，通过__new__加上了新的方法def_count和def_list，
      可以自定义添加各网站解析的代理ip方法，通过def_count获取方法的数量，
      def_list 获取方法的名称列表，最后通过eval_get方法将其全部解析出来

* redis_fun.py

  > redis数据库API，提供了各种调用redis的方法


* test_ip.py

  > 代理IP检测模块

   class Test_url.test_list

    > 传入一个代理IP列表，用于检测IP的可用性，该方法通过aiohttp异步模块加载
      检测IP，提高检测速度。同时使用了traceback.extract_stack()方法用于检
      测传入的IP来自数据库还是互联网。

* flask_api.py

  > web接口API，启动web服务器，通过/get获取代理IP，/count获取数量

