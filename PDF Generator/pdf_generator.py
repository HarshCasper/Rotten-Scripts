import img2pdf
import os
from PIL import Image

def removealpha(inpath):
    print('Converting Image into non alpha channel image')
    for file in os.listdir(inpath):
        img = Image.open(inpath+file)
        size = img.size
        imgnew = Image.new('RGB',size,255)
        imgnew.paste(img,(0,0))
        imgnew.save('out/'+file)
    print('Image Conversion done.')

def pdfGen(inpath,outpath):
    l = os.listdir(inpath)
    lst = []
    print('PDF Creating...')
    for i in l:
        lst.append(open((inpath+i),'rb'))
    with open('out.pdf','wb') as f:
        f.write(img2pdf.convert(lst))
        
    print('PDF Generation done.')

def main():
    inpath = 'ada/'
    outpath = 'result/'
    removealpha(inpath)
    pdfGen('out/',outpath)

    
if __name__ == "__main__":
    main()
