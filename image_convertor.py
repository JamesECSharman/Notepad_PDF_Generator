from PIL import Image, ImageColor


# Function to create a black and white, semi-transparent image for the background
def convert_image(image):
    # Opens the image
    img = Image.open(image)
    # Creates a copy of the image
    im2 = img.copy()
    # Modifies image, setting their alpha value, allowing to set transparency level
    im2.putalpha(90)
    # Pastes all pixels onto original image using the alpha as the mask
    img.paste(im2, img)
    # Converts the image to Greyscale with an alpha, maintaining transparency
    img = img.convert("LA")
    # Saves the image as a png with a set naming convention
    img.save("./New.png", "PNG")


# Function to convert the image to a semi-transparent PNG for top right hand corner logo
def convert_image_2(image):
    # Opens the image
    img = Image.open(image)
    # Creates a copy of the image
    im2 = img.copy()
    # Modifies image, setting their alpha value, allowing to set transparency level
    im2.putalpha(200)
    # Pastes all pixels onto original image using the alpha as the mask
    img.paste(im2, img)
    # Saves the image as a png with a set naming convention
    img.save("./preview.png", "PNG")


# Convert from hex to RGB using PIL Image.Color. returns the text colour as a tuple to be converted
def hex_to_rgb(hex):
    text_colour = ImageColor.getrgb(hex)
    return text_colour