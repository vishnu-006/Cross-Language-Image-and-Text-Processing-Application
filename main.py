print("OM")
#                                                       IMAGE TO TEXT CONVERSION
from PIL import Image
import pytesseract

from pdfminer.high_level import extract_text

from File import ChooseFile
from Model import Tokenize


# FOR IMAGE FILE
def ImageGiven(path):
    # Open the image using Pillow (PIL)
    image = Image.open(path)

    # Use pytesseract to perform OCR
    text = pytesseract.image_to_string(image)

    # Print the extracted text
    print(text)
    return text


# Extract text from the PDF file
def PdfGiven(path):
    extracted_text = extract_text(path)
    print(extracted_text)
    return text


# FOR PLAIN TEXT

# def TextGiven(text):
#     # some code to be written
#     print(text)
#     return text


option = int(input(""" Choose the input type : 
1 . Image
2 . Pdf
3 . Plain Text  """))

if option == 1:
    path = ChooseFile()
    temp = ImageGiven(path)
    Tokenize(temp)
elif option == 2:
    path = ChooseFile()
    temp = PdfGiven(path)
    Tokenize(temp)
else:
    text = input("ENTER THE TEXT")
    Tokenize(text)
