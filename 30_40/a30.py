'''
30. 形態素解析結果の読み込み

形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），
品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素
（マッピング型）のリストとして表現せよ．第4章の残りの問題では，
ここで作ったプログラムを活用せよ．
'''

from pprint import pprint
path = './neko.txt.mecab'

def processing():
        with open(path, 'r',encoding='utf-8')as f:
            general_list = []
            neko_list = []
            lines = f.readlines()
            for text in lines:
                neko_dic = {}
                suf = text.split("\t")
                if suf[0] == "EOS\n":
                    continue
                temp = suf[1].split(',')
                neko_dic["surface"] = suf[0]
                if len(temp) <= 7:
                    neko_dic["base"] = suf[0]
                else:
                    neko_dic["base"] = temp[6]
                neko_dic["pos"] = temp[0]
                neko_dic["pos1"] = temp[1]
                neko_list.append(neko_dic)
                if suf[0]=="。":
                    general_list.append(neko_list)
                    neko_list = []
        return general_list

def main():
    ans = processing()
    pprint(ans[:2])
    
if __name__ == '__main__':
    main()


'''
sufの中身
['な', '助動詞,*,*,*,特殊・ダ,体言接続,だ,ナ,ナ\n']
['艶', '名詞,一般,*,*,*,*,艶,ツヤ,ツヤ\n']
['っぽい', '形容詞,接尾,*,*,形容詞・アウオ段,基
            
'''