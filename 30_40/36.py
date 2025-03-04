'''
36. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
'''
import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np 
from a30 import processing
from a35 import frequency

def main():
    mapping = processing()
    c = frequency(mapping)
    top10 = c.most_common()[:10]
    
    # 棒グラフを作成
    x_var = []
    y_var = []
    for i, word in enumerate(top10):
        x_var.append(word[0])
        y_var.append(word[1])
    
    plt.bar(x_var, y_var)
    plt.show()
    
if __name__ == '__main__':
    main()