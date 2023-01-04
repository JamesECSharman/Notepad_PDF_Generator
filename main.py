from fpdf import FPDF
import pandas as pd

# Create PDF Object
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

# Create Data Object
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 200)
    pdf.cell(w=0, h=12, txt=(row["Topic"]), align="L", ln=1)
    pdf.line(10, 25, 200, 25)

    # Set the footer for master
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 200)
    pdf.cell(w=0, h=10, txt=(row["Topic"]), align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(275)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 200)
        pdf.cell(w=0, h=10, txt=(row["Topic"]), align="R")

pdf.output("output.pdf")
