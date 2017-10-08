from proxy_utils import ProxyCrawler
import requests
import re


class FreeProxy(ProxyCrawler):
    http_proxy_list=  https_proxy_list =["https://www.hide-my-ip.com/proxylist.shtml"]

    def get_proxy_json (self):
        proxy_url = self.http_proxy_list[0]
        html = requests.get(proxy_url ,headers =self.headers).text
        jd = re.search("var json =(.*?) ;<!-- proxylist -->",html ,re.S)
        print(html)
        return jd

    def get_http(self):
        #socket_proxy_url = "https://www.socks-proxy.net/"
        for  _url in self.http_proxy_list:
            tree =self.make_tree(_url)
            for row in tree.xpath("//tr/td[5][text()='anonymous']")[1:-1]:

                ip =row.xpath("../td[1]/text()")[0]
                port=row.xpath("../td[2]/text()")[0]
                self.save_proxy(ip, port ,_url)

    def get_https(self):
        pass


