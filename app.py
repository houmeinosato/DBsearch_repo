import streamlit as st
import base64
from fpdf import FPDF

# PDFファイルを生成する関数
def create_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Streamlit PDFダウンロードデモ", ln=True, align='C')
    # その他のPDFの内容をここに追加


    
    return pdf.output(dest='S').encode( 'utf-8'  )

# Base64でエンコードしてダウンロードリンクを生成する関数
def create_download_link(pdf_content):
    b64 = base64.b64encode(pdf_content).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="your_document.pdf">Download PDF file</a>'
    return href

# Streamlitのボタンを使用してPDFをダウンロードする
if st.button('PDFをダウンロード'):
    pdf = create_pdf()
    st.markdown(create_download_link(pdf), unsafe_allow_html=True)


# サロゲートペアを削除する関数
def remove_surrogates(text):
    return text.encode('utf-8', 'ignore').decode('utf-8')

# PDFファイルを作成する関数
def create_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    # ページにテキストを追加する前に、サロゲートペアを削除する
    text = remove_surrogates("This is a test with a surrogate pair: \ud800")
    pdf.cell(40, 10, text)
    return pdf.output(dest='S').encode('utf-8')
