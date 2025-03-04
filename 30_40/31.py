'''
31. 動詞
動詞の表層形をすべて抽出せよ．
'''
from a30 import processing

def main():
    mapping = processing()
    verb_surface = []
    for sentence in mapping:
        for text in sentence:
            if text['pos'] == '動詞':
                verb_surface.append(text['surface'])
    print(set(verb_surface))
        
if __name__ == '__main__':
    main()