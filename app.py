from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
import os

# ユーザのデスクトップのディレクトリを取得
file = "sample.pdf"
file_path = os.path.expanduser("~") + "/Desktop/" + file

# A4の新規PDFファイルを作成
page = canvas.Canvas(file_path, pagesize=portrait(A4))

# フォントの読み込み
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Windowsに標準で入っているゴシックと明朝のフォントを読み込む
pdfmetrics.registerFont(TTFont("HGRGE", "C:/Windows/Fonts/HGRGE.TTC"))
pdfmetrics.registerFont(TTFont("HGRME", "C:/Windows/Fonts/HGRME.TTC"))

# フォントを設定
page.setFont("HGRGE", 20)

# 文字を書き込む
page.drawString(200, 300, "こんにちは、世界！")
page.drawCentredString(200, 200, "こんにちは、世界！")
page.drawRightString(200, 100, "こんにちは、世界！")

# PDFファイルとして保存
page.save()
