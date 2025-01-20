'''
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる

各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
'''

import itertools
path = 'popular-names.txt'

def main():
    with open(path, 'r') as f:
        line = f.readlines()
        line = map(lambda x: x.replace('\n', ''), line)
        line = list(map(lambda x: x.split('\t'), line))
        
    line = sorted(line, key=lambda num: num[0]) # 1列目は名前(A-Z)
    grouped = [(k, len(list(g))) for k, g in itertools.groupby(line, lambda num : num[0])] # 名前で
    grouped = sorted(grouped, key=lambda num : num[1], reverse=True)
    for key, count in grouped:
        print(key, count)

if __name__ == '__main__':
    main()

'''
cut -f1 "./popular-names.txt" | sort | uniq -c | sort -nr
'''

'''
itertools
(リストの)連続する同じ値の要素をグループ化

l = [0, 0, 0, 1, 1, 2, 0, 0]
print([(k, list(g)) for k, g in itertools.groupby(l)])
# [(0, [0, 0, 0]), (1, [1, 1]), (2, [2]), (0, [0, 0])]
'''