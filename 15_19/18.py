'''
18. 各行を3コラム目の数値の降順にソート

各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ
（この問題はコマンドで実行した時の結果と合わなくてもよい）．
'''

path = 'popular-names.txt'

def main():
    with open(path, 'r') as f:
        line = f.readlines()
        line = map(lambda x: x.replace('\n', ''), line)
        line = list(map(lambda x: x.split('\t'), line))
        output = sorted(line, key=lambda x: int(x[2]), reverse=True)
    print(output[:10]) # 10個表示

if __name__ == '__main__':
    main()
    
'''
sort -n -r -k 3,3 -t " " "./popular-names.txt"

-n
数値としてソートする（数値順に並び替える）

-r
逆順（降順）でソートする

-k 3,3
3列目だけを基準にしてソートする
3,3 は「3列目から3列目まで」という意味で、ソート対象を限定する

-t " "
フィールドの区切り文字（デリミタ）を指定する。ここでは空白（スペース）を区切り文字として指定している。
'''