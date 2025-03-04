"""
単語の出現頻度のヒストグラムを描け．ただし，横軸は出現頻度を表し，1から単語の出現頻度の最大値までの線形目盛とする．
縦軸はx軸で示される出現頻度となった単語の異なり数（種類数）である．
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
    plt.hist(data.values(), range(1, 40)) # 40以上はなさそう
    plt.show()
    
if __name__ == "__main__":
    main()