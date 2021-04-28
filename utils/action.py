
import time
from playsound import playsound
from multiprocessing import Process

from utils.Decorator import Count


import os
from utils.settings import AudioFormat,MusicPath

def GetMusicList(MusicPath):
    dir_list = os.listdir(MusicPath)
    # 问题：是否可以通过其他方式匹配文件，加快匹配速率
    music_list = [i for i in dir_list if i[-3:] in AudioFormat] # 获取当前文件中的所有mp3、wav格式的数据
    return music_list

# 用于存放播放子进程的列表（可以使用进程池）
l = []

# 播放
@Count
def play(path):
    """
    音乐播放
    :param path:音乐路径
    :return:
    """

    p = Process(target=playsound, args=(path,))
    l.append(p) # 添加至进程列表，默认之播放一首，保证里面只有一个对象
    p.daemon = True # 设置守护进程

    p.start()  # 启动线程，即让线程开始执行

# 结束
def end():
    """
    结束当前子进程（关闭当前音乐）
    :return:
    """
    try:
        l[0].terminate() # 结束当前进程
        l.pop(0) # 删除对象
    except IndexError:
        pass

# if __name__ == "__main__":
#     p = Process(target=play, args=("../music_data/sold out.mp3",)) # 测试
#     p.start() #启动线程，即让线程开始执行

