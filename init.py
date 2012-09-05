#Capturing video from default camera
#Flip video horizontally to get mirror image
#Module: 1
#date: 3 sep,2012
#Lib: OpenCV 2.4
#Python: 2.7
#OS: Windows XP
#@author: Akash Shende
#         akash321@gmail.com
#@copyright: (c) 2012-2013

from cv2.cv import *

def main():
    capture=CreateCameraCapture(0)
    window=NamedWindow("test")


    while 1:
        frm=QueryFrame(capture)
        Flip(frm,frm,1)
        AddS(frm,Scalar(10,00,100),frm)
    
        ShowImage("test",frm)
        key=WaitKey(1)
    
        if(key==27):
            ReleaseCapture(capture)
            DestroyWindow("test")
                
#calling main function
main()

    
    
