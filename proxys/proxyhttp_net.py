from proxy_utils import ProxyCrawler
from selenium import webdriver
import platform
import lxml.html


domain = "https://proxyhttp.net"
class ProxyNet(ProxyCrawler):


    http_proxy_list = [domain +ele for ele in ["/free-list/anonymous-server-hide-ip-address/",
                                       "/free-list/proxy-anonymous-hide-ip-address/" ,
                                       "/free-list/proxy-high-anonymous-hide-ip-address/",
                                       "/free-list/proxy-https-security-anonymous-proxy/"]]

    https_proxy_list = http_proxy_list

    def get_http(self):
        http_url_text_list = []
        try:
            if platform.system() == "Linux":
                b = webdriver.PhantomJS()
            else:
                b = webdriver.Chrome()

            b.implicitly_wait(20)



            for  _url in self.http_proxy_list: #遍历各类
                for i in range(1,2): #翻页
                    b.get(_url +str(i))
                    http_url_text_list.append(b.page_source)
        except:
            b.quit()

        finally:
            b.quit()
        for html  in http_url_text_list:
            tree = lxml.html.fromstring(html)
            for row in tree.xpath("//table[@class='proxytbl']//tr/td[4][not(contains(text(),'Transparent'))]")[1:]:

                ip =row.xpath("../td[1]/text()")[0] .strip()
                port=row.xpath("../td[2]/text()[2]")[0] .strip()

                print(ip,port)
                self.save_proxy(ip, port ,domain)



    def get_https(self):
        if platform.system() == "Linux":
            b = webdriver.PhantomJS()
        else:
            b = webdriver.Chrome()

        b.implicitly_wait(20)

        http_url_text_list = []
        for _url in self.http_proxy_list:  # 遍历各类
            for i in range(1, 5):  # 翻页
                b.get(_url + str(i))
                http_url_text_list.append(b.page_source)

        b.quit()

        for html in http_url_text_list:
            tree = lxml.html.fromstring(html)
            for row in tree.xpath("//table[@class='proxytbl']//tr/td[4][not(contains(text(),'Transparent'))]")[1:]:
                if row.xpath("../td[@class='t_https']/img"):
                    ip = row.xpath("../td[1]/text()")[0]
                    port = row.xpath("../td[2]/text()[2]")[0]

                    self.save_proxy(ip,port, domain ,"https")

