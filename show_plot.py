import pandas as pd
import matplotlib as mtp
mtp.use("Agg")
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
import matplotlib.pyplot as plt


def print_pie(counts_dict, field):
    print("this output show_Image!")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    labels =['{}:{}'.format(index, value) for index,value in counts_dict.items()]
    fig = plt.figure(figsize=(8,8))
    ax1 = fig.add_subplot(111)
    ax1.set_title("{field} 统计饼状图".format(field=field
                                         ))
    values = list(counts_dict.values())
    explode = [0 for value in values]
    explode[0] += 0.1
    ax1.pie(values, labels=labels, explode=explode, shadow=True)
    plt.savefig('static/images/tempShow.jpg')
    
    
def counts_max(ser, max_num):
    ser = ser.value_counts()
    counts_dict = {}
    num = 0
    for index, value in ser.items():
        if num < max_num:
            if index == '':
                continue
                index = "未统计"
            counts_dict[index] = value
        elif num == 10:
            counts_dict["其他"] = value
        else:
            counts_dict["其他"] += value
        num += 1
    return counts_dict
    

if __name__ == "__main__":
    df = pd.read_csv("tempDfXXX.csv")
    counts = counts_max(df['标本'], 10)
    print_pie(counts, "标本")
