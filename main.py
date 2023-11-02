# fpdf is file and FPDF is a class used to generate pdf instances
from fpdf import FPDF
import pandas as pd

# pdf is an instance of the FPDF class
pdf = FPDF(orientation="p", unit="mm", format="a4")
pdf.set_auto_page_break(auto=False)

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(254, 0, 0)
    pdf.cell(w=0, h=15, txt=row['Topic'], align="l", ln=1)
    pdf.line(10, 21, 200, 21)
    # Set the Footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=8, txt=row['Topic'], align="R")

    for i in range(row['Pages']-1):
        pdf.add_page()
        # Set the Footer
        pdf.ln(280)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(w=0, h=8, txt=row['Topic'], align="R")

pdf.output("output_pdf.pdf")
#
# # adds new page to pdf
# pdf.add_page()
# # to set the font you can have multiple fonts for each cell, you need to defined it each time if u need different font
# pdf.set_font(family="Times", style="B", size=12)
# # to write anything in the pdf
# pdf.cell(w=0, h=12, txt="Text in pdf", align="l", ln=1)
# pdf.cell(w=0, h=10, txt="text in pdf", align="l", border=1)
# # generates pdf file with name in mentioned
# pdf.output("output_pdf.pdf")
