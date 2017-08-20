from  flask import Flask,g
from redis_fun import RedisClient

__all__=['app']
app=Flask(__name__)
# def r():
#     return RedisClient()
r = RedisClient()
@app.route('/')

def index():
    return '<h2>欢迎使用代理api(请使用/get和/count查看)</h2>'
@app.route('/get')
def get():
    return str(r.get)
@app.route('/count')
def count():
    return str(r.rlen)
if __name__=='__main__':
    app.run()