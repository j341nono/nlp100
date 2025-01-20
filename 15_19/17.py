'''
17. １列目の文字列の異なり

1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはcut, sort, uniqコマンドを用いよ．
'''

path = './popular-names.txt'

def main():
    with open(path, 'r') as f:
        line = f.readlines()
        # map: 指定した関数(lambda)をリスト等の各要素に対して適用し、新しいリストとして返す
        name = map(lambda x: x.split('\t')[0], line)
        name = set(name)
    name = sorted(name)
    print(name)

if __name__ == '__main__':
    main()

'''
! cut -d $'\t' -f 1 './popular-names.txt'|uniq
'''