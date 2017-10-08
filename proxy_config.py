import  redis

REDIS_POOL = redis.ConnectionPool(host='xxx.xxx.xxx.xxx', db=0, password='yyyy') #根据自身配置写
REDIS_COMM = redis.StrictRedis(connection_pool= REDIS_POOL)



HTTP_KEY = "http_proxy"  # http proxy  redis 的队列name
HTTPS_KEY = "https_proxy" # https proxy  redis 的队列name
PROXY_TIMEOUT = 45  # 抓取爬虫网站的超时时间


MIN_NUM = 666 # IP池 内低于 MIN_NUM  时，清洗线程将暂停OVER_MIN_WAITTIME
MAX_NUM =999 # IP池内数量高于MAX_NUM 时,抓取线程将 暂停 OVER_MAX_WAITTIME
MAX_VOLUME =20000  #高于最大容量时 抓取线程将终止
OVER_MAX_WAITTIME = 300
OVER_MIN_WAITTIME = 100
RUNOUND_TIMEWAIT = 3999 #代理ip 网站抓取一轮后的 暂停时间
#以上这6 个配置 支持热更改。无需重启程序 即可生效



#校检网址。每次会随机取出一个进行检测，根基自己的任务可以自行定制
DEFAULT_JUDGE_URLS =["https://3g.ganji.com/tj_ershouche/27669329632947x",
                     "https://3g.ganji.com/tj_ershouche/31373929586636x",
                     "https://3g.ganji.com/tj_ershouche/31308330736720x"]

DEFAULT_KEYWORD ="赶集" #校检关键词

DEFAULT_BAD_KEYWORD ="验证码" #校检非法关键词


