# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 11:51:00 2017

@author: ksl97
"""


import goslate


#인터넷 연결한 상태로 할것
#많이하면 안되더


def translate(filename):
    fread = open(filename,"r+" ,encoding = "UTF8")
    ftranslate = open("Korean_to_English.txt", "w+", encoding = "UTF8")
        
    gs = goslate.Goslate()
      
    
    while(True):
            
        line = fread.readline()
        trans = gs.translate(line, "eng")
            
        if(not line):
            break
        print(line +  " "+ gs.translate(line, "eng"))
        ftranslate.write(trans+"\n")
            
        
    fread.close()
    ftranslate.close()

#testing
translate("most_common_korean_words.txt")








    

