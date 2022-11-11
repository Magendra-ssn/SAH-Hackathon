import nltk.data
try:
    from PIL import Image


except ImportError:
    import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'
def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

a=ocr_core('C:\\Users\\hp\\Pictures\\sample handwritten image.jpg')

f1=open('important.txt','w+')

#nltk.download('punkt')

a_list = nltk.tokenize.sent_tokenize(a)

for i in a_list:
    y=0
    x=i.split()
    for j in x:
        if ord(j[0])>65 and ord(j[0])<90:
            y+=1
    if(y>1):
        f1.write(i)

f1.close()
f2=open('important.txt','r')
print(f2.read())
