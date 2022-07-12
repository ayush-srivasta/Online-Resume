import io
import fitz
from PIL import Image

def convert_pfd_image(file):
    pdf_file = fitz.open("media\\pdf\\myfile.pdf")
    print("******************************")
    # print(file)
    print("******************************")
    # page=pdf_file[0]
    image_list = pdf_file.getPageImageList(0)

    print(image_list)
   