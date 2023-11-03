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
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice}", border=0, align="L", ln=1)
    pdf.cell(w=50, h=8, txt=f"Date {date}", border=0, align="L", ln=1)
    pdf.ln(10)
    # Add Headers
    column_name = list(df.columns)
    column_name = [item.replace("_", " ").title() for item in column_name]
    pdf.set_font(family="Times", style="B", size=10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=30, h=8, txt=column_name[0], border=1)
    pdf.cell(w=68, h=8, txt=column_name[1], border=1)
    pdf.cell(w=32, h=8, txt=column_name[2], border=1)
    pdf.cell(w=30, h=8, txt=column_name[3], border=1)
    pdf.cell(w=30, h=8, txt=column_name[4], border=1, ln=1)
    # Add rows
    total_amount = 0
    for index, row in df.iterrows():
        pdf.set_font(family="Times", style="B", size=10)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=68, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=32, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)
        total_amount = total_amount + row["total_price"]

    pdf.set_font(family="Times", style="B", size=10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=8, txt=f"Total: {total_amount}", align="R", border=1, ln=1)
    pdf.ln(10)
    pdf.set_font(family="Times", style="B", size=20)
    pdf.cell(w=0, h=15, txt=f"The total due amount is $ {total_amount} .", align="L",ln=1)
    # ADD company name and logo
    pdf.set_font(family="Times", size=20)
    pdf.cell(w=70, h=10, txt="Your Company name")
    pdf.image("logo.jpg", w=10)

    pdf.output(rf"invoice_pdf\{filename}.pdf")
