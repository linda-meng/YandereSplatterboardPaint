from pygame import *
from random import *
from math import *
from tkinter import *
from time import sleep
font.init()
#----METADATA----#
__author__ = "Yttrium Z (You Zhou)"
__date__ = "Not finished"
__purpose__ = "Grade 11 Project - Paint Program"
__name__ = "Yandere Splatterboard"
__copyright__ = "Yttrium Z 2015-2016"
#----SETUP----#
root = Tk()
root.withdraw() #makes sure file dialog box disappears after it closes
screen = display.set_mode((1200,750))
display.set_caption("YANDERE SPLATTERBOARD - PAINT PROGRAM BY YOU ZHOU ~~~~~~GREAT ART TAKES DEADICATION~~~~~~")
try:
    display.set_icon(transform.scale(image.load("images/icon.jpg"),(32,32))) #sets icon
except:
    pass
#----LOADING SCREEN----#
screen.blit(image.load("images/LoadScreen.png"),(0,0))
display.flip()
#----PERMANENT CONSTANT DATA----#
#data that can never change no matter what user does
#MUSIC (Really lags up the program startup)
mixer.init()
'''music = [mixer.Sound("music/MiraiNikkiOP.ogg"),
         mixer.Sound("music/InnocentBlue.ogg"),
         mixer.Sound("music/NeverSayNever.ogg"),
         mixer.Sound("music/BoukenDesho.ogg"),
         mixer.Sound("music/Lillium.ogg"),
         mixer.Sound("music/My_Dearest.ogg")] #all music (the playlist)
#shuffle(music) #shuffles the music
#music[0].play()'''
song = 0 #which song are we playing
screen.blit(image.load("images/LoadScreen2.png"),(0,0)) #second loading screen - means music is loaded and loading is almost done
display.flip()
sleep(1)
#COLOR
WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHT_GREY = (180,180,180)
DARK_GREY = (50,50,50)
GREY = (100,100,100)
PINK = (255,150,150)
RED = (255,0,0)
BLOODRED = (220,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)
#FONTS
comicsans = font.SysFont("comicsansms", 15)
arial = font.SysFont("arial",15)
timesnr = font.SysFont("timesnewroman",15)
lucidaconsole = font.SysFont("lucidaconsole",15)
impact = font.SysFont("impact",15)
vladimirscript = font.SysFont("vladimirscript",15)
titlefont = font.SysFont("comicsansms",25)
#SPRITES AND IMAGES
pencilsprite = transform.scale(image.load("images/pencil.png"),(40,40))
eraser = transform.scale(image.load("images/eraser.gif"),(40,40))
paintbrush = transform.scale(image.load("images/paintbrush.png"),(40,40))
linesprite = transform.scale(image.load("images/linesprite.png"),(40,40))
dropper = transform.scale(image.load("images/dropper.png"),(40,40))
fancyA = transform.scale(image.load("images/A.png"),(40,40))
roundedrect = transform.scale(image.load("images/roundrect.png"),(40,40))
ellipsesprite = transform.scale(image.load("images/ellipse.png"),(40,40))
dottedbox = transform.scale(image.load("images/dottedbox.gif"),(40,40))
fillbucket = image.load("images/fillbucket.png")
spraycan = transform.scale(image.load("images/spraypaint.png"),(40,40))
ibeam = transform.scale(image.load("images/ibeam.png"),(40,40))
crosscursor = transform.scale(image.load("images/crosscursor.gif"),(40,40))
saveicon = transform.scale(image.load("images/saveicon.png"),(60,60))
openicon = transform.scale(image.load("images/openicon.png"),(60,60))
yunoface = transform.smoothscale(image.load("images/yunoface.png"),(60,60))
yunogasai = image.load("images/yunogasai.png")
yandereyuno = transform.smoothscale(image.load("images/yandereyuno.png"),(220,300))
kotonohaface = transform.smoothscale(image.load("images/kotonoha.png"),(60,60))
kotonohakatsura = transform.smoothscale(image.load("images/kotonohakatsura.png"),(360,400))
yanderekotonoha = transform.smoothscale(image.load("images/yanderekotonoha.png"),(310,400))
lucyface = transform.smoothscale(image.load("images/lucyface.png"),(60,60))
lucy = transform.smoothscale(image.load("images/lucy.png"),(280,400))
yanderelucy = transform.smoothscale(image.load("images/yanderelucy.png"),(525,600))
inoriface = transform.smoothscale(image.load("images/inoriface.png"),(60,60))
inoriyuzuriha = transform.smoothscale(image.load("images/inoriyuzuriha.png"),(280,400))
yandereinori = transform.scale(image.load("images/yandereinori.png"),(280,400))
tokoface = transform.smoothscale(image.load("images/tokoface.png"),(60,60))
tokofukawa = transform.smoothscale(image.load("images/tokofukawa.png"),(400,400))
genocidersyo = image.load("images/genocidersyo.png")
ryokoface = transform.smoothscale(image.load("images/ryokoface.png"),(60,60))
ryokoasakura = image.load("images/ryokoasakura.png")
#Finalizes Screen
screen.fill((255,150,150))
running = True
#--------------------UI CLASSES (like textboxes, drop down boxes)--------------------#
#-----------------------------TEXTBOX
class Textbox():
    #textbox
    def __init__(self,x,y,width,height,fontfamily="comicsansms",fontsize=15,col=BLACK):
        self.x = x
        self.y = y #sets co-ordinates of textbox
        self.height = height
        self.width = width #sets dimensions of textbox
        self.fontfamily = fontfamily
        self.fontsize = fontsize #font family and fontsize
        self.tbfont = font.SysFont(fontfamily,fontsize) #sets font of textbox
        self.col = col #color of text
        self.text = [""] #text of textbox
        self.width = self.tbfont.render(self.text[-1],True,BLACK).get_width()
        self.height = self.tbfont.render(self.text[-1],True,BLACK).get_height()
        self.lines = 1 #number of lines textbox has
    def changefont(self,fontfamily,fontsize):
        self.fontfamily = fontfamily
        self.fontsize = fontsize
        self.tbfont = font.SysFont(fontfamily,self.fontsize)
    def writeto(self,char):
        #writes a character in the box
        self.text[-1] += char
        self.width = max([self.tbfont.render(self.text[i],True,BLACK).get_width() for i in range(self.lines)])
        self.height = self.tbfont.render(self.text[-1],True,BLACK).get_height()*self.lines
    def delete(self):
        #deletes last character in textbox
        if self.text[-1] == "" and self.lines > 1:
            #if there's nothing in the current line, removes line altogether
            del self.text[-1]
            self.lines -= 1
        else:
            self.text[-1] = self.text[-1][:-1]
        self.width = max([self.tbfont.render(self.text[i],True,BLACK).get_width() for i in range(self.lines)]) #sets width to be maximum of the lines
        self.height = self.tbfont.render(self.text[-1],True,BLACK).get_height()*self.lines #sets height
    def newline(self):
        self.lines += 1
        self.text.append("")
        self.height = self.tbfont.render(self.text[-1],True,BLACK).get_height()*self.lines
    def drawtext(self,screen,perm=True):
        #draws text to screen
        if not perm:
            draw.rect(screen,self.col,(self.x-2,self.y-2,self.width+4,self.height+4),2)
        else:
            screen.set_clip(canvas)
        #^draws a box to fit the text of the text box drawn by the text tool
        for i in range(self.lines):
            screen.blit(self.tbfont.render(self.text[i],True,self.col),(self.x,self.y+(self.height//self.lines)*i))#blits font to screen
        screen.set_clip(None)
#-----------------------------DROPDOWNBOX
class DropDownBox():
    #drop down box
    def __init__(self,x,y,items,name):
        self.items = items #list of all the items, all items are buttons
        self.width = max([i.width for i in items]) #width of dropdown box becomes maximum width of item in list
        self.height = max([i.height for i in items]) #same idea for height as width, but for height
        self.name = name #display of drop down
        self.x = x
        self.y = y #co-ords
        self.itemrects = [Rect(i.x,i.y,i.width,i.height) for i in self.items]#item rects
        self.menudown = False #is the menu down?
        self.mainrect = Rect(self.x,self.y,self.width,self.height)#main rect of the drop down box (not it's items)
        totwidth = sum([i.width for i in self.items])#sum of all the item's widths
        totheight = sum([i.height for i in self.items])#sum of all the item's heights
        self.menurect = Rect(self.x,self.y+self.height,totwidth,totheight) #rect of the menu portion of the dropdown box
        self.highlighted = False #is the box highlighted by mouse?
    def dropdown(self,screen):
        #drops down the menu
        for i in self.items:
            i.display(screen)
        self.menudown = True
    def drawbox(self,screen):
        if self.highlighted:
            col = LIGHT_GREY
        else:
            col = WHITE
        draw.rect(screen,col,(self.x,self.y,self.width+10,self.height)) #draws box
        screen.blit(comicsans.render(self.name,True,BLACK),(self.x+2,self.y+2))
    def istouch(self):
        #states whether mouse is touching the mainrect of drop down menu
        mx,my = mouse.get_pos()
        return self.mainrect.collidepoint(mx,my)
    def clickon(self,screen):
        #method when box is clicked
        mx,my = mouse.get_pos()
        if not self.menudown:
                #if the menu is not down 
                self.menudown = True
        elif self.menurect.collidepoint(mx,my):
            for i in self.items:
                if i.istouch():
                    i.clickon(screen)
                    i.selected = True
                else:
                    i.selected = False
        else:
            self.menudown = False
#--------------------TOOL CLASSES--------------------#
#--basis for tools
class Tool():
    def __init__(self):
        #initialization of tool
        pass
    def rclick(self,screen):
        #right click of tool
        pass
    def lclick(self,screen):
        #left click of tool
        pass
    def mouseup(self,screen):
        #if mouse is raised
        pass
    def scroll(self,screen,forward=True):
        #scrolling function of tool
        pass
    def cont(self,screen):
        #as mouse is being held
        pass
    def outside(self):
        #while the mouse is outside the canvas, some things can still be done
        pass
    def keypress(self,screen,keypressed=""):
        #interaction of tool with keyboard
        pass
    def drawsprite(self,screen):
        #draws the sprite on the mouse
        mx,my = mouse.get_pos()
        screen.blit(self.icon,(mx,my))
#-------------------------------------------Pencil
class Pencil(Tool):
    #1 pixel line that follows mouse
    def __init__(self):
        global lcol
        global pencilsprite
        #sets up color and default starting coords for line
        mx,my = mouse.get_pos()
        self.icon = pencilsprite #sets mouse sprite
        self.col = lcol
        self.sx = mx #sx is x co-ord for starting dot
        self.sy = my #sy is y co-ord for starting dot, the algorithm works by drawing a line from (sx,sy) to (mx,my) and changing sx and sy to mx and my
    def lclick(self,screen):
        #sets sx and sy to wherever user clicked
        self.sx = mx
        self.sy = my
    def rclick(self,screen):
        #same as left click
        self.lclick(screen)
    def cont(self,screen):
        #draws a line from (sx,sy) to (mx,my)
        mb = mouse.get_pressed()
        #following two if statements set the colour of the mouse based on whether right mouse button or left mouse button is held
        if mb[0]:
            global lcol
            self.col = lcol
        elif mb[2]:
            global rcol
            self.col = rcol
        draw.line(screen,self.col,(self.sx,self.sy),(mx,my))
        self.sx = mx
        self.sy = my #changes the sx and sy to mx and my to keep make it follow the mouse
    def outside(self):
        #continues drawing if the last click was canvas - it won't draw outside of canvas because of clipping before calling this method
        global lastclick
        if lastclick == "canvas":
            self.cont(screen)
    def drawsprite(self,screen):
        mx,my = mouse.get_pos()
        screen.blit(self.icon,(mx,my-40))
#-------------------------------------------Eraser
class Eraser(Tool):
    #draws line of white circles to erase stuff
    def __init__(self):
        global eraser
        #sets up default starting coords for eraser line
        mx,my = mouse.get_pos()
        self.icon = eraser #sets mouse sprite
        self.sx = mx #starting co-ords of lines drawn that follows mouse
        self.sy = my
        self.size = 10 #size of eraser
    def lclick(self,screen):
        #changes sx and sy to be where mouse is
        mx,my = mouse.get_pos()
        self.sx = mx
        self.sy = my
    def rclick(self,screen):
        #same as left click
        self.lclick(screen)
    def scroll(self,screen,forward=True):
        if not forward:
            #makes eraser bigger
            if self.size < 512:
                #limits size of eraser at 512 (more would be obnoxious)
                self.size += 1
        else:
            #makes eraser smaller
            if self.size > 1:
                #makes sure eraser size doesn't go below 1
                self.size -= 1
    def cont(self,screen):
        #erases in a line that follows user's mouse - same idea as pencil but uses a line of circles instead of an actual line
        mx,my = mouse.get_pos()
        dist = ((mx-self.sx)**2+(my-self.sy)**2)**0.5 #distance
        dist = max(1,dist) #makes sure dist != 0 so divison by 0 doesn't happen
        lx = (mx-self.sx)/dist #increment of x and y values of the line
        ly = (my-self.sy)/dist
        for i in range(int(dist)):
            draw.circle(screen,WHITE,(int(self.sx+lx*i),int(self.sy+ly*i)),self.size)
        self.sx = mx
        self.sy = my
    def outside(self):
        #continues drawing if the last click was canvas - it won't draw outside of canvas because of clipping before calling this method
        global lastclick
        if lastclick == "canvas":
            self.cont(screen)
    def drawsprite(self,screen):
        mx,my = mouse.get_pos()
        draw.circle(screen,WHITE,(mx,my),self.size) #draws circle to show user how big eraser is
        super(Eraser,self).drawsprite(screen) #Calls on Tool class's default toolbit, as that fits the bill for the Eraser tool
    def keypress(self,screen,keypressed=""):
        if keypressed == " ":
            self.size = 10 #resets the size to 10 upon space press
#-------------------------------------------Paint Brush
class Brush(Tool):
    #draws colored circles
    #this class is pretty much a combination of the eraser class and the pencil class
    def __init__(self):
        global paintbrush
        global lcol
        #sets up default starting coords for brush
        mx,my = mouse.get_pos()
        self.icon = paintbrush #sets mousesprite of tool
        self.sx = mx #starting coords for lines drawn with this tool
        self.sy = my
        self.size = 10 #size of brush
        self.col = lcol #color of brush
    def lclick(self,screen):
        #changes sx and sy to be where mouse is
        mx,my = mouse.get_pos()
        self.sx = mx
        self.sy = my
    def rclick(self,screen):
        #same as left click
        self.lclick(screen)
    def scroll(self,screen,forward=True):
        if not forward:
            #makes brush bigger
            if self.size < 512:
                #limits size of brush at 512 (more would be obnoxious)
                self.size += 1
        else:
            #makes brush smaller
            if self.size > 1:
                #makes sure brush size doesn't go below 1
                self.size -= 1
    def cont(self,screen):
        #draws in a line that follows user's mouse - same idea as pencil but uses a line of circles instead of an actual line
        mb = mouse.get_pressed()
        #the two following if statements changes color drawn to mouse color
        if mb[0]:
            global lcol
            self.col = lcol
        elif mb[2]:
            global rcol
            self.col = rcol
        mx,my = mouse.get_pos()
        dist = ((mx-self.sx)**2+(my-self.sy)**2)**0.5 #distance
        dist = max(1,dist) #makes sure distance isn't 0 so division by 0 doesn't occur
        lx = (mx-self.sx)/dist #increment of x and y values of the line
        ly = (my-self.sy)/dist
        for i in range(int(dist)):
            draw.circle(screen,self.col,(int(self.sx+lx*i),int(self.sy+ly*i)),self.size)
        self.sx = mx
        self.sy = my
    def outside(self):
        #continues drawing if the last click was canvas - it won't draw outside of canvas because of clipping before calling this method
        global lastclick
        if lastclick == "canvas":
            self.cont(screen)
    def drawsprite(self,screen):
        global lcol
        global rcol
        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()
        if mb[2]:
            self.col = rcol
        else:
            self.col = lcol
        draw.circle(screen,self.col,(mx,my),self.size) #draws circle to show user how big brush is
        screen.blit(self.icon,(mx,my-40))
    def keypress(self,screen,keypressed=""):
        if keypressed == " ":
            self.size = 10
#-------------------------------------------Line Tool
class Line(Tool):
    #draws a line
    def __init__(self):
        global lcol
        global linesprite
        self.icon = linesprite #sets sprite
        self.col = lcol
        self.size = 10
        self.sx = 0 #starting point of line
        self.sy = 0 
    def lclick(self,screen):
        global lcol
        global cfiller
        global canvas
        mx,my = mouse.get_pos()
        self.col = lcol #changes color to left mouse color
        self.sx = mx #changes starting point of line to where user clicked
        self.sy = my
        cfiller = screen.copy().subsurface(canvas) #sets the canvas filler to be what the user was when they clicked
    def rclick(self,screen):
        global rcol
        self.lclick(screen) #changes color to right mouse color, the rest is the same as left click
        self.col = rcol
    def cont(self,screen):
        global cfiller
        #same algorithm as brush tool
        screen.blit(cfiller,(300,50))
        mx,my = mouse.get_pos()
        dist = ((mx-self.sx)**2+(my-self.sy)**2)**0.5 #distance
        dist = max(1,dist) #makes sure distance isn't 0 so division by 0 doesn't occur
        lx = (mx-self.sx)/dist #increment of x and y values of the line
        ly = (my-self.sy)/dist
        for i in range(int(dist)):
            draw.circle(screen,self.col,(int(self.sx+lx*i),int(self.sy+ly*i)),self.size)
    def scroll(self,screen,forward=True):
        if forward:
            #makes line size smaller and limits it at 1
            if self.size > 1:
                self.size -= 1
        else:
            #makes size larger and limits it at 512
            if self.size < 512:
                self.size += 1
    def outside(self):
        #draws a line as long as the last click was in the canvas
        global lastclick
        if lastclick == "canvas":
            self.cont(screen)
    def drawsprite(self,screen):
        global lcol
        global rcol
        mb = mouse.get_pressed()
        mx,my = mouse.get_pos()
        if mb[2]:
            draw.circle(screen,self.col,(mx,my),self.size)
        else:
            draw.circle(screen,lcol,(mx,my),self.size)
        screen.blit(self.icon,(mx,my-40))
    def keypress(self,screen,keypressed=""):
        if keypressed == " ":
            self.size = 10
#-------------------------------------------Selector
class Selector(Tool):
    #selects color at given location in the canvas
    def __init__(self):
        self.icon = dropper #sets sprite
    def lclick(self,screen):
        global lcol
        mx,my = mouse.get_pos()
        lcol = screen.get_at((mx,my))
    def rclick(self,screen):
        global rcol
        mx,my = mouse.get_pos()
        rcol = screen.get_at((mx,my))
    def drawsprite(self,screen):
        mx,my = mouse.get_pos()
        screen.blit(self.icon,(mx-40,my-40))
#-------------------------------------------Text
class Text(Tool):
    #writes text
    def __init__(self,fontfamily,fontsize):
        self.icon = ibeam
        self.fontfamily = fontfamily
        self.fontsize = fontsize #sets font
        self.textbox = Textbox(0,0,0,0,fontfamily,fontsize,(0,0,0))
        self.hastextbox = False #has this tool drawn a textbox already?
    def lclick(self,screen):
        global lcol
        mx,my = mouse.get_pos()
        if self.hastextbox:
            #turns off text box if we have one
            self.hastextbox = False
            currtool.textbox.drawtext(screen)
        else:
            #draws a text box if we don't have one
            self.textbox = Textbox(mx,my,20,20,self.fontfamily,self.fontsize,lcol)
            self.hastextbox = True
    def rclick(self,screen):
        #literally the same thing as lclick, but with rcol instead of lcol
        global rcol
        mx,my = mouse.get_pos()
        if self.hastextbox:
            #turns off text box if we have one
            self.hastextbox = False
            currtool.textbox.drawtext(screen)
        else:
            #draws a text box if we don't have one
            self.textbox = Textbox(mx,my,20,20,self.fontfamily,self.fontsize,rcol)
            self.hastextbox = True
    def scroll(self,screen,forward=True):
        if forward:
            #makes text smaller
            self.fontsize -= 1
            self.fontsize = max(self.fontsize,5) #makes sure fontsize isn't less than 5
        else:
            #makes text bigger
            self.fontsize += 1
            self.fontsize = min(self.fontsize,99) #makes sure fontsize isn't greater than 99
    def keypress(self,screen,keypressed):
        #the only tool who uses this method
        #it allows the tool to interact with the user's keyboard
        if self.hastextbox:
            kp = key.get_pressed()
            if kp[K_RETURN] and (kp[K_LCTRL] or kp[K_RCTRL]):
                #finishes up the textbox when CTRL-Enter
                self.hastextbox = False
                currtool.textbox.drawtext(screen)
            elif kp[K_RETURN]:
                #adds a new line if the RETURN button is pressed
                self.textbox.newline()
            else:
                if kp[K_BACKSPACE]:
                    self.textbox.delete()
                elif 1 in kp:
                    self.textbox.writeto(keypressed) #writes keypressed to texbox
    def outside(self):
        #turns off text box if user clicks outside canvas
        global screen
        if self.hastextbox:
            self.hastextbox = False
            currtool.textbox.drawtext(screen)
    def drawsprite(self,screen):
        mx,my = mouse.get_pos()
        screen.blit(self.icon,(mx-20,my-10))
#-------------------------------------------Select Tool
class Select(Tool):
    #selects an area and makes it moveable
    def __init__(self):
        self.icon = crosscursor
        self.hasbox = False #has the tool a selected box set?
        self.forming = False #is the box being formed?
        self.selectedbox = None #selected box by shape
        self.x,self.y,self.width,self.height = 0,0,0,0 #dimensions and co-ords of selected box
        self.dx,self.dy = 0,0 #difference in x and y between mouse and corner of selectedbox
        self.op = 0 #option of size change the user tried (this is determined by where user clicks; each option affects different parts of the box, like either x or width, y or height, etc.)
        #0 = No change; 1: change x and y; 2: change width and y; 3: change x and height; 4: change width and height;
        #5 = change y; 6 = change height; 7 = change x; 8 = change width
    def lclick(self,screen):
        global cfiller
        mx,my = mouse.get_pos()
        if self.hasbox:
            #check if they press a size change point on the box
            sizepoints = [(self.x-1,self.y-1),(self.x+self.width+1,self.y-1),
                          (self.x-1,self.y+self.height+1),(self.x+self.width+1,self.y+self.height+1),
                          (self.x+(self.width+1)//2,self.y-1),(self.x+(self.width+1)//2,self.y+self.height+1),
                          (self.x-1,self.y+(self.height+1)//2),(self.x+self.width+1,self.y+(self.height+1)//2)] #points in which the size of the box can be altered
            op = 0 #option user did for size change
            self.op = 0
            for x,y in sizepoints:
                op += 1
                if Rect(x-5,y-5,10,10).collidepoint((mx,my)):
                    self.op = op
                    break
            if self.op != 0:
                #if user tried to change size we move let the cont() method handle the rest
                pass
            elif not Rect(self.x,self.y,self.width,self.height).collidepoint(mx,my):
                #if the box exists and user doesn't click it, the box disappears
                try:
                    self.selectedbox = transform.smoothscale(self.selectedbox,(abs(self.width),abs(self.height)))#resizes image
                except:
                    self.selectedbox = transform.scale(self.selectedbox,(abs(self.width),abs(self.height)))#resizes image
                screen.blit(cfiller,(300,50))
                self.hasbox = False
                screen.blit(self.selectedbox,(self.x,self.y))
            else:
                #if user did not try to change size we move the box
                self.dx = mx-self.x
                self.dy = my-self.y #sets difference between corner and mouse co-ord
        else:
            global canvas
            cfiller = screen.copy().subsurface(canvas) #makes cfiller canvas before the click
            self.x = mx
            self.y = my
            self.forming = True
    def rclick(self,screen):
        self.lclick(screen) #identical to left click
    def mouseup(self,screen):
        #if there is no box, then this defines the box
        if self.forming:
            global cfiller
            global canvas
            mx,my = mouse.get_pos()
            if mx < self.x:
                self.x = mx
            if my < self.y:
                self.y = my #makes top-left corner of box same as mouse if the mouse is above or left of the selected area
            self.x = max(301,self.x) #limits box inside canvas
            self.y = max(51,self.y)
            self.width = min(1101-self.x,self.width)
            self.height = min(651-self.y,self.height)
            screen.blit(cfiller,(300,50)) #blits cfiller to not copy the rectangle drawn by formation
            self.hasbox = True
            self.selectedbox = screen.copy().subsurface(Rect(self.x,self.y,self.width,self.height)) #sets selected box to area
            draw.rect(screen,WHITE,(self.x,self.y,self.width,self.height)) #erases area where selected image is
            cfiller = screen.copy().subsurface(canvas)
            self.forming = False
    def cont(self,screen):
        global cfiller
        mx,my = mouse.get_pos()
        if self.hasbox:
            #if there is a box, the we move it or change size
            if self.op == 0:
                self.x = mx-self.dx
                self.y = my-self.dy
            else:
                options = ["self.x,self.y,self.width,self.height=mx,my,self.width-(mx-self.x),self.height-(my-self.y)",
                           "self.width,self.y,self.height=mx-self.x,my,self.height-(my-self.y)",
                           "self.x,self.width,self.height=mx,self.width-(mx-self.x),my-self.y",
                           "self.width,self.height=mx-self.x,my-self.y",
                           "self.y,self.height=my,self.height-(my-self.y)",
                           "self.height=my-self.y",
                           "self.x,self.width=mx,self.width-(mx-self.x)",
                           "self.width=mx-self.x"]
                exec(options[self.op-1])
                self.width,self.height = max(1,self.width),max(1,self.height) #makes sure width or height isn't 0
                
        elif self.forming:
            #if the box is forming, we draw a temporary black box
            self.width = abs(self.x - mx) #width of rect is absolute distance between mouse-x and start-x
            self.height = abs(self.y - my) #height of rect is same idea as width, but with y-coords
            #the following two if statements set start x and start y to mx and my if they are greater
            screen.blit(cfiller,(300,50)) #makes sure box only appears once
            draw.rect(screen,BLACK,(min(self.x,mx)-1,min(self.y,my)-1,self.width+2,self.height+2),1)
    def outside(self):
        #removes the box if use pressed outside canvas
        global screen
        global cfiller
        global lastclick
        if self.hasbox and lastclick != "canvas":
            #if the last click was not the canvas we turn off the tool
            try:
                self.selectedbox = transform.smoothscale(self.selectedbox,(abs(self.width),abs(self.height)))#resizes image
            except:
                self.selectedbox = transform.scale(self.selectedbox,(abs(self.width),abs(self.height)))#resizes image
            screen.blit(cfiller,(300,50))
            self.hasbox = False
            screen.blit(self.selectedbox,(self.x,self.y))
        elif self.hasbox:
            #if the last click was the canvas, we continue drawing the box
            pass
    def keypress(self,screen,keypressed):
        #handles key methods for a box
        global boxcp
        kp = key.get_pressed()
        if kp[K_DELETE]:
            #deletes box
            self.hasbox = False
        elif kp[K_c] and (kp[K_RCTRL] or kp[K_LCTRL]) and self.hasbox:
            #copies box onto clipboard
            boxcp = (transform.smoothscale(self.selectedbox,(self.width,self.height)),(self.x,self.y)) #sets the clipboard's image and coordinates
        elif kp[K_x] and (kp[K_RCTRL] or kp[K_LCTRL]) and self.hasbox:
            #cuts box onto clipboard
            self.hasbox = False
            boxcp = (transform.smoothscale(self.selectedbox,(self.width,self.height)),(self.x,self.y)) #sets the clipboard's image and coordinates
    def drawsprite(self,screen):
        mx,my = mouse.get_pos()
        draw.line(screen,BLACK,(mx,my-10),(mx,my+10),2) #drawing crosshairs
        draw.line(screen,BLACK,(mx-10,my),(mx+10,my),2)
        screen.blit(self.icon,(mx-20,my-20))
#-------------------------------------------Spray Paint
class Spray(Tool):
    #colours random pixels within a 10 radius circle
    def __init__(self):
        global lcol
        self.icon = spraycan
        self.col = lcol
        self.sx,self.sy = 0,0
    def lclick(self,screen):
        global lcol
        mx,my = mouse.get_pos()
        self.col = lcol
        self.sx = mx
        self.sy = my
    def rclick(self,screen):
        self.lclick(screen) #same as lclick but changes colour to right mouse button instead
        global rcol
        self.col = rcol
    def cont(self,screen):
        mx,my = mouse.get_pos()
        #same algorithm as brush or line function but with random dots instead of full circles
        dist = hypot(mx-self.sx,my-self.sy)
        dist = max(1,dist) #makes sure distance isn't 0
        lx = (mx-self.sx)/dist
        ly = (my-self.sy)/dist
        for i in range(int(dist)):
            for j in range(3):
                randang = randint(0,359) #random angle
                randhy = randint(0,10) #random hypotenuse
                screen.set_at((int(self.sx+lx*i+cos(randang)*randhy),int(self.sy+ly*i+sin(randang)*randhy)),self.col) #random spray
        self.sx,self.sy = mx,my
    def outside(self):
        #continues drawing if the last click was canvas - it won't draw outside of canvas because of clipping before calling this method
        global lastclick
        if lastclick == "canvas":
            self.cont(screen)
    def drawsprite(self,screen):
        mx,my = mouse.get_pos()
        screen.blit(self.icon,(mx-10,my))
#-------------------------------------------Shape Tool
class Shape(Tool):
    #pastes a shape on the screen
    def __init__(self):
        global lcol
        self.icon = roundedrect
        self.shape = "rect" #shape of tool, default is rect
        self.col = lcol #color of shape - default is left mouse color
        self.width = 0 #width of shape - default is 0
        self.sx,self.sy = 0,0 #starting co-ords of shape, starts at 0,0 (doesn't rly matter since we change it on click)
    def lclick(self,screen):
        global cfiller
        global canvas
        global lcol
        mx,my = mouse.get_pos()
        cfiller = screen.copy().subsurface(canvas) #sets cfiller to be canvas before click
        self.sx,self.sy = mx,my #sets starting co-ords to mouse pos
        self.col = lcol #sets color to left click color
    def rclick(self,screen):
        self.lclick(screen) #identical to lclick
        self.col = rcol #sets color to rclick color
    def scroll(self,screen,forward=True):
        if forward:
            #makes shape border smaller
            self.width -= 1
            self.width = max(0,self.width) #makes sure width is at least 0
        else:
            #makes shape border bigger
            self.width += 1
            self.width = min(99,self.width) #makes sure width does not exceed 99
    def cont(self,screen):
        global cfiller
        mx,my = mouse.get_pos()
        screen.blit(cfiller,(300,50))
        if self.shape == "rect":
            sx = min(self.sx,mx) #sx becomes smaller of startx and mouse-x
            sy = min(self.sy,my) #same idea as sx
            draw.rect(screen,self.col,(sx,sy,abs(self.sx-mx),abs(self.sy-my)),self.width)
        elif self.shape == "ellipse":
            sx = min(self.sx,mx) #sx becomes smaller of startx and mouse-x
            sy = min(self.sy,my) #same idea as sx
            draw.ellipse(screen,self.col,(sx,sy,abs(self.sx-mx),abs(self.sy-my)),min(abs(self.sy-my)//2,abs(self.sx-mx)//2,abs(self.width)))
#-------------------------------------------Fill Tool
class Fill(Tool):
    #fills an area with a colour
    def __init__(self):
        self.icon = fillbucket
        self.fcol = BLACK #fill colour - what the colour to change pixels into
        self.ccol = WHITE #change colour - what colours to change
    def lclick(self,screen):
        global lcol
        global canvas
        mx,my = mouse.get_pos()
        self.fcol = lcol #sets fill colour to left mouse colour
        self.ccol = screen.get_at((mx,my)) #sets change colour to where user clicked
        if self.fcol == self.ccol:
            return 0 #does not run if the change colour is the same as the fill colour
        tochange = set()#set of pixels to change
        tochange.add((mx,my))
        while len(tochange) > 0:
            x,y = tochange.pop()
            if canvas.collidepoint(x,y) and screen.get_at((x,y)) == self.ccol:
                #changes the colour of all four directions
                screen.set_at((x,y),self.fcol)
                tochange.add((x+1,y))
                tochange.add((x-1,y))
                tochange.add((x,y+1))
                tochange.add((x,y-1))
                
    def rclick(self,screen):
        #same as left click, but uses right mouse colour instead
        global rcol
        self.fcol = rcol
        self.ccol = screen.get_at((mx,my)) #sets change colour to where user clicked
        if self.fcol == self.ccol:
            return 0 #does not run if the change colour is the same as the fill colour
        tochange = set()#set of pixels to change
        tochange.add((mx,my))
        while len(tochange) > 0:
            x,y = tochange.pop()
            if canvas.collidepoint(x,y) and screen.get_at((x,y)) == self.ccol:
                #changes the colour of all four directions
                screen.set_at((x,y),self.fcol)
                tochange.add((x+1,y))
                tochange.add((x-1,y))
                tochange.add((x,y+1))
                tochange.add((x,y-1))
    def drawsprite(self,screen):
        mx,my = mouse.get_pos()
        screen.blit(self.icon,(mx-40,my-40))
#-------------------------------------------Stamp
class Stamp(Tool):
    #stamps images
    def __init__(self,img,img2=False):
        self.img = img #image the stamp will stamp
        self.owidth = self.width = self.img.get_width() #dimensions of stamp (owidth and oheight are original width and height)
        self.oheight = self.height = self.img.get_height()
        self.percentage = 100 #percentage of image size
        if not img2:
            self.img2 = img #image the stamp stamps when right clicked - default is current stamp
        else:
            self.img2 = img2
        self.owidth2 = self.width2 = self.img2.get_width()
        self.oheight2 = self.height2 = self.img2.get_height()
        self.icon = self.img
        self.currimg = "" #which image is the stamp drawing
    def lclick(self,screen):
        global cfiller
        global canvas
        #sets the img to image 1 and sets cfiller to canvas upon click
        cfiller = screen.copy().subsurface(canvas) #sets cfillers
        self.currimg = ""
        try:
            self.icon = transform.smoothscale(self.img,(self.width,self.height)) #changes icon to image 1
        except:
            self.icon = transform.scale(self.img,(self.width,self.height))
    def rclick(self,screen):
        #sets the img to image 2 and sets cfiller upon click
        self.lclick(screen)
        try:
            self.icon = transform.smoothscale(self.img2,(self.width2,self.height2)) #changes icon to image 2
        except:
            self.icon = transform.scale(self.img2,(self.width2,self.height2))
        self.currimg = "2"
    def cont(self,screen):
        screen.blit(cfiller,(canvas[0],canvas[1]))
        mx,my = mouse.get_pos()
        currwidth = eval("self.width"+self.currimg)
        currheight = eval("self.height"+self.currimg)
        currimg = eval("self.img"+self.currimg) #currimg dimensions and currimg
        try:
            screen.blit(transform.smoothscale(currimg,(currwidth,currheight)),(int(mx-currwidth/2),int(my-currheight/2))) #tries to blit a smoothscaled stamp
        except:
            screen.blit(transform.scale(currimg,(currwidth,currheight)),(int(mx-currwidth/2),int(my-currheight/2))) #blits a scaled stamp
    def mouseup(self,screen):
        #resets icon = image 1
        self.currimg = ""
        try:
            self.icon = transform.smoothscale(self.img,(self.width,self.height)) #changes icon to image 1
        except:
            self.icon = transform.scale(self.img,(self.width,self.height))
    def scroll(self,screen,forward=True):
        if forward:
            #makes image smaller
            if min(self.width,self.height) > 20 and min(self.width2,self.height2) > 20 and self.percentage > 1:
                #limits the image size so that both height and width can be no lower than 20 and makes sure the image isn't 0% size
                self.percentage -= 1 
        else:
            #makes image bigger
            if max(self.width,self.height) < 1024:
                #limits image width and height at 1024px (actualy a little more, but it doesn't really matter)
                self.percentage += 1
        self.width = int(self.owidth*self.percentage/100)
        self.height = int(self.oheight*self.percentage/100)
        self.width2 = int(self.owidth2*self.percentage/100)
        self.height2 = int(self.oheight2*self.percentage/100)
        currwidth = eval("self.width"+self.currimg)
        currheight = eval("self.height"+self.currimg)
        currimg = eval("self.img"+self.currimg) #currimg dimensions and currimg
        try:
            self.icon = transform.smoothscale(currimg,(currwidth,currheight)) #changes icon size
        except:
            self.icon = transform.scale(currimg,(currwidth,currheight))
    def keypress(self,screen,keypressed=""):
        if keypressed == " ":
            #if the user hit space, we return the image to it's original state
            self.percentage = 100
            self.width = self.owidth
            self.height = self.oheight
            self.width2 = self.owidth2
            self.height2 = self.oheight2
            currwidth = eval("self.width"+self.currimg)
            currheight = eval("self.height"+self.currimg)
            currimg = eval("self.img"+self.currimg) #currimg dimensions and currimg
            try:
                self.icon = transform.smoothscale(currimg,(currwidth,currheight)) #sets icon to have same size as new image
            except:
                self.icon = transform.scale(currimg,(currwidth,currheight)) #sets icon to have same size as new image
    def drawsprite(self,screen):
        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()
        screen.blit(self.icon,(mx-self.icon.get_width()//2,my-self.icon.get_height()//2))
        if mb == (0,0,0):
            draw.line(screen,WHITE,(mx,my-10),(mx,my+10),2)
            draw.line(screen,WHITE,(mx-10,my),(mx+10,my),2) #drawing crosshairs if the mouse is not being pressed
#----------------BUTTON CLASS----------------#
#this class is the class for all buttons in the program
class Button():
    #button for selecting tool, or for changing fontsize, or changing color, or selecting font
    def __init__(self,func,pic,x=0,y=0,toolbit="",width=40,height=40,arg2=None):
        self.height = height #dimensions of button
        self.width = width
        self.func = func #function button does
        self.x = x #coords of button
        self.y = y
        self.pic = pic #picture of button
        self.highlighted = False #is button being hovered over or held on?
        self.toolbit = toolbit
        self.selected = False #is this button selected (only applies to drop down boxes' buttons)
        self.arg2 = arg2 #2nd argument for button - optional. Tool buttons don't use this
    def display(self,screen):
        #displays button
        global currtool
        if self.highlighted:
            dispcol = RED
        else:
            dispcol = WHITE
        draw.rect(screen,dispcol,(self.x,self.y,self.width,self.height))
        if type(self.pic) == Surface:
            screen.blit(self.pic,[self.x,self.y])
        elif type(self.pic) == Rect:
                draw.rect(screen,self.arg2,self.pic)
        if self.func == currtool or self.selected:
            #If it's the selected tool, the border of the button is red, otherwise it's black
            draw.rect(screen,RED,(self.x,self.y,self.width,self.height),1)
        else:
            draw.rect(screen,BLACK,(self.x,self.y,self.width,self.height),1)
    def istouch(self):
        #is the mouse touching the button? Well this method says!
        mx,my = mouse.get_pos()
        rectform = Rect(self.x,self.y,self.width,self.height)
        return rectform.collidepoint(mx,my)
    def clickon(self,screen,rclick=False):
        global textool
        global currtool
        global lcol
        global rcol
        global shapetool
        global root
        global cfiller
        if issubclass(type(self.func),Tool):
            #tool change button
            currtool = self.func
        elif self.func == "font":
            #font change button
            currtool = textool
            textool.fontfamily = self.arg2
            textool.textbox.changefont(self.arg2,textool.textbox.fontsize) #changes fontfamily
        elif self.func == "fontsize":
            #fontsize change button
            currtool = textool
            newfontsize = textool.fontsize + self.arg2
            newfontsize = min(99,newfontsize)
            newfontsize = max(5,newfontsize) #limits new font size
            textool.fontsize = newfontsize
            textool.textbox.changefont(textool.textbox.fontfamily,newfontsize) #changes fontsize
        elif self.func == "shape":
            #shape change button
            currtool = shapetool
            shapetool.shape = self.arg2 #changes shapetool to shape
            if self.arg2 == "ellipse":
                tools[8].pic = ellipsesprite
                shapetool.icon = ellipsesprite
            elif self.arg2 == "rect":
                tools[8].pic = roundedrect
                shapetool.icon = roundedrect
        elif self.func == "shapewidth":
            #shape width change
            currtool = shapetool
            shapetool.width += self.arg2
            shapetool.width = min(99,shapetool.width) #limits new shapewidth
            shapetool.width = max(0,shapetool.width)
        elif self.func == "color":
            #color change button
            mb = mouse.get_pressed()
            if mb[0]:
                lcol = self.arg2
            elif mb[2]:
                rcol = self.arg2
        elif self.func == "save":
            #save function
            if type(currtool) == Select:
                currtool.hasbox = False
            elif type(currtool) == Text:
                currtool.hastextbox = False
            mouse.set_visible(True)
            root = Tk()
            root.withdraw() #resets window
            loadname = filedialog.asksaveasfilename()
            if loadname:
                if loadname[-4:] in [".jpg",".png",".bmp",".gif"]:
                    ext = ""
                else:
                    ext = ".jpg"
                image.save(screen.copy().subsurface(canvas), loadname + ext)
            mouse.set_visible(False)
        elif self.func == "open":
            #open function
            if type(currtool) == Select:
                currtool.hasbox = False
            elif type(currtool) == Text:
                currtool.hastextbox = False
            root = Tk()
            root.withdraw() #resets window
            loadname = filedialog.askopenfilename()
            mouse.set_visible(True)
            if loadname:
                if loadname[-4:] in [".jpg",".png",".gif",".bmp"]:
                    if len(mem) >= 256:
                        del mem[0] #removes the last thing memorized if we're over the limit
                    mem2 = []
                    mem.append(screen.copy())
                    if not rclick:
                        draw.rect(screen,WHITE,canvas) #clears everything previously on the canvas if user does not hold shift
                    cfiller = screen.copy().subsurface(canvas)
                    opened_image = image.load(loadname)
                    img_ratio = opened_image.get_width()/opened_image.get_height()
                    if opened_image.get_width() >= opened_image.get_height():
                        width = (min(opened_image.get_width(),800))
                        height = (int(width/img_ratio))
                    else:
                        height = (min(opened_image.get_height(),600))
                        width = (int(height*img_ratio))
                    currtool = selectool #changes current tool to select tool
                    currtool.hasbox = True
                    currtool.selectedbox = transform.scale(opened_image,(width,height)) #makes opened image the box's image
                    currtool.x,currtool.y,currtool.width,currtool.height = 300,50,width,height #creating a select box around uploaded image
                else:
                    print("Invalid image")
            mouse.set_visible(False)
    def disptoolbit(self,screen):
        #displays the toolbit so that user can know what button's tool does
        global comicsans
        mx,my = mouse.get_pos()
        width = comicsans.render(self.toolbit,True,BLOODRED).get_width()+20
        if width + mx + 5 > 1200:
            mx -= width #makes sure toolbit doesn't go off the edge
        if self.func in [yunostamp,kotonohastamp,lucystamp,inoristamp,tokostamp,ryokostamp]:
            #if the the button changes the tool into a special yandere stamp, in which case we add an extra line of text informing the user of the right-click special
            draw.rect(screen,BLACK,(mx,my-53,width,53))
            screen.blit(comicsans.render(self.toolbit,True,BLOODRED),(mx+5,my-48))
            smallfont = font.SysFont("comicsansms",10) #small font
            screen.blit(smallfont.render("RIGHT CLICK ON CANVAS FOR YANDERE VERSION",True,BLOODRED),(mx+5,my-30))
            screen.blit(smallfont.render("[Scroll to change size, space to reset size]",True,BLOODRED),(mx+5,my-17))
        elif self.func in [linetool,brushtool,erasertool]:
            #if it's a resizable and space resettable tool we still add an extra line
            smallfont = font.SysFont("comicsansms",10) #small font
            width = max(width,smallfont.render("[Scroll to change size, space to reset size]",True,BLOODRED).get_width()+20)
            draw.rect(screen,BLACK,(mx,my-40,width,40))
            screen.blit(comicsans.render(self.toolbit,True,BLOODRED),(mx+5,my-35))

            screen.blit(smallfont.render("[Scroll to change size, space to reset size]",True,BLOODRED),(mx+5,my-17))
        else:
            draw.rect(screen,BLACK,(mx,my-30,width,30))
            screen.blit(comicsans.render(self.toolbit,True,BLOODRED),(mx+5,my-25))
            
#MOUSE COLOURS
lcol = BLACK
rcol = RED
#TOOLS
penciltool = Pencil() #pencil tool
brushtool = Brush() #brush tool
erasertool = Eraser() #eraser tool
linetool = Line() #line tool
selectortool = Selector() #selector tool
textool = Text("comicsansms",15) #text tool
shapetool = Shape() #shape tool
selectool = Select() #select tool
spraytool = Spray() #spray tool
filltool = Fill() #fill tool
#stamps
yunostamp = Stamp(yunogasai,yandereyuno) #Yuno Gasai stamp
kotonohastamp = Stamp(kotonohakatsura,yanderekotonoha) #Kotonoha Katsura stamp
lucystamp = Stamp(lucy,yanderelucy) #Lucy stamp
inoristamp = Stamp(inoriyuzuriha,yandereinori) #Inori Yuzuriha stamp
tokostamp = Stamp(tokofukawa,genocidersyo) #Toko Fukawa stamp
ryokostamp = Stamp(ryokoasakura) #Ryoko Asakura stamp
#DROP DOWN BOXES
fontdropdown = DropDownBox(20,390,[Button("font",comicsans.render("Comic Sans MS",True,BLACK),20,410,"Change Font-Family",200,20,"comicsansms"),
                                   Button("font",arial.render("Arial",True,BLACK),20,430,"Change Font-Family",200,20,"arial"),
                                   Button("font",timesnr.render("Times New Roman",True,BLACK),20,450,"Change Font-Family",200,20,"timesnewroman"),
                                   Button("font",lucidaconsole.render("Lucida Console",True,BLACK),20,470,"Change Font-Family",200,20,"lucidaconsole"),
                                   Button("font",impact.render("Impact",True,BLACK),20,490,"Change Font-Family",200,20,"impact"),
                                   Button("font",vladimirscript.render("Vladimir Script",True,BLACK),20,510,"Change Font-Family",200,20,"vladimirscript")],"SELECT FONT")
shapedropdown = DropDownBox(120,200,[Button("shape",comicsans.render("Rectangle",True,BLACK),120,220,"Change Shape",170,20,"rect"),
                                     Button("shape",comicsans.render("Ellipse",True,BLACK),120,240,"Change Shape",170,20,"ellipse")],"CHANGE SHAPE")
#^drop down box for fonts
fontdropdown.items[0].selected = True
shapedropdown.items[0].selected = True
#Fontsize buttons
fontsizebuttons = [Button("fontsize",comicsans.render(" <",True,BLACK),60,370,"Change fontsize",20,20,-1),
                   Button("fontsize",comicsans.render(" >",True,BLACK),100,370,"Change fontsize",20,20,1)]
#shape width buttons
shapewidthbuttons = [Button("shapewidth",comicsans.render(" <",True,BLACK),120,220,"Change width",20,20,-1),
                   Button("shapewidth",comicsans.render(" >",True,BLACK),250,220,"Change width",20,20,1)]
#----TOOL VARIABLES----#
currtool = penciltool #current tool
tools = [Button(penciltool,pencilsprite,20,100,"Pencil: 1 pixel line that follows your mouse"),
         Button(erasertool,eraser,20,150,"Eraser: Erases things to give you a second chance at artful Deadication"),
         Button(brushtool,paintbrush,20,200,"Brush: Nice thick strokes"),
         Button(spraytool,spraycan,20,250,"Spray-paint: Colours random pixels at clicked location"),
         Button(selectortool,dropper,20,300,"Colour selector: Change your mouse colour to colour at clicked location"),
         Button(textool,fancyA,20,350,"Text tool: Write some Deadicated text"),
         Button(selectool,dottedbox,80,100,"Select tool: Select an area and manipulate with Deadication"),
         Button(linetool,linesprite,80,150,"Line tool: Draw a line"),
         Button(shapetool,roundedrect,80,200,"Shape tool: Draw a shape to give your Deadication some structure"),
         Button(filltool,fillbucket,80,250,"Fill tool: Fill an area with a colour (Warning: uses a lot of CPU)"),
         Button("save",saveicon,1120,100,"Save your work of Deadication",60,60),
         Button("open",openicon,1120,170,"Open a previously saved image - right click to open without deleting current work",60,60)]#buttons of all tools user can press
stamps = [[Button(yunostamp,yunoface,550,690,"Paste the cute yet scary Yuno Gasai, of whom violence is no problem",60,60),
         Button(kotonohastamp,kotonohaface,610,690,"Paste the shy yet violent Kotonoha Katsura, who easily goes insane",60,60),
         Button(lucystamp,lucyface,670,690,"Paste the pretty yet ruthless Lucy, who has an amnesiac alter-ego known as Nyu",60,60),
         Button(inoristamp,inoriface,730,690,"Paste the quiet yet deadly Inori Yuzuriha, in whom the crazy Mana Ouma lives",60,60),
         Button(tokostamp,tokoface,790,690,"Paste the antisocial but sadistic Toko Fukawa, who has an alter-ego called Genocider Syo",60,60),
         Button(ryokostamp,ryokoface,850,690,"Paste the apparently cheerful but emotionless Ryoko Asakura, who'll use violence to achieve her goals",60,60)]]
stampage = 0 #which stamp page are we on
#^stamp's 2-d list, each nested list contains the stamps for one stamp page
tools += stamps[0] #adds the first page of stamps to tools
#----CANVAS----#
canvas = Rect(300,50,800,600) #canvas rect
draw.rect(screen,BLACK,(299,49,802,602)) #draws canvas border
draw.rect(screen,WHITE,canvas) #draws canvas
cfiller = screen.copy().subsurface(canvas) #canvas filler
#------BACKGROUND------#
#header and subtitle
header = titlefont.render("YANDERE",True,BLACK) #header word 1 "YANDERE"
header2 = titlefont.render("SPLATTERBOARD",True,BLOODRED) #header word 2 "SPLATTERBOARD"
screen.blit(header,(550,2))
screen.blit(header2,(680,2))
comicsans.set_italic(True) #italicizes subtitle
subtitle = comicsans.render("Great art takes Deadication",True,BLACK) #subtitle
comicsans.set_italic(False)
screen.blit(subtitle,(610,28))
#mini-titles
comicsans.set_underline(True) #underlines mini-titles
tooltitle = comicsans.render("TOOLS",True,BLACK) #Title of tools section
screen.blit(tooltitle,(20,70))
ystamptitle = comicsans.render("STAMPS OF DEADICATION",True,BLOODRED) #Title of Yandere Character Stamps section
screen.blit(ystamptitle,(550,660))
screen.blit(comicsans.render("FONT-SIZE",True,BLACK),(60,350))
comicsans.set_underline(False)
#----COLOR PALETTE----#
draw.rect(screen,DARK_GREY,(40,486,150,60)) #drawing background for palette buttons
screen.blit(comicsans.render("COLOUR PALETTE",True,WHITE),(50,486)) #blitting title of color palette
palette = transform.scale(image.load("images/spectrum_chart.jpg"),(300,194))
palrect = Rect(0,546,300,194) #palette rect
pspot1 = (0,750) #spot of left mouse color on the palette
pspot2 = (0,648) #spot of right mouse color on the palette
palbuttons = [Button("color",Rect(50,506,20,20),50,506,"",20,20,BLACK),
              Button("color",Rect(70,506,20,20),70,506,"",20,20,WHITE),
              Button("color",Rect(90,506,20,20),90,506,"",20,20,RED),
              Button("color",Rect(110,506,20,20),110,506,"",20,20,GREEN),
              Button("color",Rect(130,506,20,20),130,506,"",20,20,BLUE),
              Button("color",Rect(150,506,20,20),150,506,"",20,20,PINK)]#buttons for more specific colors
#----other important variables----#
lastclick = "" #keeps track of last click
filler = screen.copy() #screen filler - used for mouse sprites and toolbits and other temporary pop-ups
mem = [] #memory for previous saves for the undo function
mem2 = [] #memory for saves removed by the undo function for the redo function
boxcp = None #clipboard for boxes (created by the select tool)
#----MAIN LOOP----#
while running:
    #----MUSIC HANDLER----#
    '''
    if not mixer.get_busy():
        song += 1
        if song >= len(music):
            #resets the playlist
            shuffle(music) #randomizes playlist
            song = 0
        music[song].play()'''
    screen.blit(filler,(0,0)) #fills the screen to hide toolbit, mouse sprites and other pop-ups
    #----EVENT LOOP----#
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            mb = mouse.get_pressed()
            mx,my = mouse.get_pos()
            if canvas.collidepoint(mx,my):
                screen.set_clip(canvas)
                #if user clicks canvas
                lastclick = "canvas" #sets last click to canvas
                if e.button == 4:
                    #front scroll
                    currtool.scroll(screen,True)
                elif e.button == 5:
                    #back scroll
                    currtool.scroll(screen,False)
                else:
                    if not textool.hastextbox and not selectool.hasbox:
                        if len(mem) >= 256:
                            del mem[0] #limits memory at 256
                        #makes sure we don't have an open text box or an open select box when we click, as that will just close the selected box and shouldn't be saved into memory
                        mem2 = [] #makes the redo option empty as it shouldn't do anything once new data is added to the screen
                        mem.append(screen.copy()) #adds a screenshot to the undo list memory before the user's change to the canvas
                    if e.button == 1:
                        currtool.lclick(screen) #calls tool's left click method
                    elif e.button == 3:
                        currtool.rclick(screen) #calls tool's right click method
                screen.set_clip(None)
            elif fontdropdown.mainrect.collidepoint(mx,my) or (fontdropdown.menudown and fontdropdown.menurect.collidepoint(mx,my)):
                #if user clicks font drop down menu
                lastclick = "fontdropdown"
                fontdropdown.clickon(screen)
            elif shapedropdown.mainrect.collidepoint(mx,my) or (shapedropdown.menudown and shapedropdown.menurect.collidepoint(mx,my)):
                #if user clicks shape drop down menu
                lastclick = "shapedropdown"
                shapedropdown.clickon(screen)
            elif palrect.collidepoint(mx,my):
                #if user clicks palette
                lastclick = "palette"
            else:
                #if user doesn't click palette or canvas
                lastclick = "" #set last click to "" (which means everything except canvas, drop down boxes and palette)
                screen.set_clip(canvas)
                currtool.outside() #runs current tool's outside function, as user clicked outside of canvas
                screen.set_clip(None)
                #following loop checks for tools/buttons and if we clicked them or not
                for b in palbuttons:
                    if b.istouch():
                        b.clickon(screen)
                        break
                for b in fontsizebuttons:
                    if b.istouch():
                        b.clickon(screen)
                        break
                for b in shapewidthbuttons:
                    if b.istouch():
                        b.clickon(screen)
                        break
                for t in tools:
                    if t.istouch():
                        if t.func != currtool:
                            #tool button clicked
                            if e.button == 3:
                                #handles right clicking on button
                                t.clickon(screen,True)
                            else:
                                #handles left clicking on button
                                t.clickon(screen)
                        break
            if lastclick != "fontdropdown":
                fontdropdown.menudown = False #turns off menu in fontdropdown if it was not clicked
            if lastclick != "shapedropdown":
                shapedropdown.menudown = False #turns off menu in shapedropdown if it was not clicked
        if e.type == MOUSEBUTTONUP:
            if lastclick == "canvas":
                if e.button not in [4,5]:
                    currtool.mouseup(screen) #tool's mouseup method
        if e.type == KEYDOWN:
            #----KEY PRESS FUNCTIONS----#
            kp = key.get_pressed()
            canundo = True #can the user undo under the circumstances (applies to redo as well)
            if type(currtool) == Text:
                if currtool.hastextbox:
                    #if the current tool has a text box, you cannot undo
                    canundo = False
            elif type(currtool) == Select:
                if currtool.hasbox:
                    #if the current tool has a box, you cannot undo
                    canundo = False
            if kp[K_z] and (kp[K_LCTRL] or kp[K_RCTRL]) and (kp[K_LSHIFT] or kp[K_RSHIFT]) and canundo:
                #if the user pressed Ctrl-Shift-Z will redo
                if len(mem2) > 0:
                    if len(mem) >= 256:
                        del mem[0] #removes the last thing memorized if we're over the limit
                    mem.append(screen.copy()) #appends current screen to undo list
                    prevsave = mem2.pop(-1) #gets new screen from redo list
                    screen.blit(prevsave,(0,0))
            elif kp[K_z] and (kp[K_LCTRL] or kp[K_RCTRL]) and canundo:
                #if the user presses Ctrl-Z will undo
                if len(mem) > 0:
                    mem2.append(screen.copy()) #appends the current screen to redo list
                    prevsave = mem.pop(-1) #prevsave = last screen save
                    screen.blit(prevsave,(0,0)) #fills the screen with new save
            elif kp[K_SPACE] and (kp[K_LCTRL] or kp[K_RCTRL]):
                #clears the canvas if user presses CTRL and space
                if len(mem) >= 256:
                    del mem[0] #removes the last thing memorized if we're over the limit
                mem2 = [] #makes the redo option empty as it shouldn't do anything once new data is added to the screen
                mem.append(screen.copy()) #adds a screenshot to the undo list memory before the user's change to the canvas
                draw.rect(screen,WHITE,canvas)
            elif kp[K_s] and (kp[K_LCTRL] or kp[K_RCTRL]):
                #if user presses CTRL-S will save
                if not canundo:
                    if type(currtool) == Select:
                        currtool.hasbox = False
                    elif type(currtool) == Text:
                        currtool.hastextbox = False
                mouse.set_visible(True)
                loadname = filedialog.asksaveasfilename()
                if loadname:
                    if loadname[-4:] in [".jpg",".png",".bmp",".gif"]:
                        ext = ""
                    else:
                        ext = ".jpg"
                    image.save(screen.copy().subsurface(canvas), loadname + ext)
                mouse.set_visible(False)
                root.destroy()
                root = Tk() #allows user to use window again by resetting the window
                root.withdraw()
            elif kp[K_o] and (kp[K_LCTRL] or kp[K_RCTRL]):
                #if user presses CTRL-O will open a file and paste it onto canvas
                if not canundo:
                    if type(currtool) == Select:
                        currtool.hasbox = False
                    elif type(currtool) == Text:
                        currtool.hastextbox = False
                mouse.set_visible(True)
                loadname = filedialog.askopenfilename()
                if loadname:
                    if loadname[-4:] in [".jpg",".png",".gif",".bmp"]:
                        if len(mem) >= 256:
                            del mem[0] #removes the last thing memorized if we're over the limit
                        mem2 = []
                        mem.append(screen.copy())
                        if not kp[K_LSHIFT] and not kp[K_RSHIFT]:
                            draw.rect(screen,WHITE,canvas) #clears everything previously on the canvas if user does not hold shift
                        cfiller = screen.copy().subsurface(canvas)
                        opened_image = image.load(loadname)
                        img_ratio = opened_image.get_width()/opened_image.get_height()
                        if opened_image.get_width() >= opened_image.get_height():
                            width = (min(opened_image.get_width(),800))
                            height = (int(width/img_ratio))
                        else:
                            height = (min(opened_image.get_height(),600))
                            width = (int(height*img_ratio))
                        currtool = selectool #changes current tool to select tool
                        currtool.hasbox = True
                        currtool.selectedbox = transform.scale(opened_image,(width,height)) #makes opened image the box's image
                        currtool.x,currtool.y,currtool.width,currtool.height = 300,50,width,height #creating a select box around uploaded image
                    else:
                        print("Invalid image")
                root.destroy()
                root = Tk() #allows user to use window again by resetting the window
                root.withdraw()
                mouse.set_visible(False)
            elif kp[K_v] and (kp[K_LCTRL] or kp[K_RCTRL]):
                #CTRL-V
                #pastes clipboard image
                if boxcp != None:
                    screen.set_clip(canvas)
                    if selectool.hasbox:
                        #if we have a select box, we paste the image in there instead
                        if selectool.selectedbox != boxcp[0]:
                            #if the current selection is not the clipboard, we paste it to ensure it isn't lost
                            screen.blit(selectool.selectedbox,(selectool.x,selectool.y))
                            cfiller = screen.copy().subsurface(canvas)
                            selectool.selectedbox = boxcp[0]
                            selectool.width = boxcp[0].get_width()
                            selectool.height = boxcp[0].get_height()
                    else:
                        #we blit the image to where we copied it from in a select box
                        selectool.selectedbox = boxcp[0]
                        selectool.x = boxcp[1][0]
                        selectool.y = boxcp[1][1]
                        selectool.width = boxcp[0].get_width()
                        selectool.height = boxcp[0].get_height() #setting up the box to contain the image
                        selectool.hasbox = True
                        cfiller = screen.copy().subsurface(canvas)
                        currtool = selectool
                    screen.set_clip(None)
            else:
                currtool.keypress(screen,e.unicode)#uses current tool's keypress method
            
    #----BACKGROUND----#
    #draws boxes that indicate color of both mouse buttons
    draw.rect(screen,lcol,(300,650,40,40))
    draw.rect(screen,rcol,(340,650,40,40))
    #draw dropdownboxes
    fontdropdown.drawbox(screen)
    shapedropdown.drawbox(screen)
    #----DRAWING PALETTE----#
    for b in palbuttons:
        b.display(screen)
    screen.blit(palette,(0,546))
    #----DRAWING BUTTONS----#
    for b in tools:
        b.display(screen)
    for b in fontsizebuttons:
        b.display(screen)
    for b in shapewidthbuttons:
        b.display(screen)
    draw.rect(screen,PINK,(80,370,20,20))
    screen.blit(comicsans.render(str(textool.fontsize),True,BLACK),(80,370)) #displays fontsize for textbox
    draw.rect(screen,PINK,(140,220,110,20))
    dispwidth = "Border size: "+str(shapetool.width) if shapetool.width > 0 else "No border (fill)"
    screen.blit(comicsans.render(dispwidth,True,BLACK),(140,220)) #displays width of shapetool for shape tool
    #----MOUSE HOLD FUNCTIONS----#
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()
    if mb[0] or mb[2]:
        if canvas.collidepoint(mx,my) and lastclick == "canvas":
                screen.set_clip(canvas)
                currtool.cont(screen)
                screen.set_clip(None)
        else:
            screen.set_clip(canvas)
            currtool.outside()
            screen.set_clip(None)
            if palrect.collidepoint(mx,my) and lastclick == "palette":
                #if user clicked in palette, the following if statements will change the color of either his left mouse or his right mouse button
                if mb[0]:
                    lcol = screen.get_at((mx,my))
                    pspot1 = (mx,my) #changes position of left-mouse circle on canvas
                elif mb[2]:
                    rcol = screen.get_at((mx,my))
                    pspot2 = (mx,my) #changes position of right-mouse circle on canvas
    elif mb[1]:
        pass
    else:
        #following loops highlights all hovered buttons and unhighlights all non-hovered buttons
        for t in tools:
            if t.istouch():
                t.highlighted = True
            else:
                t.highlighted = False
        for b in fontsizebuttons:
            if b.istouch():
                b.highlighted = True
            else:
                b.highlighted = False
        for b in shapewidthbuttons:
            if b.istouch():
                b.highlighted = True
            else:
                b.highlighted = False
        if fontdropdown.istouch():
            fontdropdown.highlighted = True
        else:
            fontdropdown.highlighted = False #sets highlighted of fontdropdown box
        if shapedropdown.istouch():
            shapedropdown.highlighted = True
        else:
            shapedropdown.highlighted = False #sets highlighted of shapedropdown box
    #----SCREEN SAVING----#  
    filler = screen.copy() #copies all updates into filler
    #----Temporary drawings that should never stick to screen (e.g. sprites and toolbits)----#
    #DRAWS TOOLBIT
    #following loop displays toolbit if the mouse is touching the button
    for t in tools:
        if t.istouch():
            t.disptoolbit(screen)
            break
    #DRAWS TEXTBOX IF THE TEXT TOOL IS SELECTED AND A TEXTBOX IS OPEN
    if type(currtool) == Text:
        if currtool.hastextbox:
            currtool.textbox.drawtext(screen,False)
    #DRAWS SELECTED BOX IF THE SELECT TOOL IS SELECTED AND A SELECTED BOX EXISTS
    if type(currtool) == Select:
        if currtool.hasbox:
            draw.rect(screen,BLACK,(currtool.x-1,currtool.y-1,currtool.width+2,currtool.height+2),1)
            try:
                screen.blit(transform.smoothscale(currtool.selectedbox,(currtool.width,currtool.height)),(currtool.x,currtool.y))
            except:
                screen.blit(transform.scale(currtool.selectedbox,(currtool.width,currtool.height)),(currtool.x,currtool.y))
            sizepoints = [(currtool.x-1,currtool.y-1),(currtool.x+currtool.width+1,currtool.y-1),
                          (currtool.x-1,currtool.y+currtool.height+1),(currtool.x+currtool.width+1,currtool.y+currtool.height+1),
                          (currtool.x+(currtool.width+1)//2,currtool.y-1),(currtool.x+(currtool.width+1)//2,currtool.y+currtool.height+1),
                          (currtool.x-1,currtool.y+(currtool.height+1)//2),(currtool.x+currtool.width+1,currtool.y+(currtool.height+1)//2)] #points in which the size of the box can be altered
            for x,y in sizepoints:
                draw.rect(screen,(255,50,50,150),(x-5,y-5,10,10),1)
    #HANDLES DROP DOWN MENUS
    if fontdropdown.menudown:
        for i in fontdropdown.items:
            #sets all highlighted items in dropdown menu to highlighted or unhighlighted
            if i.istouch():
                i.highlighted = True
            else:
                i.highlighted = False
        fontdropdown.dropdown(screen)
    if shapedropdown.menudown:
        for i in shapedropdown.items:
            #sets all highlighted items in dropdown menu to highlighted or unhighlighted
            if i.istouch():
                i.highlighted = True
            else:
                i.highlighted = False
        shapedropdown.dropdown(screen)
    #DRAWS CIRCLES OF COLOR INDICATION ON PALETTE
    draw.circle(screen,WHITE,pspot1,10,1)
    draw.circle(screen,BLOODRED,pspot2,10,1)
    #DRAWS MOUSE SPRITE
    if canvas.collidepoint(mx,my):
        mouse.set_visible(False)
        currtool.drawsprite(screen)
    else:
        mouse.set_visible(True)
    display.flip()
root.destroy()
quit()
