import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Matplotlib中文显示
mpl.rcParams['font.sans-serif'] = "Microsoft YaHei"
mpl.rcParams['axes.unicode_minus'] = False


def Analysis(path="log.txt"):
    """"
    获取日志文件中的一些统计性描述
    return:DataFrame,音乐播放次数，
    """
    # 思考：如果不是txt文件而是用其他格式，如json、csv改如何修改前面的代码以及后续的代码呢？
    with open("log.txt", "r") as f:
        data_list = f.readlines()
        data_list = [i.strip() for i in data_list]
    data = [i.split("\t") for i in data_list]
    arr = np.array(data)
    df = pd.DataFrame(arr[:, 1], index=arr[:, 0], columns=["song"])
    record = df["song"].value_counts()  # 统计各个音乐播放次数

    return df, record

def Visualization(data):
    """
    使用柱状图进行可视化
    :param data:
    :return:
    """
    plt.figure()
    # 思考：如果换做其他图形，如折线图如何展示呢？
    plt.plot(data.index,data.values) #plot折线图,bar柱状图
    plt.xlabel("song")
    plt.ylabel("num")
    plt.show()

if __name__ == "__main__":
    _,df = Analysis() # 此处只对于统计量可视化，对于没有用的数据可以用_接收表示后续不会用
    Visualization(df)