import requests
import re
from utils.settings import headers,proxies
# 爬虫程序需要经常维护，如果程序不能正常获取数据需要对页面进行分析，对程序做修改
def get_music(id,name,proxies=proxies, headers=headers):
    """
    通过网易云外链获取音乐文件
    :param id: 歌曲对应的ID
    :param name: 歌曲名称，用于保存文件
    :param proxies:
    :param headers:
    :return:
    """
    URL = "url"%id
    try:
        response = requests.get(URL, proxies=proxies, headers=headers)
        with open("./music_data/%s.mp3"%name, "wb") as f:
            f.write(response.content)
            print("%s 下载成功"%name)
    except Exception:
        print("%s 下载失败"%name)

def getID(artist_id):
    """
    根据歌手的ID获取其对应页面的所有歌曲ID（歌手的ID可以通过网易云歌手页面查看）
    如，https://music.163.com/#/artist?id=2116（对应^陈奕迅^）
    :param artist_id:
    :return:
    """
    URL = "url"%artist_id # 原址中的#删掉
    response = requests.get(URL, proxies=proxies, headers=headers)
    # 使用正则表达式将歌曲信息匹配出来
    # <a href="/song?id=65766">富士山下</a>
    data = re.findall(r'<a href="/song\?id=([0-9]+)">(.*?)</a>',response.text)
    # 返回数据
    # 思考：因为playsound不支持中文路径，如何在此处结合之前的播放逻辑做出修改呢？
    return data

if __name__ == "__main__":
    data = getID(2116)
    for id,name in data:
        get_music(id,name)
