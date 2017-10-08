from flask import Flask
import redis
import random
import  time

pool = redis.ConnectionPool(host='xxxx', port=6379, db=0,password ='yyyy') #自己设定
rs = redis.StrictRedis(connection_pool=pool)
cache_time = 200  #缓存时间

app = Flask(__name__)


t =0
rl_raw_list =[]
@app.route("/proxy/<x>/<proxy_num>")
def get_proxy(x, proxy_num):
    if x =="https":
        k = "https_proxy"
    else:
        k ="http_proxy"

    return get_redis_proxy(k, proxy_num)

def get_redis_proxy(k,page):
    global rl_raw_list ,t
    ts = time.time()
    if page ==1:
        px = rs.rpop(k)
        if px !=None:
            px_str = px.decode()
            rs.rpush(k,px_str)
            return px_str
        else:
            return "仓库空了"
    try:
        if ts -t >cache_time:
            rl = rs.lrange(k, 0, -1)
            rl_new_list = [i.decode() for i in rl]

            rl_raw_list = rl_new_list

            t = ts
            print("新请求")
            return "<h2>代理ip</h2><br>{}".format("<br>".join(random.sample(rl_raw_list,page)))
        else:
            print("原来请求")
            return "<h2>代理ip</h2><br>{}".format("<br>".join(random.sample(rl_raw_list,page)))

    except Exception as e:
        print(e)
        return "请求个数超过最大值或者程序内部故障"




if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)