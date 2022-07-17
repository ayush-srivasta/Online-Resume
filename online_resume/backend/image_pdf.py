import fitz

#opeing the file
number_of_pages=0
pdf_file=""
location ="/media/images/"
image=""
def convert():
     file_path ="media\\pdf\\myfile.pdf"
     pdf_file = fitz.open(file_path)

     #Reading the location where to save the file
     
     #finding number of pages in the pdf
     number_of_pages = len(pdf_file)
     print(number_of_pages)
          
for current_page_index in range(number_of_pages):
  #iterating through each image in every page of PDF
  for img_index,img in enumerate(pdf_file.getPageImageList(current_page_index)):
        xref = img[0]
        image = fitz.Pixmap(pdf_file, xref)
        #if it is a is GRAY or RGB image
        image.writePNG("{}/image{}-{}.png".format(location,current_page_index, img_index))
        
print("****************")
print(image)               
print("************")