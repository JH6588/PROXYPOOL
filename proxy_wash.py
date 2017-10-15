from proxy_utils import ProxyCrawler
import sys ,time
from  importlib import reload
import proxy_config
from  proxy_config import REDIS_COMM ,HTTP_KEY,HTTPS_KEY
P = ProxyCrawler()

def wash_proxy(proxy_type = 0):
    if proxy_type == 0:
        redis_key = HTTP_KEY
    elif proxy_type == 1:
        redis_key =HTTPS_KEY
    else:
        return
    while True:
        proxy = REDIS_COMM.rpop(redis_key)
        if proxy ==None:
            break
        proxy_str = proxy.decode()
        ip ,port =proxy_str.split(':')
        new_proxy_config =reload(proxy_config)
        proxy_timeout = new_proxy_config.PROXY_TIMEOUT
        min_num = new_proxy_config.MIN_NUM
       # print(proxy_timeout,min_num,"----------------")
        if P.get_anonymous(ip,port,timeout= proxy_timeout):
            REDIS_COMM.lpush(redis_key,proxy_str)
            print("{}检验通过".format(proxy_str))
        else:
            store_num = REDIS_COMM.llen(redis_key)
            print("{}检验失败,库中还有{}个".format(proxy_str,store_num))
            if store_num < min_num:
                time.sleep(proxy_config.OVER_MIN_WAITTIME)




if __name__ == '__main__':
    if len(sys.argv) >1 and sys.argv[1] =="https":  # python  proxy_wash.py https  执行抓取https proxy
        wash_proxy(1)
    else:
        wash_proxy(0) #默认抓取http proxy
