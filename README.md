# PROXYPOOL
搭建代理IP池

## 如何运行
- 安装虚拟环境，我的环境是*python3.5*， 安装第三方库redis ,安装PhantomJs。
- 配置好 *proxy_config.py* 中的 *redis*地址 
- 直接运行抓取程序*python  proxy_run.py* 运行清洗程序 *proxy_wash.py*

## 如何扩展抓取网站
- 直接在*proxys*文件夹内添加抓取程序文件xxx.py
- 新的抓取class 需要继承*ProxyCrawler*类 ，然后实现get_http 或get_https 方法 
- 基于PhantomJS的爬虫需要做好异常处理，在finally中关闭phantomjs。或执行process_clean.sh

## api配置
-  可设置缓存时间 *cache_time*  和一次性请求个数 *proxy_num* 
-  比如 直接 *GET* http://host:port/proxy/http/100* 将返回 100个 http的ip
-  如果结合我前面 [SimpleDistributed-Spider](https://github.com/summerlove66/SimpleDistributed-Spider) 来用的话
需将cache_time =0 


