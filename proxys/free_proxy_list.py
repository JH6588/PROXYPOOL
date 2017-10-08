from proxy_utils import ProxyCrawler

class FreeProxy(ProxyCrawler):
    new_proxy_url = "https://www.sslproxies.org/"
    uk_proxy_url = "https://free-proxy-list.net/uk-proxy.html"
    anonymous_proxy_url = "https://free-proxy-list.net/anonymous-proxy.html"
    us_proxy_url = 'https://www.us-proxy.org/'
    ssl_proxy_url = "https://www.sslproxies.org/"

    http_proxy_list = [new_proxy_url, uk_proxy_url, anonymous_proxy_url ,ssl_proxy_url,
                       us_proxy_url]

    https_proxy_list = http_proxy_list

    def get_http(self):
        #socket_proxy_url = "https://www.socks-proxy.net/"
        for  _url in self.http_proxy_list:
            tree =self.make_tree(_url)
            for row in tree.xpath("//tr/td[5][text()='anonymous']")[1:-1]:

                ip =row.xpath("../td[1]/text()")[0]
                port=row.xpath("../td[2]/text()")[0]
                self.save_proxy(ip, port ,_url)

    def get_https(self):
        for _url in self.https_proxy_list:
            tree = self.make_tree(_url)
            for row in tree.xpath("//tr/td[5][text()='anonymous']")[1:-1]:
                if row.xpath("../td[7][text()='yes']"):
                    ip = row.xpath("../td[1]/text()")[0]
                    port = row.xpath("../td[2]/text()")[0]
                    self.save_proxy(ip,port ,_url ,"https")


