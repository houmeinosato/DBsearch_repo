import streamlit as st
from fpdf import FPDF
import base64

pdf = FPDF()  # pdf object
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

pdf.set_font("Times", "B", 11)
pdf.set_xy(10.0, 20)
pdf.cell(w=75.0, h=5.0, align="L", txt="This is my sample text")
pdf.set_font("Times", , 13)
pdf.set_xy(20.0, 30)
pdf.cell(w=75.0, h=5.0, align="L", txt="This is my sample text")

st.download_button(
    "Download Report",
    data=pdf.output(dest='S').encode('latin-1'),
    file_name="Output.pdf",
)


