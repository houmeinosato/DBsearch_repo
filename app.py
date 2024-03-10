import streamlit as st

import base64

'''
#from fpdf import FPDF
pdf = FPDF()  # pdf object
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

pdf.set_font("Times", "B", 11)
pdf.set_xy(10.0, 20)
pdf.cell(w=75.0, h=5.0, align="L", txt="This is my sample text")
'''

import datetime
import sys,os
import xlrd
import win32com.client



yyyy    = datetime.datetime.now().strftime('%Y')        #文字列4桁
mm      = datetime.datetime.now().strftime('%m')        #文字列2桁
dd      = datetime.datetime.now().strftime('%d')        #文字列2桁


#global 研修実績データ件数 , 研修実績データ番号 , 研修実績データ

if(len(sys.argv)<2):
    パス = os.getcwd()
    print("os.getcwd:",パス)
else:
    パス = sys.argv[1]
    print("sys.argv[1]:",パス)

絶対指定フォルダー名 = パス
file_name       = "研修修了証_幼稚園.xlsx"

sheet_name      = "Sheet1"
abs_file_name   = os.path.join(パス, file_name)
excel           = win32com.client.Dispatch("Excel.Application")
修了証ファイル  = excel.Workbooks.Open(abs_file_name)
修了証シート    = 修了証ファイル.WorkSheets(sheet_name)

# ＰＤＦの書き出し先
pdf_name = "修了証_{}{}.pdf".format( "20001231" , "氏名" ) 
abs_pdf_name = os.path.join( パス , pdf_name )
#print('===='+絶対指定フォルダー名+'======abs_pdf_name:'+pdf_name+"/"+abs_pdf_name)
pdf = 修了証ファイル.ActiveSheet.ExportAsFixedFormat(0,abs_pdf_name)


st.download_button(
    label = "Download ",
    data = pdf_name ,

    file_name = pdf_name ,
    mime="application/pdf"
)
