from fpdf import FPDF
import pandas as pd


# Function to create the PDF
def generate_pdf(csv, align, r, g, b):
    # Create PDF Object
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False, margin=0)

    # Create Data Object
    df = pd.read_csv(csv)

    for index, row in df.iterrows():
        pdf.add_page()

        # Set the header
        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(r, g, b)
        pdf.cell(w=0, h=12, txt=row["Topic"], align=align,
             ln=1)
        pdf.image('preview.png', x=188, y=4, w=12, h=12, type='', link='')
        pdf.image('New.png', x=75, y=110, w=70, h=70, type='', link='')
        # Add the lines to the PDF
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

        # Set the footer
        pdf.ln(265)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        # Set the pages
        for i in range(row["Pages"] - 1):
            pdf.add_page()

            pdf.ln(277)
            pdf.set_font(family="Times", style="I", size=8)
            pdf.set_text_color(180, 180, 180)
            pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
            pdf.image('preview.png', x=188, y=4, w=12, h=12, type='', link='')
            pdf.image('New.png', x=75, y=110, w=70, h=70, type='', link='')

            # Add the lines to the PDF
            for y in range(20, 298, 10):
                pdf.line(10, y, 200, y)

    # Output to generate PDF for download
    pdf.output("output.pdf")