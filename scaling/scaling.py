#!/home/md98/bamboo_env/bin python
# -*- coding: UTF-8 -*-


# python version 3.5
# requirement library
# jpype1  version 0.6.2
# konlpy version 0.4.4


# system
# Linux Mint 18.1 Serena
# Linux version 4.4.0-53-generic (buildd@lcy01-28) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.4) ) #74-Ubuntu SMP Fri Dec 2 15:59:10 UTC 2016
# java version "1.7.0_80"
# Java(TM) SE Runtime Environment (build 1.7.0_80-b15)
# Java HotSpot(TM) 64-Bit Server VM (build 24.80-b11, mixed mode)

from konlpy.tag import Hannanum
from konlpy.tag import Twitter

H = Hannanum()
T = Twitter()
filter_pronouns = ['나', '너', '우리', '저', '저희', '그', '그녀', '그것', '것', '자기', '자네', '누구', '누구나', '아무', '아무나', '내']
def filtering_data(data:str, filter:list):
    '''
:param data: text data (type : str)
       filter : don't want data (If filter doesn't have pronouns, filtered text list has pronouns. So I recommend 
filter = filter + scaling.filter_pronouns

:return: filtered text list (type : str list)


this method uses Hannanum and Twitter from konlpy.tag

H means Hannanum()
T means Twitter()

Tip!
if Data has a lot of white space, it takes a lot of time.
I don't know why.
But I think that the reason is konlpy.

Used : 

data = """너에게 묻는다.
- 안도현 -
너에게 묻는다
연탄재 함부로 발로 차지 마라
너는 누구에게 한번이라도 뜨거운 사람이었느냐

반쯤 깨진 연탄
언젠가는 나도 활활 타오르고 싶을 것이다
나를 끝 닿는데까지 한번 밀어붙여 보고 싶은 것이다

타고왔던 트럭에 다시 실려 돌아가면
연탄, 처음으로 붙여진 나의 이름도 으깨어져
나의 존재도 까마득히 뭉개질 터이니
죽어도 여기서 찬란한 끝장을 보고 싶은 것이다

나를 기다리고 있는 찬란한 밑불위에
지금은 인정머리없는 차가운 내 몸을 얹고
아랫쪽부터 불이 건너와 옴겨 붙기를
시간의 바통을  내가 넘겨 받는 순간이 오기를
그리하여 서서히 온몸이 벌겋게 달아오르기를
나도 느껴보고 싶은 것이다
나도 보고 싶은 것이다

모두들 잠든 깊은 밤에 눈에 발갛게 불을 켜고
구들장 속이 얼마나 침침한지 손을 뻗어보고 싶은 것이다
나로 하여 푸근한 잠 자는 처녀의 등허리를
밤새도록 슬금슬금 만져도 보고 싶은 것이다
"""
filter_set = []
import scaling
filter_set= filter_set+scaling.filter_pronouns
scaled_data = scaling.filtering_data(data, filter_set)
print(type(scaled_data)) # <class 'list'>
print(type(scaled_data[0])) # <class 'str'>
print(scaled_data) # ['안도현', '연탄재', '발', '한번', '사람', '연탄', '끝', '한번', '트럭', '연탄', '처음', '이름', '뭉개질', '터', '여기', '끝장', '지금', '몸', '아랫쪽', '불', '옴겨', '시간', '바통', '순간', '오기', '온몸', '밤', '눈', '불', '구들장', '손', '처녀']


    '''
    h_nouns = H.nouns(data)
    t_nouns = T.nouns(data)


    filtered_nouns = []


    for word in h_nouns:
        if word in t_nouns:
            if word not in filter:
                filtered_nouns.append(word)
    return filtered_nouns

def check_count_nouns(nouns_list:list):
    '''
    
    :param nouns_list: scaling nouns data list
    
    :return: 
    dictionary {word: frequency}
    '''
    d ={}
    for word in nouns_list:
        if word in d.keys():
            d[word] += 1
        else:
            d[word] = 1

    return d


def most_common_words_filter(deep:int):
    '''
    
    :param deep: top #(deep) in most_common_korean_words.txt
    :return: fileter most_common_words
    usage:
    filter = filter+scaling.most_common_words_filter(100)
    scaled = scaling.filtering_data(data, filter)
    '''
    f = open("most_common_korean_words.txt")
    most_common_words = []
    for i in range(deep):
        most_common_word = f.readline().rstrip('\n')
        most_common_words.append(most_common_word)

    return most_common_words


if __name__ == "__main__":

    text_file_directory = 'data/'

    text_file_number = 40030
    text_file_name = str(text_file_number) + '.txt'

    text_file = text_file_directory + text_file_name

    f = open(text_file)

    data = f.read()

    pos_data = T.pos(data, norm= True)

    for i in enumerate(pos_data):
        if pos_data[i[0]][1] =='Josa':
            print(pos_data[i[0]-1])

