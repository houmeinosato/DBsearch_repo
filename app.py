# app.py
import streamlit as st
import pandas as pd
from fpdf import FPDF

# エクセルシートのファイル名
excel_file = "sample.xlsx"

# エクセルシートを読み込む
df = pd.read_excel(excel_file)

# データフレームを表示する
st.write(df)

# PDFとしてダウンロードする関数
def download_pdf():
    # PDFオブジェクトを作成する
    pdf = FPDF()
    # ページを追加する
    pdf.add_page()
    # フォントを設定する
    pdf.set_font("Arial", size=12)
    # データフレームの各行をPDFに書き込む
    for i in range(len(df)):
        row = df.iloc[i]
        pdf.cell(200, 10, txt=str(row), ln=i+1, align="L")
    # PDFをメモリに保存する
    pdf.output("output.pdf", "S")
    # PDFをバイナリデータとして返す
    return pdf.output(dest="S")

# PDFとしてダウンロードするボタンを追加する
if st.button("Download PDF"):
    # PDFデータを取得する
    pdf_data = download_pdf()
    # PDFデータをダウンロードできるようにする
    st.download_button("Download PDF", pdf_data, file_name="output.pdf", mime="application/pdf")
