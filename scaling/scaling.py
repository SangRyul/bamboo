#!/home/md98/bamboo_env/bin python
# -*- coding: UTF-8 -*-



from konlpy.tag import Hannanum
from konlpy.tag import Twitter

H = Hannanum()
T = Twitter()
filter_pronouns = ['나', '너', '네','우리', '저', '저희', '그', '그녀', '그것', '것', '자기', '자네', '누구', '누구나', '아무', '아무나', '내']
def getFilteredData(data:str, filter:list):
    h_nouns = H.nouns(data)
    t_nouns = T.nouns(data)


    output = []



    for word in h_nouns:
        if word in t_nouns:
            if word not in filter:
                output.append(word)
    return output

def getCountNouns(nouns:list):
    '''
    
    :param nouns: scaling nouns data list
    
    :return: 
    dictionary {word: frequency}
    '''
    countNouns ={}
    for word in nouns:
        if word in countNouns.keys():
            countNouns[word] += 1
        else:
            countNouns[word] = 1

    return countNouns


def getMostCommonWords(deep:int):
    '''
    
    :param deep: top #(deep) in most_common_korean_words.txt
    :return: fileter commonWords
    usage:
    filter = filter+scaling.most_common_words_filter(100)
    scaled = scaling.filtering_data(data, filter)
    '''
    f = open("most_common_korean_words.txt")
    commonWords = []
    for i in range(deep):
        wordlist = f.readline().rstrip('\n')
        commonWords.append(wordlist)

    return commonWords


##if __name__ == "__main__":

