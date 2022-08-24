from unittest import TextTestResult
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

image = cv2.imread(
    "C:/Users/Ata Sabri/OneDrive/Desktop/Folder/handWitten.png")

text = pytesseract.image_to_string(image)

print(text)
