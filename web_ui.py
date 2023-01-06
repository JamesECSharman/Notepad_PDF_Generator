import streamlit as st
import pandas
from image_convertor import convert_image, convert_image_2, hex_to_rgb
from pdf_generator import generate_pdf

st.set_page_config(
    layout='wide',
    page_title="PDF NotePad Generator",
    page_icon=":spiral_note_pad"
)

# convert CSV into a DF to be able to generate CSV file for download
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')


# Part of the generate CSV file for download function
df = pandas.read_csv("topics.csv")
csv = convert_df(df)

# Page header
st.title("Note Pad Generator V1.11", )

# Intro text below the header
st.write("Hello and welcome to the Note Pad Generator, "
         "simply upload your image and CSV file to have a branded notepad PDF auto generated for you!")

# Download function to download the CSV template
csv_template_download = st.download_button(label="Download CSV Template", data=csv, file_name="csv_template.csv",
                                           mime="text/csv")

# Creates Expander for instructional text
expander = st.expander("**Expand for Instructions**", expanded=False)

# Instructional text to display the user
with expander:
    st.write("""Simply upload your CSV file with Topics and a PNG image to be added to the page.
    When uploading your CSV file, please make sure you do not alter any of the headers in the file and only edit the
    lines below the Topics and Pages header. All images uploaded must be PNG and it is recommended to upload images
    with transparent backgrounds for the cleanest image.
    An overview of what the csv headers mean and how they work can be seen below""")
    st.write("**CSV Inputs:**")
    st.write("""*Topics*: This will display the title text on the first page.  
             *Pages*: This will denote the number of pages for each topic.""")
    st.write("**Text Orientation Selector:**")
    st.write("""It is worth noting that the Page Titles option will allowu to change the text location from a 
    Left orientation or a central orientation. Logos will be placed to the t yoop right hand corner and as a watermark in 
    the middle of the page.""")
    st.write("**Colour Picker:**")
    st.write("""The Colour Picker will allow you to select any colour you wish for the text at the top of the page. Please
    note that you should choose a dark colour, as the text will be on a white background and lighter colours could become
    washed out.""")

col1, empty_col_1, col2 = st.columns([1.5, 0.1, 1.5])

with col1:
    # Upload function for CSV file
    upload_csv = st.file_uploader("**Upload CSV File**", type="csv")
    # Upload function for Image
    upload_image = st.file_uploader("**Upload Image for Branding**", type="png")
with col2:
    # Select box to allow users to select Topics alignment - left or centered
    title_position = st.selectbox('**Where do you want your Page Titles?**', ('Left', 'Center'))
    # If title position is set to left or center, then the title_alignment value is updated for PDF generation
    if title_position == "Left":
        title_alignment = "L"
    if title_position == "Center":
        title_alignment = "C"
    # Image Colour picker for user to define title colour
    # st.empty()
    colour_picker = st.color_picker("**What Colour Text Would You Like?**", value=None)
    # Convert image HEX to RGB by defined function
    text_colour = hex_to_rgb(colour_picker)
    # Converts tuple into 3 definable int to input into the PDF generator
    (red, green, blue) = text_colour
    # Generate PDF Button
    button = st.button("Generate PDF")
    # If button is pressed action list
    if button:
        # Set's CSV to uploaded csv
        csv = upload_csv
        # Sets img to Uploaded image
        img = upload_image
        # Triggers convert_image function to create background image
        convert_image(img)
        # Triggers cover_image function to set logo in top right hand corner
        convert_image_2(img)
        # Triggers generate_pdf function from csv
        note_pad = generate_pdf(csv, align=title_alignment, r=red, g=green, b=blue)
        # Generates a download button which ensures the correct pdf output
        with open("output.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
            download = st.download_button(label="Download PDF Notepad",
                                          data=PDFbyte,
                                          file_name="test.pdf",
                                          mime='application/octet-stream')


