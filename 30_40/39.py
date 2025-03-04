"""
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
"""
from a30 import processing
import collections
import matplotlib.pyplot as plt
import japanize_matplotlib

def main():
    mapping = processing()
    word_list = []
    for sentense in mapping:
        for text in sentense:
            word_list.append(text["surface"])
    data = collections.Counter(word_list)
    temp = sorted((data.values()), reverse = True)
    plt.plot(temp)
    plt.xlabel('出現頻度順位')
    plt.ylabel('出現頻度')
    ax = plt.gca()
    ax.set_yscale('log')  # メイン: y軸をlogスケールで描く
    ax.set_xscale('log')
    plt.show()

if __name__ == "__main__":
    main()
    
    
"""
出現頻度がk番目に大きい要素が、1位のものの頻度と比較して 1/kに比例するという経験則である
-> 両対数グラフで描くと直線になる

--> ある特定の文脈では、その領域で頻出する単語が多く現れ、逆に一般的でない単語はほとんど出てこない
"""