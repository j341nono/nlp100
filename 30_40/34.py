'''
34. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
'''

from a30 import processing

def main():
    mapping = processing()
    ans = []
    for sentence in mapping:
        cnt = 0
        bf = ''
        for i in range(len(sentence)):
            if sentence[i]['pos']=='名詞':
                cnt += 1
                bf += sentence[i]['surface']
            else:
                if cnt >= 2:
                    ans.append(bf)
                cnt = 0
                bf = ''
    print(set(ans))
        
if __name__ == '__main__':
    main()