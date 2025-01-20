'''
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
'''

import sys
path = './popular-names.txt'

def main():
    arg = sys.argv
    n = arg[1]
    n = int(n)
    
    with open(path, 'r') as f:
        text = f.read().split('\n')
        text = text[:-1]

        part = len(text) // n
        remainder = len(text) % n

        parts = []
        for i in range(n):
            start = i * part
            if i < n - 1 or remainder == 0: # 終了idxを次に
                end = (i + 1) * part
            else:#最後のブロック
                end = len(text)  # 最後の部分を含める
            parts.append(text[start:end])

        for i, part in enumerate(parts):
            part = ''.join(part)
            print(f"Part {i + 1}:\n", part)
    
if __name__ == '__main__':
    main()
    

'''
split -n 3 -d --additional-suffix=.txt "./popular-names.txt"

https://eng-entrance.com/linux-command-split#i
'''

'''
(example)
len(text)=7, n=3
when i=0 start=0 end=2 text[0,2] ['line1', 'line2']
when i=1 start=3 end=4 text[3,4] ['line3', 'line4']
when i=2 start=4 end=7 text[4,7] ['line5', 'line6', 'line7']
'''