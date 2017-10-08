from proxy_utils import ProxyCrawler
from selenium import webdriver
import platform
import lxml.html


start_url = "https://nyloner.cn/proxy"
class NYProxy(ProxyCrawler):



    def get_http(self):

        if platform.system() == "Linux":
            b = webdriver.PhantomJS()
        else:
            b = webdriver.Chrome()
        b.implicitly_wait(20)
        try:
            http_url_text_list =[]

            b.get(start_url)
            http_url_text_list.append(b.page_source)
            for i in range(6):
                next_click = b.find_element_by_css_selector("button#next-page")
                next_click.click()
                http_url_text_list.append(b.page_source)
            b.quit()
            for html  in http_url_text_list:
                tree = lxml.html.fromstring(html)
                for row in tree.xpath("//tbody//tr"):

                    ip =row.xpath("./td[2]/text()")[0]
                    port=row.xpath("./td[3]/text()")[0]


                    self.save_proxy(ip, port ,start_url)

        except:
            b.quit()

        finally:
            b.quit()

