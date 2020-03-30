import pytesseract as pt

from PIL import Image

print("1")
image = Image.open("./1.jpg")
print("2")

text = pt.image_to_string(image)
print(text)
