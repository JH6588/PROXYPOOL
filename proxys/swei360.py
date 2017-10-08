from proxy_utils import ProxyCrawler


class SWE360(ProxyCrawler):

    start_url = "http://www.swei360.com/free/"
    proxy_list =[start_url+"?stype={}?stype=1".format(i ,j ) for i in [1,3] for j in range(1,5) ]

    def  get_http(self):

        for _url in self.proxy_list:
            tree = self.make_tree(_url)
            for ele in tree.xpath("//tbody//tr/td[3][text()='高匿代理IP']"):
                ip = ele.xpath("../td[1]/text()")[0]
                port = ele.xpath("../td[2]/text()")[0]

                print("{}:{}".format(ip,port))
                self.save_proxy(ip,port,_url)

    def get_https(self):

        for _url in self.proxy_list:
            tree = self.make_tree(_url)
            for ele in tree.xpath("//tbody//tr/td[3][text()='高匿代理IP']"):
                if ele.xpath("../td[4]/text()")[0] =="HTTPS":
                    ip = ele.xpath("../td[1]/text()")[0]
                    port = ele.xpath("../td[2]/text()")[0]

                    print("{}:{}".format(ip, port))
                    self.save_proxy(ip, port,_url ,"https")




