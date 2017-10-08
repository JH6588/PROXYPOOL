import requests
import lxml.html
import proxy_config
from urllib.parse import  urlparse
from importlib import reload
from proxy_config import DEFAULT_BAD_KEYWORD,DEFAULT_JUDGE_URLS,DEFAULT_KEYWORD,PROXY_TIMEOUT
import random


DEFAULT_ENCODING = "utf8"
DEFAULT_HEADERS= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/44.0.2403.130 Safari/537.36'}

#根据请求头过滤和异常校检来 抓取proxy.如果对匿名性程度 ，可自行增减。
DEFAULT_BAN_HEADERS_KEY =["via" ,"X-HOST" ,"X-Cache-Lookup" ,"X-Cache", "Proxy-Connection" , "X-Real-IP","X-Forwarded-For",
                          "Proxy-Authorization" ]

class ProxyCrawler:
    def __init__(self ,headers=DEFAULT_HEADERS ,keyword = DEFAULT_KEYWORD ,
                 bad_keyword =DEFAULT_BAD_KEYWORD  ):

        self.headers = headers
        self.keyword = keyword
        self.bad_keyword = bad_keyword
    def get_http(self):
        pass

    def get_https(self):
        pass

    def get_judgeurl(self):

        return random.choice(DEFAULT_JUDGE_URLS )


    def get_anonymous(self ,ip ,port ,timeout =PROXY_TIMEOUT  ):
        judge_url = self.get_judgeurl()
        req_scheme = urlparse(judge_url).scheme
        try:
            reload(proxy_config)

            req = requests.get(judge_url, headers=self.headers, proxies={req_scheme: "{}:{}".format(ip, port)},
                               timeout= timeout)

            req.encoding = DEFAULT_ENCODING
            status = req.status_code
            req_headers = req.headers
            html = req.text
            print(req_headers)
            forbid_keys = [k for k in req_headers if k in DEFAULT_HEADERS]
            if  400 <= status :
                print("状态码异常:{}".format(status))
                return False
            elif self .keyword not in html :
                print("异常，不存在校验字符! \n {}".format(html[:1000]))
                return False
            elif self.bad_keyword in html:
                print("异常，存在非法字符! \n ")
                return False
            elif forbid_keys:
                print("非法请求头部: {}".format(",".join(forbid_keys)))
                return False
            else:
                #print(html)
                return True

        except Exception as e:
            print("请求失败 {} ".format(e ))
            return  False

    def  save_proxy(self ,ip ,port ,from_url ,proxy_type ="http"):
        if self.get_anonymous(ip,port ):
            if proxy_type =="http":
                save_key = proxy_config.HTTP_KEY
                print("库中现有ip {} 个".format(proxy_config.REDIS_COMM.llen(proxy_config.HTTP_KEY)))
            else:
                save_key =proxy_config.HTTPS_KEY
                print("库中现有ip {} 个".format(proxy_config.REDIS_COMM.llen(proxy_config.HTTPS_KEY)))
            proxy_config.REDIS_COMM.rpush(save_key ,"{}:{}".format(ip,port) )
            print("成功: {}:{} ,来源:{}".format(ip,port ,from_url))

        else:
            print("舍弃 {}:{},来源:{}".format(ip,port ,from_url))



    def  make_tree(self,url ,encoding ="utf8"):
        req = requests.get(url, headers=self.headers ,verify=False )
        req.encoding = encoding
        tree = lxml.html.fromstring(req.text)
        return tree