from functools import wraps
import re
import time

def Count(func, *args, **kwargs):
    """
    统计音乐播放信息
    :param f:
    :param args:
    :param kwargs:
    :return:
    """
    @wraps(func)
    def wrapper(path, *args, **kwargs):
        with open("log.txt", "a") as f:
            # 写入当前时间及播放音乐名称
            f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\t"+re.split(r"\\",path)[-1]+"\n")
            func(path,*args, **kwargs)
    return wrapper