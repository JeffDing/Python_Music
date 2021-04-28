import os
import sys
# 获取根目录
Base_Dir = os.path.abspath("../")
# 设置工程目录为导入工具包的搜索路径
sys.path.append(Base_Dir)
# 设置音乐路径
MusicPath = ".\\music_data\\"#  可以直接基于根目录设置Base_Dir+"\\music_data\\"
# 将当前支持的音乐格式放置在列表中
AudioFormat = ["MP3","mp3",] # 当前支持音频的格式


# 爬虫部分
headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
    "Cookie": """Cookie信息"""
}

proxies = {
    "HTTP": "49.86.178.152:9999"
}
