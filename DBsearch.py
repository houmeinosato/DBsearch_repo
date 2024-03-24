import streamlit as st

import sqlite3
import pandas as pd

import datetime
import sys,os




yyyy    = datetime.datetime.now().strftime('%Y')        #文字列4桁
mm      = datetime.datetime.now().strftime('%m')        #文字列2桁
dd      = datetime.datetime.now().strftime('%d')        #文字列2桁



#------------------------------------------------------------------------------------------------------------------------------ 1 ------------------
def 受講情報表示():             ######################################################################################### 3 ####################



    st.title('個人情報につき取扱注意')
    
    st.write('研修名と(ｼ)メイの一部から対象を検索します')
    
    Val選択研修名   = st.text_input("研修名")
    Val選択メイ     = st.text_input("メ　イ")
    
    ## ボタン
    if st.button("検索実行"):
      

        検索条件 = ""
        if  Val選択研修名  == '':                   # 対象－研修名
            if  Val選択メイ  == '':                   # 対象－研修名
                pass

            else:
                検索条件 =    " メイ   LIKE '%" + Val選択メイ + "%' "            
            
        else:        
            検索条件  =  "    研修名   LIKE '%" + Val選択研修名 + "%' "
            if  Val選択メイ  == '':                   # 対象－研修名
                pass
            else:
                検索条件 +=  " AND メイ LIKE '%" + Val選択メイ + "%' "              
        
        if 検索条件 == "":
            pass
            #st.popup("研修名かメイを入力してください")

        else:

            print(検索条件)            

            # データベース
            dbname = 'Careerup.db'
            conn = sqlite3.connect(dbname)
            # cur = conn.cursor()
            tblname = 'Kensyu_jisseki'

            # 抽出
            sql_select = "SELECT 研修名, 修了番号, 研修区分, 研修分野, 研修時間, 姓, セイ, 名, メイ, 生年月日, 保育士県名, 保育士番号, 個人電話, 自宅住所  FROM '" +  tblname + "'  where  " + 検索条件 
            df = pd.read_sql_query( sql_select , conn)
            st.write(df)


    return 


   
if __name__ == '__main__':
    
    受講情報表示()
    

