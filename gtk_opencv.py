#! /usr/bin/env python
"""
@author: Akash Shende
embedding OpenCV video in Gtk+ 

steps:
__main__
1)create Gtk window
2)create drawing area
3)connect expose event to callback function
4)set timeout

__callback__
1)create camera capture
2)retrieve frame from camera
3)show image on drawing area"""


import opencv as cv2
import cv as cv
import gtk as gtk
import gtk.gdk as gdk
import gobject #for gobject functions


class Mirror(gtk.Window):
    __name__="mirror"
    widget=None
    time=None
    def __init__(self):
        gtk.Window.__init__(self)
        self.connect("delete-event",gtk.main_quit)
        self.hbox=gtk.VBox(True,5)
        
#        self.button=gtk.Button("Click")
#       self.button.connect("clicked",self.print_text)
        
        #create drawing area
        self.canvas=gtk.DrawingArea()
        self.canvas.set_size_request(640,480)
        
        self.hbox.pack_start(self.canvas)
#        self.hbox.pack_start(self.button)
        
        self.add(self.hbox)
        
        self.hbox.show()
        self.canvas.show()
#       self.button.show()
        
        #connect to expose event
        self.canvas.connect("expose_event",self.draw_on_canvas)
       
       
    def print_text(self,button):
        print "you clicked it..!!"
        
    def draw_on_canvas(self,widget,time):
        #create pixbuf to store data from iplimage
        
        #image processing part
        frame=cv.QueryFrame(cap)
        print frame
        cv.CvtColor(frame,frame,cv.CV_BGR2RGB)
        cv.Flip(frame,frame,1)
        
        print "copying to pixbuff..."
        pixbuf=gdk.pixbuf_new_from_data(frame.tostring(),gdk.COLORSPACE_RGB,False,frame.depth,frame.width,frame.height,1500)
        print pixbuf
        
        display=self.canvas.window
        img=gdk.Image(gdk.IMAGE_FASTEST,display.get_visual(),640,480)
        
        print display
        #display.draw_image(display.new_gc(),img,0,0,0,0,-1,-1)
        display.draw_rgb_image(display.new_gc(),0,0,640,480,gdk.RGB_DITHER_NONE,frame.tostring(),1920)
        
        print "drawing...."
        return True
        

        
if(__name__=="__main__"):
    
    global cap
    global frame
    
    cap=cv.CreateCameraCapture(0)
    win=Mirror()
    print win.__name__
    
    gobject.timeout_add(100,win.draw_on_canvas,None,None)
    win.show()
    gtk.main()
    
