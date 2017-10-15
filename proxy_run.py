import time
import sys
import random
from proxys.free_proxy_list import FreeProxy
from proxys.cn_proxy_com import CNProxy
from proxys.gatherproxy import GatherProxy
from proxys.httpsdaili import HTTPSDaili
from proxys.nyloner import NYProxy
from proxys.proxyhttp_net import ProxyNet
import proxy_config
from  proxy_config import REDIS_COMM, HTTP_KEY, HTTPS_KEY, MAX_VOLUME
from importlib import reload

proxy_objs = [FreeProxy(), CNProxy(), GatherProxy(), HTTPSDaili(), NYProxy(), ProxyNet()]


def proxy_runner(proxy_type=0):
    if proxy_type == 0:
        redis_key = HTTP_KEY
    elif proxy_type == 1:
        redis_key = HTTPS_KEY
    else:
        return

    while True:
        random.seed = int(time.time())
        random.shuffle(proxy_objs)
        new_proxy_config = reload(proxy_config)
        max_num = new_proxy_config.MAX_NUM
        over_max_waittime = new_proxy_config.OVER_MAX_WAITTIME
        round_timewait = new_proxy_config.RUNOUND_TIMEWAIT
        max_volume = new_proxy_config.MAX_VOLUME
        for obj in proxy_objs:
            store_num = REDIS_COMM.llen(redis_key)
            if store_num > max_volume:
                raise  Exception
            if store_num > max_num:
                print("现IP数量: {} , 超过 MAX_VOLUME: {} , "
                      " 等待 MAX_WAITTIME:  {}".format(store_num ,max_num ,over_max_waittime))
                time.sleep(over_max_waittime)
            try:
                obj.get_http()
            except:
                pass
        print("等待 RUNOUND_TIMEWAIT: {}".format(round_timewait))
        time.sleep(round_timewait)


if __name__ == '__main__':

    if len(sys.argv) > 1 and sys.argv[1] == "https":  #默认为抓取http proxy
        proxy_runner(1)
    else:
        proxy_runner(0)
