from proxy_utils import ProxyCrawler


class CNProxy(ProxyCrawler):

    start_url = "http://cn-proxy.com/archives/218"


    def  get_http(self):
        tree = self.make_tree(self.start_url)
        for ele in tree.xpath("//tbody//tr/td[3][text()='高度匿名']"):
            ip = ele.xpath("../td[1]/text()")[0]
            port = ele.xpath("../td[2]/text()")[0]

            print("{}:{}".format(ip,port))
            self.save_proxy(ip,port ,self.start_url)



