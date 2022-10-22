from rembg import remove
from PIL import Image


# input_path = "C:\\Users\\Djasnive\\Pictures\\Saved Pictures\\PC Lenovo legion.jpg"
# output_path = "output.png"

def remover(input_path, output_path):
    input_element = Image.open(input_path)
    output = remove(input_element)

    output.save(output_path)
