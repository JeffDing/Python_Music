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
    "Cookie": """_iuqxldmzr_=32; _ntes_nnid=c47d3c4dbb92dcd4eb3b8f6c7975ea97,1600494261864; _ntes_nuid=c47d3c4dbb92dcd4eb3b8f6c7975ea97; WM_TID=OGgKWy+A1ndFBVQVBEMp+xMZag2wsR6w; ntes_kaola_ad=1; NMTID=00OKRDnkVD7JQLytEPUikd8USHR2v4AAAF1WcSywQ; UM_distinctid=17780b337373f8-087f97ea5e1aa2-33e3567-1e6000-17780b33738a6b; WEVNSM=1.0.0; WNMCID=iaedft.1618812859545.01.0; WM_NI=+LzeOKKAhehQ1Bhz8d7+N7lZCVI3nOn+MwN57XzOySnjM+0QXg6qNqupskPNwX/0MNtz7c2XJ0yxJvUzuc0JeI6xlqPPfIkulrYJ6lH8IN3WT8yx7JFE97AaoS8JvA0jOFc=; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb8d248f68da8a8c57daa868bb7d14f878b9fbaf8688da68e95d425b390f9acf82af0fea7c3b92ae994b686ce41899fa886eb5bf39ea89bbb70f5f582d8ef52818a87d4ed45aef58398cd3ff588b6b0fc59aeb683ccb35b9cb9fa92cd7bb7b0bd8cd346b588e1d1d046b8a6f984b1548af0b799c97e97a6bb84b342a797fa99ef7b9490aaaaea7fb0ae97abb5688ce887afb25d98e8b799b642869bf7d8c46bad8df8abf54bf4b681a7e237e2a3; playerid=14295087; JSESSIONID-WYYY=Nhq2funCKNGD2WSrc41Qwx0UwVAHDpyZcSpU4ypwyu9EJuHrUf+qQIP9MnIVW8l/Uv0Qm9RC1JgGlcHKpps2\9dswmND+cy78fxt1RGsTkibyyEpt2e7N4XQSu8k0ZC4cSFASxy100C26jn4IrcfgaX\GGz77JliOoGiYCZ0ImAZ6gGI:1618816399840"""
}

proxies = {
    "HTTP": "49.86.178.152:9999"
}