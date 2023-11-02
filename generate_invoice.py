import pandas as pd
from fpdf import FPDF
# glob module is used to find all the path names with a matching specified pattern
import glob
# To extract the file name
from pathlib import Path

filepaths = glob.glob("invoices/*xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    filename = Path(filepath).stem
    invoice, date = filename.split(sep="-")[0], filename.split(sep="-")[1]

    pdf = FPDF(orientation="p", unit="mm", format="a4")
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=20)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice}", border=0, align="L", ln=1 )
    pdf.cell(w=50, h=8, txt=f"Date {date}", border=0, align="L", ln=1)

    pdf.set_font(family="Times", style="B", size=15)
    pdf.cell(w=0, h=10, txt=df, )
    pdf.output(rf"invoice_pdf\{filename}.pdf")
