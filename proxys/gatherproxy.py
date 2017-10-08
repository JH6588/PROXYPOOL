from proxy_utils import ProxyCrawler ,DEFAULT_HEADERS
import requests
import lxml.html
import  re

start_url = "http://www.gatherproxy.com/proxylistbycountry/"


def proxy_urls():
    req = requests.get(start_url ,headers = DEFAULT_HEADERS)
    tree = lxml.html.fromstring(req.text)
    proxy_url_list = tree.xpath("//ul[@class='pc-list']/li/a/@href")
    return proxy_url_list

class GatherProxy(ProxyCrawler):
    domain = "http://www.gatherproxy.com"
    http_proxy_list = https_proxy_list = proxy_urls()



    def get_http(self):

        for  _url in self.http_proxy_list:
            proxy_url = self .domain + _url
            page_html = requests.get(proxy_url,headers =self.headers).text
            regex_str = '''"PROXY_IP":"(.*?)",.*?,"PROXY_PORT":"(.*?)",.*?,"PROXY_TYPE":"Elite"'''
            proxy_all = re.findall(regex_str ,page_html)
            for proxy in proxy_all:
                ip = proxy[0]
                port = int(proxy[1] ,16)
                self.save_proxy(ip ,port,proxy_url)



    def get_https(self):
        for _url in self.https_proxy_list:
            req_url = self.domain + _url
            page_html = requests.get( req_url, headers=self.headers).text
            regex_str = '''"PROXY_IP":"(.*?)",.*?,"PROXY_PORT":"(.*?)",.*?,"PROXY_TYPE":"Elite"'''
            proxy_all = re.findall(regex_str, page_html)
            for proxy in proxy_all:
                ip = proxy[0]
                port = int(proxy[1], 16)
                self.save_proxy(ip, port ,req_url,"https")


