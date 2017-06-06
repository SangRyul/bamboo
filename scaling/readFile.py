#!/home/md98/bamboo_env/bin python
# -*- coding: UTF-8 -*-

import datetime
import os



def read(textfilename:str):
    if os.path.isfile(textfilename):
        f = open(textfilename)

        global date
        global data
        date = datetime.datetime.strptime(f.readline(), "%Y년 %m월 %d일 %p %H:%M ")
        data = f.read()

        f.close()

    else:
        print("No file : "+textfilename)
        data = ''
