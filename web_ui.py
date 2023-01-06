import streamlit as st
import pandas
from image_convertor import convert_image, convert_image_2
from pdf_generator import generate_pdf


# convert CSV into a DF to be able to generate the PDF
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')


# Part of the generate PDF file function
df = pandas.read_csv("topics.csv")
csv = convert_df(df)

# Page header
st.subheader("Note Pad Generator V1.0")

# Intro text below the header
st.write("Hello and welcome to the Note Pad Generator, "
         "simply upload your image and CSV file to have a branded notepad PDF auto generated for you!")

# Download function to download the CSV template
csv_template_download = st.download_button(label="Download CSV Template", data=csv, file_name="csv_template.csv",
                                           mime="text/csv")

# Instructional text to display the user
st.write("When uploading your CSV file, please make sure you do not alter any of the headers.")
st.write("Topics: This will display the title text on the first page.")
st.write("Pages: This will denote the number of pages for each topic.")


# Upload function for CSV file
upload_csv = st.file_uploader("Upload CSV File")
# Upload function for Image
upload_image = st.file_uploader("Upload Image for Branding", type="png")
# If image is uploaded, read the image name for the image conversion functions
if upload_image:
    image_name = st.write("Filename: ", upload_image.name)
    print(image_name)

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
    # Triggers conver_image function to set logo in top right hand corner
    convert_image_2(img)
    # Triggers generate_pdf function from csv and image_name from if upload_image script
    note_pad = generate_pdf(csv, image_name)
    # Generates a download button which ensures the correct pdf output
    with open("output.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
        download = st.download_button(label="Download PDF Notepad",
                    data=PDFbyte,
                    file_name="test.pdf",
                    mime='application/octet-stream')