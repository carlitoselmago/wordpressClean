import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
import PIL
from PIL import Image

#searchFolder="/home/haxoorx/Documents/testResize"
searchFolder="/home/haxoorx/Documents/uploads"

maxfileSize=300 #in KB
maxWidth=1024

#functions
def resizeImage(fileURI):
    
    f= open(fileURI, 'r+')
    try:
        image= Image.open(f)
        if image:
            width, height = image.size
            if width>maxWidth:
                #image = resizeimage.resize_width(image, maxWidth,Image.BICUBIC)
                wpercent = (maxWidth/float(width))
                hsize = int((float(height)*float(wpercent)))
                img = image.resize((maxWidth,hsize), PIL.Image.ANTIALIAS)
                img.save(fileURI,quality=80, optimize=True, progressive=True)
            else:
                image.save(fileURI,quality=80, optimize=True, progressive=True)

            if ".png" in fileURI:
                os.system('optipng '+fileURI)
        else:
            print "couldn't open image"
    
    except:
        print "not an image file"
    
    f.close()
    
def searchInWebsite(filename):
    
    match=False
    filename, file_extension = os.path.splitext(filename)
    for img in webImages:
        if filename in img:
            match=True
    return match
        
#end functions

#loadCSV
csvImgFile=open("wordpressSpider/images.csv",'r')
webImages=csvImgFile.read().splitlines()
   



for path, subdirs, files in os.walk(searchFolder):
   for filename in files:
     
    f = os.path.join(path, filename)
    
    if searchInWebsite(filename):

        #print filename

        #check file size
        statinfo = os.stat(f)

        filesize= (int(statinfo.st_size)/1024)

        if filesize>maxfileSize:
            
            resizeImage(f)
            print "exceded file size", f," : "+str(filesize)+" Kb"
        else:
            print f," OK!"
        
        
    
    else:
        print "Image not in website, gonna DELETE",f
        os.remove(f)
    
    #a.write(str(f) + os.linesep) 