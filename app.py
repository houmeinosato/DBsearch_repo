import streamlit as st
import pdfkit
import reportlab

# Streamlitのタイトルと説明文
st.title("StreamlitでPDF作成")
st.markdown("このアプリでは、StreamlitでPDFファイルを作成する方法を紹介します。")

# StreamlitのファイルアップローダーでHTMLファイルを選択
uploaded_file = st.file_uploader("HTMLファイルを選択してください", type="html")

# HTMLファイルが選択された場合
if uploaded_file is not None:
    # HTMLファイルの内容を読み込む
    html = uploaded_file.read()

    # PDFファイルの名前を入力する
    pdf_name = st.text_input("PDFファイルの名前を入力してください", value="output.pdf")

    # PDFファイルの作成ボタンを表示する
    create_button = st.button("PDFファイルを作成")

    # PDFファイルの作成ボタンが押された場合
    if create_button:
        # pdfkitを使ってHTMLファイルをPDFファイルに変換する
        pdfkit.from_string(html, pdf_name)

        # reportlabを使ってPDFファイルをバイナリデータに変換する
        with open(pdf_name, "rb") as f:
            pdf_data = f.read()

        # StreamlitのダウンロードボタンでPDFファイルをダウンロードできるようにする
        st.download_button("PDFファイルをダウンロード", pdf_data, file_name=pdf_name, mime="application/pdf")
