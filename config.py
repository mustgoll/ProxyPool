HOST='localhost'
PORT='6379'
DB=0
PWD='abcd1234'  #redis密码
NAME='proxies'
MIN=30
MAX=60#若不在这个区间，则自动获取
GET_REDIS_LIST=5 #每次从数据库获取用于检测的数量
REDIS_IP_CHECK=20#检查数据库ip的时间间隔（除以3取整为检测数据库ip是否足够的时间间隔）
from random import choice
TEST_URL=choice(['http://www.ip138.com/','http://www.baidu.com','http://www.sohu.com/','https://www.so.com/'])

