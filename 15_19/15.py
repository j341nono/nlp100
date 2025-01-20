'''
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
'''

import sys
path = './popular-names.txt'

def main():
    args = sys.argv
    value = int(args[1])
    
    with open(path, 'r') as f:
        line = f.readlines()
        count = len(line) - 1
        for i in reversed(range(value)):
            result = line[count - i].replace('\n', '')
            print(result)

if __name__ == '__main__':
    main()


'''
tail -n 5 './popular-names.txt'
'''