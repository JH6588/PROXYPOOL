import  redis

REDIS_POOL = redis.ConnectionPool(host='xxx.xxx.xxx.xxx', db=0, password='yyyy') #根据自身配置写
REDIS_COMM = redis.StrictRedis(connection_pool= REDIS_POOL)


DEFAULT_ENCODING = "utf8"
HTTP_KEY = "http_proxy"
HTTPS_KEY = "https_proxy"
PROXY_TIMEOUT = 45
MIN_NUM = 666
MAX_NUM =999
MAX_VOLUME =20000
OVER_MAX_WAITTIME = 300
OVER_MIN_WAITTIME = 100
RUNOUND_TIMEWAIT = 3999

DEFAULT_JUDGE_URLS =["https://3g.ganji.com/tj_ershouche/27669329632947x","https://3g.ganji.com/tj_ershouche/31373929586636x","https://3g.ganji.com/tj_ershouche/31308330736720x"]
DEFAULT_KEYWORD ="赶集"
DEFAULT_BAD_KEYWORD ="验证码"


