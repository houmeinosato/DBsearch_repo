import streamlit as st
import base64

import sys,os
import xlrd
#import win32com.client



file_name       = "研修修了証_幼稚園.xlsx"
sheet_name      = "Sheet1"
excel           = win32com.client.Dispatch("Excel.Application")
修了証ファイル  = excel.Workbooks.Open(file_name)
修了証シート    = 修了証ファイル.WorkSheets(sheet_name)

# ＰＤＦの書き出し先
pdf_name = "修了証_{}{}.pdf".format( "20001231" , "氏名" ) 
pdf = 修了証ファイル.ActiveSheet.ExportAsFixedFormat( 0 , pdf_name )


st.download_button(
    label = "Download ",
    #data = pdf ,
    file_name = pdf_name ,
    mime="pdf"
)
