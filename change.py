# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def fileformatting():
    import re
    errorlog = open("error_log.txt","w+", encoding = "UTF8")
    for x in range(1,1015):
        try:
            #please change this number
           
            f = open(str(x)+".txt", "r+", encoding = "UTF8")
                
            time = f.readline() # 시간
            
            r = f.read()
            if("<br /" in r):
                r = r.replace("<br />", "")
            
            article = r.split("#대나무")
            for k in range(len(article)):
                if(len(article[k])>1 and article[k][0].isdigit()):
                    bamboo_name = re.search(r'\d+', article[k]).group()
                    article[k] = article[k].replace(bamboo_name, "")
                    newfile = open(bamboo_name+".txt", "w+", encoding = "UTF8")
                    newfile.write(time)
                    newfile.write(article[k])
            print(x)
       
        except:
            errorlog.write(str(x)+'파일이 손상되었음 \n')
    
       
            
            
if __name__ == "__main__":
    fileformatting()

   