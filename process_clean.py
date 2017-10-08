import psutil
import subprocess

'''本来是担心 有些用了phantomJS的爬虫 出现异常导致phantomJS 导致进程驻留 。
一般情况下爬虫程序在finally里面加个quit ，基本不会出现这种情况。所以此文件可视情况运行'''


def kill_phantomjs( ):
    pids = psutil.pids()
    aim_num =0
    for pid in pids:
        try:
            p = psutil.Process(pid).cmdline()
            if len(p) >1:
                p_str = "".join(p)
                if "phantomjs" in p_str:
                    aim_num +=1
                    subprocess.Popen("kill {}".format(pid))
            print("遗留{}个".format(aim_num))
        except Exception as e:
            print("执行错误：{}".format(e))


