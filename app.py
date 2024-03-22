import streamlit as st

import sqlite3
import pandas as pd

#import csv

import datetime
import sys,os




yyyy    = datetime.datetime.now().strftime('%Y')        #文字列4桁
mm      = datetime.datetime.now().strftime('%m')        #文字列2桁
dd      = datetime.datetime.now().strftime('%d')        #文字列2桁


#global 研修実績データ件数 , 研修実績データ番号 , 研修実績データ




#------------------------------------------------------------------------------------------------------------------------------ 1 ------------------


def 年月日8桁(年月日):
    #年月日 = "2024/1/1"
    target = '/'
    idx1 = 年月日.find(target)
    年 = 年月日[:idx1]
    月日 = 年月日[len(年) + 1:]
    idx2 = 月日.find(target)
    月 = ("0" + 月日[:idx2])[-2:]
    日 = ("0" + 月日[idx2 + 1:])[-2:]
    結果 = 年 + 月 + 日
    #print(結果)
    return 結果

def 年月日10桁(年月日):
    #年月日 = "2024/1/1"
    target = '/'
    idx1 = 年月日.find(target)
    年 = 年月日[:idx1]
    月日 = 年月日[len(年) + 1:]
    idx2 = 月日.find(target)
    月 = ("0" + 月日[:idx2])[-2:]
    日 = ("0" + 月日[idx2 + 1:])[-2:]
    結果 = 年 + "/" + 月 + "/" +日
    #print(結果)
    return 結果







#--------------------------------------------------------------











def 受講情報表示():             ######################################################################################### 3 ####################



    st.title('運用を停止しております。')
    
    st.write('別サイトに移行しましたので、必要な方はご連絡ください。')
    
    

   

    return 


 
    



   
if __name__ == '__main__':
    
    受講情報表示()
    

