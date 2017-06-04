#!/home/md98/bamboo_env/bin python
# -*- coding: UTF-8 -*-

import readFile
import scaling

if __name__ == '__main__':
    text_file_directory ='../data/'
    for text_file_number in range(40491, 37840, -1):
        text_file_name = str(text_file_number) + '.txt'
        text_file = text_file_directory + text_file_name
        print(text_file)
        readFile.read(text_file)

        output = open('nouns/'+ str(text_file_number)+str('.txt'), "a")
        for noun in scaling.getFilteredData(readFile.data, scaling.filter_pronouns):
            output.write(noun+" ")
        output.close()

