import io
import fitz
from PIL import Image

def convert_pfd_image(file):
    pdf_file = fitz.open("media\\pdf\\myfile.pdf")
    page=pdf_file[0]
    image_list = page.getImageList()

    print(image_list)
   