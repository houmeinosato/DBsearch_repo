from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

doc = SimpleDocTemplate("table_pdf.pdf", pagesize=letter)
data = [["col1", "col2", "col3"],
        [1, 2, 3],
        [4, 5, 6]]

table = Table(data)
table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                           ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                           ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                           ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                           ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                           ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                           ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

elements = [table]
doc.build(elements)
