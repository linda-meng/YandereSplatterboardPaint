import os
from random import *
from math import *
from tkinter import *
from tkinter import filedialog as filedialog
from pygame import *
from pygame import time as pytime
from time import *
font.init()
#----METADATA----#
__author__ = "Yttrium Z (You Zhou)"
__date__ = "January 29th, 2016"
__purpose__ = "Grade 11 Project - Paint Program"
__name__ = "Yandere Splatterboard"
__copyright__ = "Yttrium Z 2015-2016"
#----SETUP----#
os.environ['SDL_VIDEO_WINDOW_POS'] = '25,25'
root = Tk()
root.withdraw() #makes sure file dialog box disappears after it closes
screen = display.set_mode((1200,750))
try:
    display.set_icon(transform.scale(image.load("images/icon.jpg"),(32,32))) #sets icon
except:
    pass
display.set_caption("YANDERE SPLATTERBOARD - PAINT PROGRAM BY YTTRIUM Z ~~~~~~GREAT ART TAKES DEADICATION~~~~~~","Yandere Splatterboard")
#----LOADING SCREEN----#
screen.blit(image.load("images/LoadScreen.png"),(0,0))
draw.rect(screen,(255,0,0),(143,466,80,27))
display.flip()
#----PERMANENT CONSTANT DATA----#
#data that can never change no matter what user does
#MUSIC (Really lags up the program startup)
init()
mixer.init()
music = [mixer.Sound("music/My_Dearest.ogg"),
        mixer.Sound("music/MiraiNikkiOP.ogg"),
        mixer.Sound("music/InnocentBlue.ogg"),
        mixer.Sound("music/Lillium.ogg"),
        mixer.Sound("music/BoukenDesho.ogg"),
        mixer.Sound("music/NeverSayNever.ogg")]
'''
'''
shuffle(music) #shuffles the music
music[0].play()
song = 0 #which song are we playing
draw.rect(screen,(255,0,0),(143,466,420,27))
display.flip()
#COLOR
WHITE = (255,255,255,255)
BLACK = (0,0,0,255)
LIGHT_GREY = (180,180,180,255)
DARK_GREY = (50,50,50,255)
GREY = (100,100,100,255)
PINK = (255,150,150,255)
RED = (255,0,0,255)
BLOODRED = (220,0,0,255)
BLUE = (0,0,255,255)
GREEN = (0,255,0,255)
YELLOW = (255,255,0,255)
CYAN = (0,255,255,255)
MAGENTA = (255,0,255,255)
alpha = 100 #alpha %
draw.rect(screen,(255,0,0),(143,466,500,27))
display.flip()
#FONTS
comicsans = font.SysFont("comicsansms", 15)
arial = font.SysFont("arial",15)
timesnr = font.SysFont("timesnewroman",15)
lucidaconsole = font.SysFont("lucidaconsole",15)
impact = font.SysFont("impact",15)
vladimirscript = font.SysFont("vladimirscript",15)
chiller = font.SysFont("chiller",15)
titlefont = font.SysFont("chiller",48)
draw.rect(screen,(255,0,0),(143,466,580,27))
display.flip()
#SPRITES AND IMAGES
pencilsprite = transform.scale(image.load("images/pencil.png"),(40,40)).convert_alpha()
eraser = transform.scale(image.load("images/eraser.gif"),(40,40)).convert_alpha()
paintbrush = transform.scale(image.load("images/paintbrush.png"),(40,40)).convert_alpha()
linesprite = transform.scale(image.load("images/linesprite.png"),(40,40)).convert_alpha()
dropper = transform.scale(image.load("images/dropper.png"),(40,40)).convert_alpha()
fancyA = transform.scale(image.load("images/A.png"),(40,40)).convert_alpha()
roundedrect = transform.scale(image.load("images/roundrect.png"),(40,40)).convert_alpha()
ellipsesprite = transform.scale(image.load("images/ellipse.png"),(40,40)).convert_alpha()
polygonsprite = transform.scale(image.load("images/polygon.png"),(40,40)).convert_alpha()
dottedbox = transform.scale(image.load("images/dottedbox.gif"),(40,40)).convert_alpha()
fillbucket = image.load("images/fillbucket.png").convert_alpha()
bluricon = transform.scale(image.load("images/waterdrop.png"),(40,40)).convert_alpha()
pixelateicon = transform.scale(image.load("images/pixelateicon.gif"),(40,40)).convert_alpha()
spraycan = transform.scale(image.load("images/spraypaint.png"),(40,40)).convert_alpha()
ibeam = transform.scale(image.load("images/ibeam.png"),(40,40)).convert_alpha()
crosscursor = transform.scale(image.load("images/crosscursor.gif"),(40,40)).convert_alpha()
magicwand = image.load("images/magicwand.png").convert_alpha()
saveicon = transform.scale(image.load("images/saveicon.png"),(60,60)).convert_alpha()
openicon = transform.scale(image.load("images/openicon.png"),(60,60)).convert_alpha()
undoicon = transform.scale(image.load("images/undo.png"),(60,60)).convert_alpha()
redoicon = transform.flip(undoicon,True,False)
clearicon = transform.scale(image.load("images/Red_X.png"),(60,60)).convert_alpha()
clipboard = image.load("images/clipboard.png").convert_alpha()
mirainikkibackdrop = image.load("images/mirainikkibackdrop.jpg").convert()
schooldaysbackdrop = image.load('images/schooldaysbackdrop.jpg').convert()
elfenliedbackdrop = image.load('images/elfenliedbackdrop.jpg').convert()
guiltycrownbackdrop = image.load("images/guiltycrownbackdrop.jpg").convert()
danganronpabackdrop = image.load('images/danganronpabackdrop.png').convert()
haruhibackdrop = image.load('images/haruhibackdrop.jpg').convert()
yunoface = transform.smoothscale(image.load("images/yunoface.png"),(50,50)).convert_alpha()
yunogasai = image.load("images/yunogasai.png").convert_alpha()
yandereyuno = image.load("images/yandereyuno.png").convert_alpha()
kotonohaface = transform.smoothscale(image.load("images/kotonoha.png"),(50,50)).convert_alpha()
kotonohakatsura = image.load("images/kotonohakatsura.png").convert_alpha()
yanderekotonoha = image.load("images/yanderekotonoha.png").convert_alpha()
lucyface = transform.smoothscale(image.load("images/lucyface.png"),(50,50)).convert_alpha()
lucy = image.load("images/lucy.png").convert_alpha()
yanderelucy = image.load("images/yanderelucy.png").convert_alpha()
inoriface = transform.smoothscale(image.load("images/inoriface.png"),(50,50)).convert_alpha()
inoriyuzuriha = image.load("images/inoriyuzuriha.png").convert_alpha()
yandereinori = image.load("images/yandereinori.png").convert_alpha()
tokoface = transform.smoothscale(image.load("images/tokoface.png"),(50,50)).convert_alpha()
tokofukawa = image.load("images/tokofukawa.png").convert_alpha()
genocidersyo = image.load("images/genocidersyo.png").convert_alpha()
ryokoface = transform.smoothscale(image.load("images/ryokoface.png"),(50,50)).convert_alpha()
ryokoasakura = image.load("images/ryokoasakura.png").convert_alpha()
yandereryoko = image.load("images/yandereryoko.png").convert_alpha()
yukkiface = transform.smoothscale(image.load('images/yukkiface.png'),(50,50)).convert_alpha()
yukiteruamano = image.load("images/yukiteruamano.png").convert_alpha()
makotoface = transform.smoothscale(image.load("images/makotoface.png"),(50,50)).convert_alpha()
makotoitou = image.load("images/makotoitou.png").convert_alpha()
koutaface = transform.smoothscale(image.load("images/koutaface.png"),(50,50)).convert_alpha()
kouta = image.load("images/kouta.png").convert_alpha()
shuface = transform.smoothscale(image.load("images/shuface.png"),(50,50)).convert_alpha()
shuouma = image.load("images/shuouma.png").convert_alpha()
byakuyaface = transform.smoothscale(image.load("images/byakuyaface.png"),(50,50)).convert_alpha()
byakuyatogami = image.load("images/byakuyatogami.png").convert_alpha()
yukiface = transform.smoothscale(image.load("images/yukiface.png"),(50,50)).convert_alpha()
yukinagato = image.load("images/yukinagato.png").convert_alpha()
kitchenknife = image.load("images/kitchenknife.png").convert_alpha()
kitchenknifeicon = transform.smoothscale(kitchenknife,(50,50))
butcherknife = image.load("images/butcherknife.png").convert_alpha()
butcherknifeicon = Surface((50,50),SRCALPHA)
butcherknifeicon.blit(transform.smoothscale(butcherknife,(50,25)),(0,12))
katana = image.load("images/katana.png").convert_alpha()
katanaicon = Surface((50,50),SRCALPHA)
katanaicon.blit(transform.smoothscale(katana,(50,25)),(0,12))
axe = image.load("images/axe.png").convert_alpha()
axeicon = transform.smoothscale(axe,(50,50))
scissors = image.load("images/scissors.png").convert_alpha()
scissorsicon = transform.smoothscale(scissors,(50,50))
cutterknife = image.load("images/cutterknife.png").convert_alpha()
cutterknifeicon = Surface((50,50),SRCALPHA)
cutterknifeicon.blit(transform.smoothscale(cutterknife,(50,17)),(0,16))
flipicon = image.load("images/flip.png").convert_alpha()
rotateicon = image.load("images/rotate.png").convert_alpha()
redarrow = transform.scale(image.load("images/RedArrowDown.png"),(30,30)).convert_alpha()
redtriangle = image.load("images/redtriangle.png").convert_alpha()
infobox = image.load("images/info.png").convert_alpha()
draw.rect(screen,(255,0,0),(143,466,809,27))
display.flip()
screen.blit(image.load("images/LoadScreen2.png"),(0,0)) #second loading screen - just for fun right before loaded
display.flip()
#Finalizes Screen
screen.blit(image.load("images/background.png"),(0,0))
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
        self.irow = 0 #position of insertion point row and column
        self.icol = 0
    def changefont(self,fontfamily,fontsize,col=None):
        if col != None:
            self.col = col #sets color
        self.fontfamily = fontfamily #sets fontfamily
        self.fontsize = fontsize #sets fontsize
        decor = (("bold",self.tbfont.get_bold()),("italic",self.tbfont.get_italic()),("underline",self.tbfont.get_underline())) #tuple of text decor
        self.tbfont = font.SysFont(fontfamily,self.fontsize)
        for t,d in decor:
            if d:
                exec("self.tbfont.set_"+t+"(True)")
    def writeto(self,char):
        #writes a character in the box
        if char == "":
            return 0 #makes sure we actually have a character to input (random keys like shift will move the cursor and that's not good)
        irow,icol = self.irow,self.icol
        self.text[irow] = self.text[irow][:icol] + char + self.text[irow][icol:] #inserts character right before insertion point
        self.icol += 1
        self.width = max([self.tbfont.render(self.text[i],True,BLACK).get_width() for i in range(self.lines)])
        self.height = self.tbfont.render(self.text[irow],True,BLACK).get_height()*self.lines
    def delete(self):
        #deletes character in front of insertion point
        if self.icol == len(self.text[self.irow]) and self.lines - self.irow > 1:
            #if there's nothing in the current line, removes line altogether
            self.text[self.irow] += self.text[self.irow+1] #adds the text of current line to previous line
            del self.text[self.irow+1]
            self.lines -= 1
        else:
            self.text[self.irow] = self.text[self.irow][:self.icol] + self.text[self.irow][self.icol+1:]
        self.width = max([self.tbfont.render(self.text[i],True,BLACK).get_width() for i in range(self.lines)]) #sets width to be maximum of the lines
        self.height = self.tbfont.render(self.text[-1],True,BLACK).get_height()*self.lines #sets height
    def backspace(self):
        #deletes character behind insertion point
        if self.icol == 0 and self.lines > 1 and self.irow > 0:
            #if the insertion point is at the beginning of line we move it back
            self.icol = len(self.text[self.irow-1]) #sets insertion point column at the end of the line moved to
            self.text[self.irow-1] += self.text[self.irow] #adds the text of current line to previous line
            del self.text[self.irow]
            self.lines -= 1
            self.irow -= 1 #moves the row one up
        elif self.irow != 0 or self.icol != 0:
            self.text[self.irow] = self.text[self.irow][:self.icol-1] + self.text[self.irow][self.icol:]
            self.icol -= 1
        self.icol = max(0,self.icol) #limits insertion point column at 0
        self.width = max([self.tbfont.render(self.text[i],True,BLACK).get_width() for i in range(self.lines)]) #sets width to be maximum of the lines
        self.height = self.tbfont.render(self.text[-1],True,BLACK).get_height()*self.lines #sets height
    def newline(self):
        self.lines += 1
        #inserts new line after insertion point
        self.irow += 1
        self.text = self.text[:self.irow] + [self.text[self.irow-1][self.icol:]] + self.text[self.irow:]
        self.text[self.irow-1] = self.text[self.irow-1][:self.icol] #trims the part of the line moved to the new line
        self.icol = 0
        self.height = self.tbfont.render(self.text[-1],True,BLACK).get_height()*self.lines
        self.width = max([self.tbfont.render(self.text[i],True,BLACK).get_width() for i in range(self.lines)]) #sets width to be maximum of the lines
    def drawtext(self,screen,perm=True):
        #draws text to screen
        if not perm:
            #if it isn't permanent drawing
            #draws a box to fit the text of the text box drawn by the text tool
            draw.rect(screen,self.col,(self.x-2,self.y-2,self.width+4,self.height+4),2)
            #draws insertion point if time is at the right interval (causes blinking effect)
            if time() % 0.9 < 0.45:
                draw.line(screen,self.col,
                          (self.x+self.tbfont.render(self.text[self.irow][:self.icol],True,BLACK).get_width(),self.y+self.tbfont.render(self.text[-1],True,BLACK).get_height()*self.irow),
                          (self.x+self.tbfont.render(self.text[self.irow][:self.icol],True,BLACK).get_width(),self.y+self.tbfont.render(self.text[-1],True,BLACK).get_height()*self.irow+self.tbfont.render(self.text[self.irow][:self.icol],True,BLACK).get_height()))
        else:
            screen.set_clip(canvas)
        for i in range(self.lines):
            screen.blit(self.tbfont.render(self.text[i],True,self.col),(self.x,self.y+(self.height//self.lines)*i))#blits font to screen
        screen.set_clip(None)
    def get_rect(self):
        #returns rect
        return Rect(self.x,self.y,self.width,self.height)
#-----------------------------DROPDOWNBOX
class DropDownBox():
    #drop down box
    def __init__(self,x,y,items,name,width=None,height=None):
        self.items = items #list of all the items, all items are buttons
        if width == None:
            self.width = max([i.width for i in items]) #width of dropdown box becomes maximum width of item in list if no width is given
        else:
            self.width = width #sets self.width to be width
        if height == None:
            self.height = max([i.height for i in items]) #same idea for height as width, but for height
        else:
            self.height = height #sets self.height to be height
        self.name = name #display of drop down
        self.x = x
        self.y = y #co-ords
        self.itemrects = [Rect(i.x,i.y,i.width,i.height) for i in self.items]#item rects
        self.menudown = False #is the menu down?
        self.mainrect = Rect(self.x,self.y,self.width+min(self.width,self.height),self.height)#main rect of the drop down box (not it's items)
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
        if self.istouch():
            col = LIGHT_GREY
        else:
            col = WHITE
        smallerd = min(self.height,self.width) #smaller dimension (of width and height)
        draw.rect(screen,col,(self.x,self.y,self.width+smallerd,self.height)) #draws box
        screen.blit(comicsans.render(self.name,True,BLACK),(self.x+2,self.y+self.height//2-10))
        draw.rect(screen,LIGHT_GREY,(self.x+self.width,self.y,smallerd,smallerd)) #draws box around arrow
        screen.blit(transform.scale(redtriangle,(smallerd,smallerd)),(self.x+self.width,self.y)) #draws drop down box's arrow
        draw.rect(screen,BLACK,(self.x,self.y,self.width+smallerd,self.height),1) #draws box's border
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
#-----------------------------GRADIENTSELECTOR
class GradSel():
    #Gradient selector, let's user choose whiteness and blackness of color
    #it is a rectangle gradient whose base color changes based on user's mouse color(s)
    def __init__(self,x,y,width=300,height=60):
        global lcol
        self.color = lcol
        self.clicked = 0 #left mouse button or right mouse button? (0 = left mouse, 1 = right mouse,-1 means not clicking)
        self.x,self.y = x,y #sets co-ords and dimensions
        self.width = width
        self.height = height
        self.selected = self.width//2 #selected color (0 means black; width means white; half of width means the color)
    def lclick(self,screen):
        #left click function
        #changes gradient to lcol
        global lcol
        self.clicked = 0
        self.color = lcol #sets its own color to lcol
    def rclick(self,screen):
        #right click function
        #sets mouse color to 
        global rcol
        self.clicked = 1
        self.color = rcol #sets its own color to rcol
    def cont(self,screen):
        #sets mouse color to where mouse is
        global lcol,rcol
        mx,my = mouse.get_pos()
        self.selected = mx-self.x #sets selected to mousex - self.x as that would be the location of color relative to box
        if self.clicked:
            rcol = screen.get_at((self.x+self.selected,self.y)) #right click sets right mouse button
            rcol = Color(rcol[0],rcol[1],rcol[2],int(alpha/100*255))#sets transparency
        else:
            lcol = screen.get_at((self.x+self.selected,self.y)) #left click sets left mouse button
            lcol = Color(lcol[0],lcol[1],lcol[2],int(alpha/100*255))#sets transparency
    def mouseup(self,screen):
        self.clicked = -1
        self.selected = self.width//2
    def draw(self,screen):
        #draws itself
        if self.clicked == -1:
            col = lcol #if the user isn't clicking we display the left color
        else:
            col = self.color #its own color
        #the following variables are increment variables
        #they show how much we must increment each color by every loop to go from black to the color
        ri = col[0]/(self.width//2) #increment for red 
        gi = col[1]/(self.width//2) #increment for green
        bi = col[2]/(self.width//2) #increment for blue
        #we draw lines to make a gradient rectangle
        for i in range(self.width//2+1):
            #the color is the increment multiplied by the the loop
            #this is so the color goes from black slowly to the color
            draw.line(screen,(int(ri*i),int(gi*i),int(bi*i)),(i+self.x,self.y),(i+self.x,self.y+self.height))
        #the following variables are the same as ri,gi and bi, but they increase into white instead of black
        ri2 = (255-col[0])/(self.width//2) #increment for red
        gi2 = (255-col[1])/(self.width//2) #increment for green
        bi2 = (255-col[2])/(self.width//2) #increment for blue
        for i in range(self.width-self.width//2):
            #same as the previous loop, except it goes from color to white
            draw.line(screen,(int(ri2*i+col[0]),int(gi2*i+col[1]),int(bi2*i+col[2])),(i+self.x+self.width//2,self.y),(i+self.x+self.width//2,self.y+self.height))
    def drawSel(self,screen):
        #DRAWS SELECTED POINT
        draw.line(screen,PINK,(self.x+self.selected,self.y),(self.x+self.selected,self.y+self.height)) #draws a pink line
        screen.blit(redarrow,(self.x+self.selected-15,self.y-10)) #draws a red arrow
    def istouch(self):
        #is the mouse touching the gradient selector? Well this method says!
        mx,my = mouse.get_pos()
        #we check if it touches the arrow and if the x co-ord is still within the gradient
        #this is to make sure the mouse does not go off the gradient via arrow
        if Rect(self.x+self.selected-15,self.y-10,30,30).collidepoint((mx,my)) and self.x <= mx < self.x+self.width:
            #if the user is clicking the red arrow we also allow touch
            return True
        return Rect(self.x,self.y,self.width,self.height).collidepoint((mx,my)) #otherwise we return true if the user pressed the gradient box
#-----------------------------VOLUME SLIDER
class volSlider():
    def __init__(self,x,y,width,height):
        self.x,self.y,self.width,self.height = x,y,width,height #dimensions and co-ords of volume slider
        self.sliderheight = self.height-20  #height of slider
        self.sliderx = self.x+(self.width-20)//2#x co-ord of slider pos
        self.place = 1 #place of volume slider
    def istouch(self):
        #is the mouse touching the volume slider? Well this method says!
        mx,my = mouse.get_pos()
        #we check if the mouse collides with the slider
        return Rect(self.sliderx,self.y+5,20,self.sliderheight+5).collidepoint(mx,my)
    def cont(self,screen):
        mx,my = mouse.get_pos()
        #while mouse is being held on volume slider
        self.place = ((self.y+self.sliderheight+5) - min(max(self.y+5,my),self.y+self.sliderheight+5))/self.sliderheight
        for m in music:
            m.set_volume(self.place) #sets all the music to a volume
    def draw(self,screen):
        #draws volume indicator box on top
        draw.rect(screen,WHITE,(self.x,self.y-40,self.width,40))
        comicsans.set_underline(True)
        screen.blit(comicsans.render("Volume Level",True,BLACK),(self.x,self.y-40))
        comicsans.set_underline(False)
        screen.blit(comicsans.render(str(round(self.place*100))+"%",True,BLACK),(self.x,self.y-20))
        #draws volume box
        draw.rect(screen,LIGHT_GREY,(self.x,self.y,self.width,self.height))
        #draws slider line
        draw.line(screen,WHITE,(self.sliderx+10,self.y+5),(self.sliderx+10,self.y+self.height-6))
    def drawSel(self,screen):
        #draws the volume selector
        draw.rect(screen,RED,(self.sliderx,self.y+int((1-self.place)*self.sliderheight)+5,20,10))

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
        screen.blit(tempdraw,(0,0)) #blits temporary drawing board (it is a drawing board to support transparency, it is declared below the classes)
        tempdraw.fill((255,255,255,0))#clears temporary drawing board
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
        draw.line(tempdraw,self.col,(self.sx,self.sy),(mx,my))
        self.sx = mx
        self.sy = my #changes the sx and sy to mx and my to keep make it follow the mouse
    def outside(self):
        #continues drawing if the last click was canvas - it won't draw outside of canvas because of clipping before calling this method
        global lastclick
        if lastclick == "canvas":
            self.cont(screen)
        else:
            screen.blit(tempdraw,(0,0)) #blits tempdraw
            tempdraw.fill((255,255,255,0)) #clears tempdraw
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
            if self.size > 0:
                #makes sure eraser size doesn't go below 1
                self.size -= 1
    def cont(self,screen):
        #erases in a line that follows user's mouse - same idea as pencil but uses a line of circles instead of an actual line
        mx,my = mouse.get_pos()
        if self.size > 0:
            #line algorithm
            dist = ((mx-self.sx)**2+(my-self.sy)**2)**0.5 #distance
            dist = max(1,dist) #makes sure distance isn't 0 so division by 0 doesn't occur
            lx = (mx-self.sx)/dist #increment of x and y values of the line
            ly = (my-self.sy)/dist
            for i in range(int(dist)):
                draw.circle(screen,WHITE,(int(self.sx+lx*i),int(self.sy+ly*i)),self.size)
        else:
            #draws a simple line
            draw.line(screen,WHITE,(self.sx,self.sy),(mx,my))
        self.sx = mx
        self.sy = my
    def outside(self):
        #continues drawing if the last click was canvas - it won't draw outside of canvas because of clipping before calling this method
        global lastclick
        if lastclick == "canvas":
            self.cont(screen)
    def drawsprite(self,screen):
        mx,my = mouse.get_pos()
        if self.size > 0:
            draw.circle(screen,WHITE,(mx,my),self.size) #draws circle to show user how big eraser is
        else:
            screen.set_at((mx,my),WHITE)
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
            if self.size > 0:
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
        if self.size > 0:
            #line algorithm
            dist = ((mx-self.sx)**2+(my-self.sy)**2)**0.5 #distance
            dist = max(1,dist) #makes sure distance isn't 0 so division by 0 doesn't occur
            lx = (mx-self.sx)/dist #increment of x and y values of the line
            ly = (my-self.sy)/dist
            for i in range(int(dist)):
                draw.circle(tempdraw,self.col,(int(self.sx+lx*i),int(self.sy+ly*i)),self.size)
        else:
            #draws a simple line
            draw.line(tempdraw,self.col,(self.sx,self.sy),(mx,my))
        self.sx = mx
        self.sy = my
    def outside(self):
        #continues drawing if the last click was canvas - it won't draw outside of canvas because of clipping before calling this method
        global lastclick
        if lastclick == "canvas":
            self.cont(screen)
        else:
            screen.blit(tempdraw,(0,0)) #blits tempdraw
            tempdraw.fill((255,255,255,0)) #clears tempdraw
    def drawsprite(self,screen):
        global lcol
        global rcol
        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()
        if mb[2]:
            self.col = rcol
        else:
            self.col = lcol
        if self.size > 0:          
            tempdraw2 = Surface((self.size*2,self.size*2),SRCALPHA) #small drawing board for the transparent sprite
            draw.circle(tempdraw2,(self.col),(self.size,self.size),self.size) #draws circle to show user how big brush is
            screen.blit(tempdraw2,(mx-self.size,my-self.size))
        else:
            screen.set_at((mx,my),self.col)
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
        screen.blit(tempdraw,(0,0)) #blits temporary drawing board
        mx,my = mouse.get_pos()
        self.col = lcol #changes color to left mouse color
        self.sx = mx #changes starting point of line to where user clicked
        self.sy = my
    def rclick(self,screen):
        global rcol
        self.lclick(screen) #changes color to right mouse color, the rest is the same as left click
        self.col = rcol
    def cont(self,screen):
        tempdraw.fill((255,255,255,0)) #clears tempdraw
        #same algorithm as brush tool
        mx,my = mouse.get_pos()
        if self.size > 0:
            #line algorithm
            dist = ((mx-self.sx)**2+(my-self.sy)**2)**0.5 #distance
            dist = max(1,dist) #makes sure distance isn't 0 so division by 0 doesn't occur
            lx = (mx-self.sx)/dist #increment of x and y values of the line
            ly = (my-self.sy)/dist
            for i in range(int(dist)):
                draw.circle(tempdraw,self.col,(int(self.sx+lx*i),int(self.sy+ly*i)),self.size)
        else:
            #draws a simple line
            draw.line(tempdraw,self.col,(self.sx,self.sy),(mx,my))
    def scroll(self,screen,forward=True):
        if forward:
            #makes line size smaller and limits it at 1
            if self.size > 0:
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
        else:
            screen.blit(tempdraw,(0,0)) #blits temporary drawing board
            tempdraw.fill((255,255,255,0)) #clears temporary drawing board
    def mouseup(self,screen):
        #same but checks if mouse is held first
        mb = mouse.get_pressed()
        if not mb[0] and not mb[2]:
            super(Line,self).mouseup(screen) #calls super mouseup
    def drawsprite(self,screen):
        global lcol
        global rcol
        mb = mouse.get_pressed()
        mx,my = mouse.get_pos()
        tempdraw2 = Surface((self.size*2,self.size*2),SRCALPHA) #small drawing board for the transparent sprite
        if self.size > 0:
            if mb[2]:
                draw.circle(tempdraw2,self.col,(self.size,self.size),self.size)
            else:
                draw.circle(tempdraw2,lcol,(self.size,self.size),self.size)
        else:
            if mb[2]:
                screen.set_at((mx,my),self.col)
            else:
                screen.set_at((mx,my),lcol)
        screen.blit(tempdraw2,(mx-self.size,my-self.size))
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
        lcol = Color(lcol[0],lcol[1],lcol[2],int(alpha/100*255))#sets transparency
    def rclick(self,screen):
        global rcol
        mx,my = mouse.get_pos()
        rcol = screen.get_at((mx,my))
        rcol = Color(rcol[0],rcol[1],rcol[2],int(alpha/100*255))#sets transparency
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
        self.dx = 0 #distance of mouse from corner of textbox - used for moving textbox on click
        self.dy = 0
    def lclick(self,screen):
        global lcol
        mx,my = mouse.get_pos()
        if self.hastextbox:
            if self.textbox.get_rect().collidepoint(mx,my-5) or self.textbox.get_rect().collidepoint(mx,my+20):
                #sets dx and dy and let's continue move the textbox
                self.dx,self.dy = mx-self.textbox.x,my-self.textbox.y
            else:
                #turns off text box if we have one and user did not click textbox
                self.hastextbox = False
                currtool.textbox.drawtext(screen)
                self.dx,self.dy = 0,0
        else:
            #draws a text box if we don't have one
            decor = (("bold",self.textbox.tbfont.get_bold()),("italic",self.textbox.tbfont.get_italic()),("underline",self.textbox.tbfont.get_underline())) #tuple of text decor
            self.textbox = Textbox(mx,my,20,20,self.textbox.fontfamily,self.textbox.fontsize,lcol)
            for t,d in decor:
                if d:
                    exec("self.textbox.tbfont.set_"+t+"(True)")
            self.hastextbox = True
    def rclick(self,screen):
        #literally the same thing as lclick, but with rcol instead of lcol
        global rcol
        mx,my = mouse.get_pos()
        if self.hastextbox:
            if self.textbox.get_rect().collidepoint(mx,my-5) or self.textbox.get_rect().collidepoint(mx,my+20):
                #sets dx and dy and let's continue move the textbox
                self.dx,self.dy = mx-self.textbox.x,my-self.textbox.y
            else:
                #turns off text box if we have one and user did not click textbox
                self.hastextbox = False
                currtool.textbox.drawtext(screen)
                self.dx,self.dy = 0,0
        else:
            #draws a text box if we don't have one
            decor = (("bold",self.textbox.tbfont.get_bold()),("italic",self.textbox.tbfont.get_italic()),("underline",self.textbox.tbfont.get_underline())) #tuple of text decor
            self.textbox = Textbox(mx,my,20,20,self.textbox.fontfamily,self.textbox.fontsize,rcol)
            for t,d in decor:
                if d:
                    exec("self.textbox.tbfont.set_"+t+"(True)")
            self.hastextbox = True
    def cont(self,screen):
        #drags the textbox if the mouse is down on canvas
        mb = mouse.get_pressed()
        if mb[0] or mb[2]:
            self.textbox.x = mx-self.dx
            self.textbox.y = my-self.dy
    def scroll(self,screen,forward=True):
        if forward:
            #makes text smaller
            self.fontsize -= 1
            self.fontsize = max(self.fontsize,5) #makes sure fontsize isn't less than 5
        else:
            #makes text bigger
            self.fontsize += 1
            self.fontsize = min(self.fontsize,99) #makes sure fontsize isn't greater than 99
        self.textbox.changefont(self.fontfamily,self.fontsize)
        self.textbox.width = max([self.textbox.tbfont.render(self.textbox.text[i],True,BLACK).get_width() for i in range(self.textbox.lines)]) #sets width to be maximum of the lines
        self.textbox.height = self.textbox.tbfont.render(self.textbox.text[-1],True,BLACK).get_height()*self.textbox.lines #sets height
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
            elif kp[K_UP]:
                #moves insertion point up
                if self.textbox.irow > 0:
                    self.textbox.irow -= 1
                    self.textbox.icol = min(self.textbox.icol,len(self.textbox.text[self.textbox.irow])) #makes sure column is not greater than number in the row
            elif kp[K_DOWN]:
                #moves insertion point down
                if self.textbox.irow < self.textbox.lines-1:
                    self.textbox.irow += 1
                    self.textbox.icol = min(self.textbox.icol,len(self.textbox.text[self.textbox.irow])) #makes sure column is not greater than number in the row
            elif kp[K_LEFT]:
                #moves insertion point left
                if self.textbox.icol > 0:
                    self.textbox.icol -= 1
                elif self.textbox.irow > 0:
                    self.textbox.irow -= 1 #moves the insertion point to the end of the above line if they move left of current line
                    self.textbox.icol = len(self.textbox.text[self.textbox.irow])
            elif kp[K_RIGHT]:
                #moves insertion point right
                if self.textbox.icol < len(self.textbox.text[self.textbox.irow]):
                    self.textbox.icol += 1
                elif self.textbox.irow < self.textbox.lines-1:
                    self.textbox.irow += 1 #moves the insertion point to the beginning of the below line if they move right of current line
                    self.textbox.icol = 0
            elif kp[K_HOME]:
                #moves insertion point to beginning of row
                self.textbox.icol = 0
            elif kp[K_END]:
                #moves insertion point to end of row
                self.textbox.icol = len(self.textbox.text[self.textbox.irow])
            else:
                if kp[K_BACKSPACE]:
                    self.textbox.backspace()
                elif kp[K_DELETE]:
                    self.textbox.delete()
                elif 1 in kp:
                    self.textbox.writeto(keypressed) #writes keypressed to texbox
    def outside(self):
        #turns off text box if user clicks outside canvas and if user didn't click font change or color change
        global screen
        global lcol
        global rcol
        if self.hastextbox and lastclick not in ["fontdropdown","fontsize","palbutton","palette","mousebutton","canvas","gradsel","fontdecor"]:
            self.hastextbox = False
            currtool.textbox.drawtext(screen)
        else:
            #changes dimensions and updates font
            mb = mouse.get_pressed()
            if lastclick in ["palbutton","palette","mousebutton","gradsel"]:
                #changes color
                if mb[0]:
                    col = lcol
                else:
                    col = rcol
            else:
                col = None
            self.textbox.changefont(self.fontfamily,self.fontsize,col)
            self.textbox.width = max([self.textbox.tbfont.render(self.textbox.text[i],True,BLACK).get_width() for i in range(self.textbox.lines)]) #sets width to be maximum of the lines
            self.textbox.height = self.textbox.tbfont.render(self.textbox.text[-1],True,BLACK).get_height()*self.textbox.lines #sets height
    def drawsprite(self,screen):
        mx,my = mouse.get_pos()     
        screen.blit(self.icon,(mx-20,my-10))
#-------------------------------------------Select Tool
class Select(Tool):
    #selects an area and makes it moveable
    def __init__(self):
        self.icon = crosscursor
        self.hasmenu = False #has the tool a menu set?
        self.selectedbox = Surface((1,1)) #selected box by shape
        self.x,self.y,self.width,self.height = 0,0,0,0 #dimensions and co-ords of selected box
        self.menux,self.menuy = 0,0 #menu position
        self.menu = [Button("save",timesnr.render("Save selected area as...",True,BLACK),self.menux,self.menuy,"",200,20,
                            transform.smoothscale(self.selectedbox,(self.width,self.height))),
                    Button("copy",timesnr.render("Copy (Ctrl-C)",True,BLACK),self.menux,self.menuy+20,"",200,20,
                            transform.smoothscale(self.selectedbox,(self.width,self.height))),
                    Button("cut",timesnr.render("Cut (Ctrl-X)",True,BLACK),self.menux,self.menuy+40,"",200,20,
                            transform.smoothscale(self.selectedbox,(self.width,self.height))),
                    Button("delete",timesnr.render("Delete (del)",True,BLACK),self.menux,self.menuy+60,"",200,20),
                    Button("flip",timesnr.render("Flip horizontally",True,BLACK),self.menux,self.menuy+80,"",200,20,(True,False)),
                    Button("flip",timesnr.render("Flip vertically",True,BLACK),self.menux,self.menuy+100,"",200,20,(False,True)),
                    Button("rotate",timesnr.render("Rotate 90° clockwise",True,BLACK),self.menux,self.menuy+120,"",200,20,-90),
                    Button("rotate",timesnr.render("Rotate 90° counter-clockwise",True,BLACK),self.menux,self.menuy+140,"",200,20,90),
                    Button("pixelate",timesnr.render("Pixelate selected area",True,BLACK),self.menux,self.menuy+160,"",200,20,
                            transform.smoothscale(self.selectedbox,(self.width,self.height))),
                    Button("greyscale",timesnr.render("Greyscale filter",True,BLACK),self.menux,self.menuy+180,"",200,20,
                            transform.smoothscale(self.selectedbox,(self.width,self.height))),
                    Button("settranscol",timesnr.render("Set transparent color",True,BLACK),self.menux,self.menuy+200,"",200,20),
                    Button("yanderetint",chiller.render("YANDERE TINT",True,BLOODRED),self.menux,self.menuy+220,"",200,20,
                            transform.smoothscale(self.selectedbox,(self.width,self.height)))] #menu
        self.settranscol = False
        self.menurect = Rect(0,0,200,len(self.menu)*20) #menu rect
        self.fromshape = False #did the selectool come as a result of a shape?
        self.pressedsave = False #did user press save?
        self.hasbox = False #has the tool a selected box set?
        self.forming = False #is the box being formed?
        self.dx,self.dy = 0,0 #difference in x and y between mouse and corner of selectedbox
        self.clicked = 0 #which button clicked? 0 means left mouse, 1 means right mouse
        self.op = 0 #option of size change the user tried (this is determined by where user clicks; each option affects different parts of the box, like either x or width, y or height, etc.)
        #0 = No change; 1: change x and y; 2: change width and y; 3: change x and height; 4: change width and height;
        #5 = change y; 6 = change height; 7 = change x; 8 = change width
    def lclick(self,screen):
        global cfiller
        global canvas
        global currtool
        mx,my = mouse.get_pos()
        if self.settranscol:
            #if we are setting transparent color, we do that
            if Rect(self.x,self.y,self.width,self.height).collidepoint(mx,my):
                #if user presses select box we set transparent color
                boxX,boxY = mx-self.x,my-self.y #sets co-ords of mouse relative to selected box
                try:
                    scaledbox = transform.smoothscale(self.selectedbox,(self.width,self.height)) #creates scaled version of selected box
                except:
                    scaledbox = transform.scale(self.selectedbox,(self.width,self.height))
                self.selectedbox.set_colorkey(scaledbox.get_at((boxX,boxY))) #sets transparent colorkey
            self.settranscol = False #turns off boolean
            return 0
        self.clicked = 0
        if self.hasmenu:
            self.clicked = 1 #if there exists a menu, we treat it as a right click - this is so the box doesn't move when cancelling a menu item
            #if a menu exists we handle it
            if not self.menurect.collidepoint(mx,my):
                self.hasmenu = False #if user did not click the menu it is removed
            else:
                #if user clicks the menu (not first button since that is special and needs to be pressed on mouse up) we handle the clicking
                if self.menu[0].istouch():
                        self.pressedsave = True #sets pressedsave boolean to true if user pressed save button
                else:
                    for b in self.menu[1:]:
                        if b.istouch():
                            b.clickon(screen) #clicks on button
                            break
        elif self.hasbox:
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
                #we draw the box and turn the hasbox boolean to False so that we stop drawing the box
                try:
                    self.selectedbox = transform.smoothscale(self.selectedbox,(abs(self.width),abs(self.height)))#resizes image
                except:
                    self.selectedbox = transform.scale(self.selectedbox,(abs(self.width),abs(self.height)))#resizes image
                self.hasbox = False
                screen.blit(self.selectedbox,(self.x,self.y)) #blits the selected box permanently
                if self.fromshape:
                    currtool = shapetool #sets currtool to shapetool if it's from shape
                    self.fromshape = False
            else:
                #if user did not try to change size we move the box
                self.dx = mx-self.x
                self.dy = my-self.y #sets difference between corner and mouse co-ord
        else:
            cfiller = screen.copy().subsurface(canvas) #makes cfiller canvas before the click
            self.x = mx
            self.y = my
            self.forming = True
    def rclick(self,screen):
        global cfiller
        global canvas
        global currtool
        mx,my = mouse.get_pos()
        if self.settranscol:
            #if we are setting transparent color we turn off the boolean on right click
            self.settranscol = False
            return 0
        self.clicked = 1
        if self.hasbox:
            if Rect(self.x,self.y,self.width,self.height).collidepoint(mx,my) and not self.hasmenu:
                #if there exists no menu we create one
                self.menux,self.menuy = mx,my
                self.menurect = Rect(self.menux,self.menuy,200,len(self.menu)*20)
                self.hasmenu = True
                if self.menuy+len(self.menu)*20 > screen.get_height():
                    #if the menu goes off the canvas, we move menuy up
                    self.menuy -= (self.menuy+len(self.menu)*20)-screen.get_height()
                self.menu = [Button("save",timesnr.render("Save selected area as...",True,BLACK),self.menux,self.menuy,"",200,20,
                            transform.smoothscale(self.selectedbox,(self.width,self.height))),
                    Button("copy",timesnr.render("Copy (Ctrl-C)",True,BLACK),self.menux,self.menuy+20,"",200,20,
                            transform.smoothscale(self.selectedbox,(self.width,self.height))),
                    Button("cut",timesnr.render("Cut (Ctrl-X)",True,BLACK),self.menux,self.menuy+40,"",200,20,
                            transform.smoothscale(self.selectedbox,(self.width,self.height))),
                    Button("delete",timesnr.render("Delete (del)",True,BLACK),self.menux,self.menuy+60,"",200,20),
                    Button("flip",timesnr.render("Flip horizontally",True,BLACK),self.menux,self.menuy+80,"",200,20,(True,False)),
                    Button("flip",timesnr.render("Flip vertically",True,BLACK),self.menux,self.menuy+100,"",200,20,(False,True)),
                    Button("rotate",timesnr.render("Rotate 90° clockwise",True,BLACK),self.menux,self.menuy+120,"",200,20,-90),
                    Button("rotate",timesnr.render("Rotate 90° counter-clockwise",True,BLACK),self.menux,self.menuy+140,"",200,20,90),
                    Button("pixelate",timesnr.render("Pixelate selected area",True,BLACK),self.menux,self.menuy+160,"",200,20,
                            transform.smoothscale(self.selectedbox,(self.width,self.height))),
                    Button("greyscale",timesnr.render("Greyscale filter",True,BLACK),self.menux,self.menuy+180,"",200,20,
                            transform.smoothscale(self.selectedbox,(self.width,self.height))),
                    Button("settranscol",timesnr.render("Set transparent color",True,BLACK),self.menux,self.menuy+200,"",200,20),
                    Button("yanderetint",chiller.render("YANDERE TINT",True,BLOODRED),self.menux,self.menuy+220,"",200,20,
                           transform.smoothscale(self.selectedbox,(self.width,self.height)))] #re-defines menu to move it
            elif self.hasmenu:
                if not self.menurect.collidepoint(mx,my):
                    self.hasmenu = False #if user did not click the menu it is removed
                else:
                    #if user clicks the menu (not first button since that is special and needs to be pressed on mouse up) we handle the clicking
                    if self.menu[0].istouch():
                        self.pressedsave = True #sets pressedsave boolean to true if user pressed save button
                    else:
                        for b in self.menu[1:]:
                            if b.istouch():
                                b.clickon(screen) #clicks on button
                                break
            else:
                if not Rect(self.x,self.y,self.width,self.height).collidepoint(mx,my):
                    #if the use clicks outside of the box and no menu is open we remove the box
                    try:
                        self.selectedbox = transform.smoothscale(self.selectedbox,(abs(self.width),abs(self.height)))#resizes image
                    except:
                        self.selectedbox = transform.scale(self.selectedbox,(abs(self.width),abs(self.height)))#resizes image
                    self.hasbox = False
                    screen.blit(self.selectedbox,(self.x,self.y)) #blits the selected box permanently
                    if self.fromshape:
                        currtool = shapetool #sets currtool to shapetool if it's from shape
                        self.fromshape = False
        else:
            #if there exists no box, we make one
            cfiller = screen.copy().subsurface(canvas) #makes cfiller canvas before the click
            self.x = mx
            self.y = my
            self.forming = True
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
        elif self.hasmenu:
            #if there exists a menu we check if we moused up over the first button (the save button, since it opens a new window we need to open it on mouseup not mousedown
            #otherwise it will close the window on mouse up after mouse down)
            if self.menu[0].istouch() and self.pressedsave:
                self.menu[0].clickon(screen)
                self.pressedsave = False
    def cont(self,screen):
        global cfiller
        mx,my = mouse.get_pos()
        if self.hasbox and not self.clicked:
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
        global currtool
        mx,my = mouse.get_pos()
        if self.hasbox and lastclick != "canvas":
            if self.hasmenu and self.menurect.collidepoint(mx,my):
                #if user clicks the menu we handle the clicking
                for b in self.menu:
                    if b.istouch():
                        b.clickon(screen) #clicks on button
                        break
                return 0 #returns 0 to discontinue
            #if the last click was not the canvas we turn off the tool
            try:
                self.selectedbox = transform.smoothscale(self.selectedbox,(abs(self.width),abs(self.height)))#resizes image
            except:
                self.selectedbox = transform.scale(self.selectedbox,(abs(self.width),abs(self.height)))#resizes image
            self.hasbox = False
            screen.blit(self.selectedbox,(self.x,self.y))
            if self.fromshape:
                currtool = shapetool #sets currtool to shapetool if it's from shape
                self.fromshape = False
        self.settranscol = False #turns off set transparent color
        self.hasmenu = False #turns off menu
    def keypress(self,screen,keypressed):
        #handles key methods for a box
        global boxcp
        global currtool
        kp = key.get_pressed()
        if kp[K_DELETE]:
            #deletes box
            self.hasbox = False
            if self.fromshape:
                self.fromshape = False
                currtool = shapetool #changes tool to shape if the selectool was from shape
        elif kp[K_c] and (kp[K_RCTRL] or kp[K_LCTRL]) and self.hasbox:
            #copies box onto clipboard
            boxcp = (transform.smoothscale(self.selectedbox,(self.width,self.height)),(self.x,self.y)) #sets the clipboard's image and coordinates
        elif kp[K_x] and (kp[K_RCTRL] or kp[K_LCTRL]) and self.hasbox:
            #cuts box onto clipboard
            self.hasbox = False
            self.hasmenu = False
            boxcp = (transform.smoothscale(self.selectedbox,(self.width,self.height)),(self.x,self.y)) #sets the clipboard's image and coordinates
    def drawsprite(self,screen):
        mx,my = mouse.get_pos()
        if self.settranscol:
            #if we are setting transparent color, we draw a magic wand instead
            screen.blit(magicwand,(mx,my))
            return 0
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
        self.size = 10
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
        lx = (mx-self.sx)*(0.8*self.size)/dist
        ly = (my-self.sy)*(0.8*self.size)/dist
        for i in range(max(1,int(dist)//int(self.size*0.8))):
            for j in range(int(self.size**1.5)):
                #randang = randint(0,359) #random angle
                #randhy = randint(0,self.size) #random hypotenuse
                randw = randint(-self.size,self.size) #random width and height
                randh = randint(-self.size,self.size)
                if hypot(randw,randh) <= self.size:
                    tempdraw.set_at((int(self.sx+lx*i+randw),int(self.sy+ly*i+randh)),self.col) #random spray
        self.sx,self.sy = mx,my
    def scroll(self,screen,forward=True):
        if forward:
            #makes size smaller
            self.size -= 1
            self.size = max(2,self.size) #limits size at 2
        else:
            #makes size bigger
            self.size += 1
            self.size = min(512,self.size) #limits size at 512
    def outside(self):
        #continues drawing if the last click was canvas - it won't draw outside of canvas because of clipping before calling this method
        global lastclick
        if lastclick == "canvas":
            self.cont(screen)
        else:
            screen.blit(tempdraw,(0,0)) #blits tempdraw
            tempdraw.fill((255,255,255,0)) #clears tempdraw
    def keypress(self,screen,keypressed=""):
        if keypressed == " ":
            self.size = 10 #resets size if space is pressed
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
        self.forming = False #forming a rect or an ellipse?
        self.sx,self.sy = 0,0 #starting co-ords of shape, starts at 0,0 (doesn't rly matter since we change it on click)
        self.points = [] #points of polygon (for polygon option)
    def lclick(self,screen,fromright=False):
        global cfiller
        global canvas
        global lcol
        global rcol
        mx,my = mouse.get_pos()
        #----Polygon----#
        if self.shape == "polygon":
            if len(self.points) == 0:
                self.col = rcol if mouse.get_pressed()[2] else lcol #sets color if there are no current points (first press)
            self.points.append((mx,my)) #adds point to points
            if self.width > 1:
                draw.circle(tempdraw,self.col,(mx,my),self.width//2) #draws a circle of the same width as the border
            screen.set_at((mx,my),self.col) #sets point to color currently at
            if len(self.points) > 1:
                #line algorithm if the width is greater than 1
                if self.width > 1:
                    x1,y1 = self.points[-2]
                    x2,y2 = self.points[-1]
                    dist = max(1,hypot(x2-x1,y2-y1))#distance between points
                    lx = (x2-x1)/dist #little x to increment circles by
                    ly = (y2-y1)/dist #little y to increment circles by
                    for i in range(int(dist)):
                        draw.circle(tempdraw,self.col,(int(x1+lx*i),int(y1+ly*i)),self.width//2)
                else:
                    #simply draws a line if width is less than 2
                    draw.line(tempdraw,self.col,self.points[-2],self.points[-1])
            return 0 #returns so that it does not run following code
        #----Other shapes----#
        mb = mouse.get_pressed()
        if mb[2] and lastclick == "canvas" and not fromright:
            #if user was already right clicking, we do nothing
            return 0
        self.forming = True
        self.sx,self.sy = mx,my #sets starting co-ords to mouse pos
        self.col = lcol #sets color to left click color
    def rclick(self,screen):
        #----Polygon----#
        if self.shape == "polygon":
            if len(self.points) == 0:
                self.lclick(screen) #calls left click method
                return 0 #stops the function if there's nothing in points
            if len(self.points) <= 2:
                self.points = [] #resets points if length of points is <=2 as we cannot make a polygon from 2 or less points
                return 0
            draw.polygon(tempdraw,self.col,self.points,self.width) #draws the polygon
            self.points = [] #clears points
            return 0
        #----Other shapes----#
        mb = mouse.get_pressed()
        if mb[0] and lastclick == "canvas":
            #if user was already left clicking, we do nothing
            return 0
        self.lclick(screen,True) #identical to lclick
        self.col = rcol #sets color to rclick color
    def scroll(self,screen,forward=True):
        global canvas
        if forward:
            #makes shape border smaller
            self.width -= 1
            self.width = max(0,self.width) #makes sure width is at least 0
        else:
            #makes shape border bigger
            self.width += 1
            self.width = min(99,self.width) #makes sure width does not exceed 99
        if self.shape == "polygon" and len(self.points) > 0:
            tempdraw.fill((255,255,255,0))
            #if length of points is greater than 0 and we have a polygon shape active, we draw all the points again with the new size
            if len(self.points) == 1:
                #if there is only one point we just draw a new circle/dot on the point
                if self.width < 2:
                    screen.set_at(self.points[0],self.col)
                else:
                    draw.circle(tempdraw,self.col,self.points[0],self.width//2)
            else:
                for i in range(1,len(self.points)):
                    #line algorithm if the width is greater than 1
                    if self.width > 1:
                        x1,y1 = self.points[i-1]
                        x2,y2 = self.points[i]
                        dist = max(1,hypot(x2-x1,y2-y1))#distance between points
                        lx = (x2-x1)/dist #little x to increment circles by
                        ly = (y2-y1)/dist #little y to increment circles by
                        for i in range(int(dist)):
                            draw.circle(tempdraw,self.col,(int(x1+lx*i),int(y1+ly*i)),self.width//2)
                    else:
                        draw.line(tempdraw,self.col,self.points[i-1],self.points[i])
    def cont(self,screen):
        global cfiller
        if self.shape == "polygon" or not self.forming:
            return 0 #does nothing if shape is a polygon or if it is not forming
        mx,my = mouse.get_pos()
        framerect = Rect(self.sx,self.sy,mx-self.sx,my-self.sy) #rect for frame of ellipse/rectangle
        framerect.normalize()
        tempdraw.fill((255,255,255,0)) #clears tempdraw
        if self.shape == "rect":
            draw.rect(tempdraw,self.col,framerect)
            if self.width > 0 and abs(self.sy-my)-self.width*2 > 0 and abs(self.sx-mx)-self.width*2 > 0:
                draw.rect(tempdraw,(255,255,255,0),(framerect[0]+self.width,framerect[1]+self.width,framerect[2]-2*self.width,framerect[3]-2*self.width))
        elif self.shape == "ellipse":
            sx = min(self.sx,mx) #sx becomes smaller of startx and mouse-x
            sy = min(self.sy,my) #same idea as sx
            ellipseSurface = Surface((abs(self.sx-mx),abs(self.sy-my)),SRCALPHA) #surface that will contain the ellipse
            draw.ellipse(ellipseSurface,self.col,Rect(0,0,framerect[2],framerect[3])) #draws ellipse
            if self.width != 0 and abs(self.sy-my)-self.width*2 > 0 and abs(self.sx-mx)-self.width*2 > 0:
                #if the width and height of the centre ellipse is greater than 0 and the ellipse has a border, draws transparent ellipse in the centre to simulate an ellipse with a border
                draw.ellipse(ellipseSurface,(255,255,255,0),(self.width,self.width,framerect[2]-self.width*2,framerect[3]-self.width*2))
            tempdraw.blit(ellipseSurface,(framerect[0],framerect[1])) #blits the ellipse surface
    def mouseup(self,screen):
        global currtool
        mb = mouse.get_pressed()
        if self.shape in ["rect","ellipse"] and self.forming:
            #turns to tool into selectool with shape in selected box
            cfiller = screen.copy().subsurface(canvas)
            currtool = selectool
            selectool.fromshape = True #sets selectool to be from shape so that it reverts to shape tool when done
            framerect = Rect(self.sx,self.sy,mx-self.sx,my-self.sy) #rect for frame of ellipse/rectangle
            framerect.normalize()
            selectool.selectedbox = tempdraw.subsurface(framerect).copy()
            selectool.x,selectool.y,selectool.width,selectool.height = framerect
            selectool.hasbox = True
            tempdraw.fill((255,255,255,0)) #clears tempdraw
            screen.blit(toolboxfiller,(20,90)) #clears shapetool's drop down box
            cfiller = screen.copy().subsurface(canvas)
            self.forming = False
        elif len(self.points) == 0:
            screen.blit(tempdraw,(0,0))
            tempdraw.fill((255,255,255,0)) #clears tempdraw
    def keypress(self,screen,keypressed=""):
        if keypressed == " ":
            self.width = 0 #resets width when space is clicked
    def outside(self):
        mb = mouse.get_pressed()
        if self.shape == "polygon" and len(self.points) > 0:
            self.points = [] #deletes points in polygon
        if lastclick == "canvas":
            self.cont(screen)
        else:
            if self.shape in ["rect","ellipse"] and self.forming:
                cfiller = screen.copy().subsurface(canvas)
                currtool = selectool
                selectool.fromshape = True #sets selectool to be from shape so that it reverts to shape tool when done
                framerect = Rect(self.sx,self.sy,mx-self.sx,my-self.sy) #rect for frame of ellipse/rectangle
                framerect.normalize()
                selectool.selectedbox = tempdraw.subsurface(framerect).copy()
                selectool.x,selectool.y,selectool.width,selectool.height = framerect
                selectool.hasbox = True
                tempdraw.fill((255,255,255,0)) #clears tempdraw
                screen.blit(toolboxfiller,(20,90)) #clears shapetool's drop down box
                self.forming = False
            if self.shape == "polygon":
                screen.blit(tempdraw,(0,0))
            tempdraw.fill((255,255,255,0)) #clears tempdraw
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
        if self.fcol[:3] == self.ccol[:3]:
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
        if self.fcol[:3] == self.ccol[:3]:
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
#-------------------------------------------Blur
class Blur(Tool):
    #blurs an area within a circle
    def __init__(self):
        self.icon = bluricon
    def cont(self,screen):
        #blurs while mouse is held
        for x in range(mx-10,mx+11):
            for y in range(my-10,my+11):
                if hypot(mx-x,my-y) <= 10 and canvas.collidepoint(x,y):
                    r,g,b,a = screen.get_at((x,y)) #finds color at a location
                    rs,gs,bs = [],[],[] #lists to hold all the neighbouring pixels color for r,g,b
                    for dx,dy in [(-1,0),(0,-1),(1,0),(0,1)]:
                        if canvas.collidepoint(x+dx,y+dy):
                            ri,gi,bi,a = screen.get_at((x+dx,y+dy)) #gets pixel's color in all four directions
                            rs.append(ri)
                            gs.append(gi)
                            bs.append(bi)
                    r2 = (r+sum(rs))//(len(rs)+1)
                    g2 = (g+sum(gs))//(len(rs)+1)
                    b2 = (b+sum(bs))//(len(rs)+1) #averages out r,g,b and sets pixel to that color
                    screen.set_at((x,y),(r2,g2,b2))
    def drawsprite(self,screen):
        mx,my = mouse.get_pos()
        screen.blit(self.icon,(mx-20,my-35))
        draw.circle(screen,BLACK,(mx,my),10,1)
        screen.blit(crosscursor,(mx-21,my-20))
#-------------------------------------------Pixelate
class Pixelate(Tool):
    #pixelates an area (within a circle is WIP)
    def __init__(self):
        self.icon = pixelateicon
    def cont(self,screen):
        #pixelates while mouse is held
        for x in range(mx-10,mx+10,5):
            for y in range(my-10,my+10,5):
                if canvas.collidepoint(x,y) and canvas.collidepoint(x+5,y+5):
                    #makes sure canvas touches opposite corners of square
                    #if it's within canvas we create a pixel
                    avgcolor = transform.average_color(screen.subsurface(Rect(x,y,5,5))) #gets average color
                    draw.rect(screen,avgcolor,(x,y,5,5)) #draws pixel
    def drawsprite(self,screen):
        mx,my = mouse.get_pos()
        screen.blit(self.icon,(mx-20,my-35))
        draw.rect(screen,BLACK,(mx-10,my-10,20,20),1)
        screen.blit(crosscursor,(mx-21,my-20))
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
        if self.istouch():
            dispcol = RED
        else:
            dispcol = WHITE
        draw.rect(screen,dispcol,(self.x,self.y,self.width,self.height))
        if type(self.pic) == Surface:
            screen.blit(self.pic,[self.x,self.y])
        elif type(self.pic) == Rect:
                draw.rect(screen,self.arg2,Rect(self.x,self.y,self.width,self.height))
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
        global textool,currtool,lcol,rcol,shapetool,custompalbuttons,cfiller,undo_mem,redo_mem,boxcp,alpha,stampage,tools
        if issubclass(type(self.func),Tool):
            #tool change button
            currtool = self.func
        elif self.func == "font":
            #font family change button
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
        elif self.func == "textdec":
            #text decorator button
            exec("textool.textbox.tbfont.set_"+self.arg2+"(not textool.textbox.tbfont.get_"+self.arg2+"())") #sets textool's decor to be opposite what it is
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
            elif self.arg2 == "polygon":
                tools[8].pic = polygonsprite 
                shapetool.icon = polygonsprite
            tools[8].toolbit = "Shape tool ("+str(self.arg2.title())+"): "+str(self.toolbit)
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
                lcol = Color(lcol[0],lcol[1],lcol[2],int(alpha/100*255))#sets transparency
            elif mb[2]:
                rcol = self.arg2
                rcol = Color(rcol[0],rcol[1],rcol[2],int(alpha/100*255))#sets transparency
        elif self.func == "addcustom":
            #add custom color button
            #adds color button to custompalbuttons
            length = len(custompalbuttons) #length of custom palette buttons list
            custompalbuttons.append(Button("color",Rect(170+length*20,506,20,20),170+length*20,506,"",20,20,self.arg2))
            if len(custompalbuttons) > 4:
                del custompalbuttons[0] #removes first item of custompalbuttons to keep it below 4
                #following loop reduces x co-ords of all previous buttons
                for b in custompalbuttons:
                    b.x -= 20
        elif self.func == "alpha":
            #alpha% scale button
            alpha += self.arg2 #changes alpha value of colors
            alpha = min(max(0,alpha),100) #limits alpha% to be from 0 - 100
            lcol = Color(lcol[0],lcol[1],lcol[2],int((alpha/100)*255)) #sets lcol and rcol
            rcol = Color(rcol[0],rcol[1],rcol[2],int((alpha/100)*255))
        elif self.func == "save":
            #save function
            mouse.set_visible(True)
            savename = filedialog.asksaveasfilename(defaultextension=".jpg")
            if savename:
                if type(currtool) == Select:
                    currtool.hasbox = False
                elif type(currtool) == Text:
                    currtool.hastextbox = False
                if self.arg2 == None:
                    #if we are not copying a selected surface, we copy the canvas
                    image.save(screen.copy().subsurface(canvas), savename)
                else:
                    #saves selected surface
                    if savename[-4:] == ".png":
                        try:
                            self.arg2 = self.arg2.convert_alpha() #converts surface into one with SRCALPHA to support alpha
                        except:
                            pass
                    image.save(self.arg2, savename)
            if self.arg2 != None:
                screen.blit(self.arg2,(selectool.x,selectool.y)) #blits the image to the screen, as we know the select tool is the only one who can call this
                selectool.hasmenu = False
            mouse.set_visible(False)
        elif self.func == "open":
            #open function
            if type(currtool) == Select:
                currtool.hasbox = False
            elif type(currtool) == Text:
                currtool.hastextbox = False
            loadname = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.bmp;*.jpg;*.jpeg;*.gif")])
            mouse.set_visible(True)
            if loadname:
                if len(undo_mem) >= 256:
                    del undo_mem[0] #removes the last thing undo_memorized if we're over the limit
                redo_mem = []
                undo_mem.append(screen.copy().subsurface(canvas))
                if not rclick:
                    draw.rect(screen,WHITE,canvas) #clears everything previously on the canvas if user does not hold shift
                cfiller = screen.copy().subsurface(canvas)
                opened_image = image.load(loadname)
                img_ratio = opened_image.get_width()/opened_image.get_height()
                if opened_image.get_width() >= opened_image.get_height():
                    width = (min(opened_image.get_width(),canvas[2]))
                    height = (int(width/img_ratio))
                else:
                    height = (min(opened_image.get_height(),canvas[3]))
                    width = (int(height*img_ratio))
                currtool = selectool #changes current tool to select tool
                currtool.hasbox = True
                currtool.selectedbox = transform.scale(opened_image,(width,height)) #makes opened image the box's image
                currtool.x,currtool.y,currtool.width,currtool.height = 300,50,width,height #creating a select box around uploaded image
            mouse.set_visible(False)
        elif self.func == "undo":
            #undo button
            if len(undo_mem) > 0:
                redo_mem.append(screen.copy().subsurface(canvas)) #appends the current screen to redo list
                prevsave = undo_mem.pop(-1) #prevsave = last screen save
                screen.blit(prevsave,(canvas[0],canvas[1])) #fills the screen with new save
        elif self.func == "redo":
            #redo button
            if len(redo_mem) > 0:
                if len(undo_mem) >= 256:
                    del undo_mem[0] #removes the last thing undo_memorized if we're over the limit
                undo_mem.append(screen.copy().subsurface(canvas)) #appends current screen to undo list
                prevsave = redo_mem.pop(-1) #gets new screen from redo list
                screen.blit(prevsave,(canvas[0],canvas[1]))
        elif self.func == "clear":
            #clear button
            if len(undo_mem) >= 256:
                del undo_mem[0]
            undo_mem.append(screen.copy().subsurface(canvas))
            redo_mem = [] #adds to undo list undo_memory and deletes all of redo list undo_memory
            draw.rect(screen,WHITE,canvas) #fills canvas white
            tempdraw.fill((255,255,255,0)) #clears tempdraw
        elif self.func in ["copy","cut"]:
            #copy/cut button
            if self.func == "cut":
                selectool.hasbox = False #turns off box in selectool
            selectool.hasmenu = False #turns off menu
            boxcp = (self.arg2,(canvas[0],canvas[1])) #sets clipboard to copied object
        elif self.func == "paste":
            #paste button
            if boxcp != None:
                if None not in boxcp:
                    if len(undo_mem) >= 256:
                            del undo_mem[0] #removes the last thing undo_memorized if we're over the limit
                    undo_mem.append(screen.copy().subsurface(canvas)) #appends current screen to undo list
                    redo_mem = []
                    screen.set_clip(canvas)
                    if selectool.hasbox:
                        screen.blit(selectool.selectedbox,(selectool.x,selectool.y))
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
        elif self.func == "delete":
            #delete button
            #deletes selectool's box
            selectool.hasbox = False #turns off box in selectool
            selectool.hasmenu = False #turns off menu
        elif self.func == "flip":
            #flip button
            if currtool == selectool:
                #selected box flip button
                selectool.selectedbox = transform.flip(selectool.selectedbox,self.arg2[0],self.arg2[1]) #flips selectool's selected box based on what user wants
                selectool.hasmenu = False #turns off menu
            elif type(currtool) == Stamp:
                #stamp flipping
                currtool.img = transform.flip(currtool.img,self.arg2[0],self.arg2[1]) #flips images of stamp
                currtool.img2 = transform.flip(currtool.img2,self.arg2[0],self.arg2[1])
            try:
                currtool.icon = transform.smoothscale(currtool.img,(currtool.width,currtool.height)) #sets icon to have same size as new image
            except:
                currtool.icon = transform.scale(currtool.img,(currtool.width,currtool.height)) #sets icon to have same size as new image  
        elif self.func == "rotate":
            #rotate selected box button
            if currtool == selectool:
                selectool.selectedbox = transform.rotate(selectool.selectedbox,self.arg2) #rotates selectool's selected box based on what user wants
                selectool.width,selectool.height = selectool.height,selectool.width #switches the height and width
                selectool.hasmenu = False #turns off menu
            elif type(currtool) == Stamp:
                #stamp rotation
                currtool.img = transform.rotate(currtool.img,self.arg2) #rotates stamp's images
                currtool.owidth,currtool.oheight,currtool.width,currtool.height = currtool.oheight,currtool.owidth,currtool.height,currtool.width #flips dimensions of stamp                
                currtool.img2 = transform.rotate(currtool.img2,self.arg2)
                currtool.owidth2,currtool.oheight2,currtool.width2,currtool.height2 = currtool.oheight2,currtool.owidth2,currtool.height2,currtool.width2
                try:
                    currtool.icon = transform.smoothscale(currtool.img,(currtool.width,currtool.height)) #sets icon to have same size as new image
                except:
                    currtool.icon = transform.scale(currtool.img,(currtool.width,currtool.height)) #sets icon to have same size as new image           
        elif self.func == "pixelate":
            #pixelate selected box button
            for x in range(0,selectool.width-selectool.width%5,5):
                for y in range(0,selectool.height-selectool.height%5,5):
                    avgcolor = transform.average_color(self.arg2.subsurface(x,y,5,5)) #gets average color (color of pixel) of area on surface
                    draw.rect(self.arg2,avgcolor,(x,y,5,5)) #draws pixel on surface
            selectool.selectedbox = self.arg2
            selectool.hasmenu = False #turns off menu
        elif self.func == "greyscale":
            #greyscale button
            for x in range(0,selectool.width):
                for y in range(0,selectool.height):
                    r,g,b,a = self.arg2.get_at((x,y)) #gets color at location
                    avg = (r+g+b)//3 #average of r-g-b values
                    self.arg2.set_at((x,y),(avg,avg,avg,a)) #sets r,g,b to avg
            selectool.selectedbox = self.arg2
            selectool.hasmenu = False
        elif self.func == "yanderetint":
            #yandere tint button (tints it bloodred)
            tintr,tintg,tintb,tinta = BLOODRED #RGB of color to tint
            for x in range(0,selectool.width):
                for y in range(0,selectool.height):
                    r,g,b,a = self.arg2.get_at((x,y)) #gets color at location
                    self.arg2.set_at((x,y),((tintr+r)//2,(tintg+g)//2,(tintb+b)//2,a)) #sets r,g,b to average of tint RGB
            selectool.selectedbox = self.arg2
            selectool.hasmenu = False
        elif self.func == "settranscol":
            #set transparent color button
            selectool.settranscol = True #turns on selectool settranscol boolean
            selectool.hasmenu = False
        elif self.func == "stampchange":
            #stamp page change button
            stampage += self.arg2
            stampage = max(min(stampage,len(stamps)-1),0) #Limits stamp page at 0 ~ len(stamps)-1
            del tools[-6:]
            tools += stamps[stampage] #sets new stamps in tools
        elif self.func == "sizechange":
            #size change button
            currtool.scroll(screen,self.arg2) #scrolls image
        elif self.func == "backdrop":
            #backdrop change button
            if len(undo_mem) >= 256:
                #adds screen to undo list
                del undo_mem[0] #removes the last thing undo_memorized if we're over the limit
            undo_mem.append(screen.copy().subsurface(canvas)) #appends current screen to undo list
            redo_mem = []
            if type(self.arg2) == Surface:
                screen.blit(self.arg2,canvas) #blits backdrop on canvas
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
            smallfont = font.SysFont("comicsansms",10) #small
            screen.blit(smallfont.render("RIGHT CLICK ON CANVAS FOR YANDERE VERSION",True,BLOODRED),(mx+5,my-30))
            screen.blit(smallfont.render("[Scroll to change size, space to reset size]",True,BLOODRED),(mx+5,my-17))
        elif self.func in [linetool,brushtool,erasertool,spraytool] or type(self.func) == Stamp:
            #if it's a resizable and space resettable tool we still add an extra line
            smallfont = font.SysFont("comicsansms",10) #small font
            width = max(width,smallfont.render("[Scroll to change size, space to reset size]",True,BLOODRED).get_width()+20)
            draw.rect(screen,BLACK,(mx,my-40,width,40))
            screen.blit(comicsans.render(self.toolbit,True,BLOODRED),(mx+5,my-35))
            screen.blit(smallfont.render("[Scroll to change size, space to reset size]",True,BLOODRED),(mx+5,my-17))
        elif self.func == shapetool:
            #if it's a shapetool we add extra text
            smallfont = font.SysFont("comicsansms",10) #small font
            width = max(width,smallfont.render("[Scroll to change size, space to reset size]",True,BLOODRED).get_width()+20)
            draw.rect(screen,BLACK,(mx,my-40,width,40))
            screen.blit(comicsans.render(self.toolbit,True,BLOODRED),(mx+5,my-35))
            screen.blit(smallfont.render("[Scroll to change border-size, space to reset to fill mode]",True,BLOODRED),(mx+5,my-17))
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
blurtool = Blur() #blur tool
pixelatetool = Pixelate() #pixelate tool
#STAMPS
#--page1
yunostamp = Stamp(yunogasai,yandereyuno) #Yuno Gasai stamp
kotonohastamp = Stamp(kotonohakatsura,yanderekotonoha) #Kotonoha Katsura stamp
lucystamp = Stamp(lucy,yanderelucy) #Lucy stamp
inoristamp = Stamp(inoriyuzuriha,yandereinori) #Inori Yuzuriha stamp
tokostamp = Stamp(tokofukawa,genocidersyo) #Toko Fukawa stamp
ryokostamp = Stamp(ryokoasakura,yandereryoko) #Ryoko Asakura stamp
#--page2
yukkistamp = Stamp(yukiteruamano) #Yukiteru Amano stamp
makotostamp = Stamp(makotoitou) #Makoto Itou stamp
koutastamp = Stamp(kouta) #Kouta stamp
shustamp = Stamp(shuouma) #Shu Ouma stamp
byakuyastamp = Stamp(byakuyatogami) #Byakuya Togami stamp
yukistamp = Stamp(yukinagato) #Yuki Nagato stamp
#--page3
kitchenknifestamp = Stamp(kitchenknife) #kitchen knife stamp
butcherknifestamp = Stamp(butcherknife) #butcher knife stamp
katanastamp = Stamp(katana) #katana stamp
axestamp = Stamp(axe) #axe stamp
scissorsstamp = Stamp(scissors) #scissors stamp
cutterknifestamp = Stamp(cutterknife) #cutter knife stamp
#DROP DOWN BOXES
#drop down box for fonts
fontdropdown = DropDownBox(114,412,[Button("font",comicsans.render("Comic Sans MS",True,BLACK),114,432,"Change Font-Family",136,20,"comicsansms"),
                                   Button("font",arial.render("Arial",True,BLACK),114,452,"Change Font-Family",136,20,"arial"),
                                   Button("font",timesnr.render("Times New Roman",True,BLACK),114,472,"Change Font-Family",136,20,"timesnewroman"),
                                   Button("font",lucidaconsole.render("Lucida Console",True,BLACK),114,492,"Change Font-Family",136,20,"lucidaconsole"),
                                   Button("font",impact.render("Impact",True,BLACK),114,512,"Change Font-Family",136,20,"impact"),
                                   Button("font",vladimirscript.render("Vladimir Script",True,BLACK),114,532,"Change Font-Family",136,20,"vladimirscript"),
                                   Button("font",chiller.render("Chiller",True,BLACK),114,552,"Change Font-Family",136,20,"chiller")],"SELECT FONT")
#drop down boxes for shapes
shapedropdown = DropDownBox(114,412,[Button("shape",comicsans.render("Rectangle",True,BLACK),114,432,"Draw a rectangle by clicking and dragging",136,20,"rect"),
                                     Button("shape",comicsans.render("Ellipse",True,BLACK),114,452,"Draw an ellipse by clicking and dragging",136,20,"ellipse"),
                                     Button("shape",comicsans.render("Polygon",True,BLACK),114,472,"Left-click or right-click to start setting points; left-click to continue setting points; right click to finish polygon",136,20,"polygon")],"CHANGE SHAPE")
#drop down boxes for backdrops
backdropdown = DropDownBox(132,100,[Button("backdrop",transform.smoothscale(mirainikkibackdrop,(58,44)),132,140,"Change backdrop",58,44,mirainikkibackdrop),
                                    Button("backdrop",transform.smoothscale(schooldaysbackdrop,(58,44)),190,140,"Change backdrop",58,44,schooldaysbackdrop),
                                    Button("backdrop",transform.smoothscale(elfenliedbackdrop,(58,44)),132,184,"Change backdrop",58,44,elfenliedbackdrop),
                                    Button("backdrop",transform.smoothscale(guiltycrownbackdrop,(58,44)),190,184,"Change backdrop",58,44,guiltycrownbackdrop),
                                    Button("backdrop",transform.smoothscale(danganronpabackdrop,(58,44)),132,228,"Change backdrop",58,44,danganronpabackdrop),
                                    Button("backdrop",transform.smoothscale(haruhibackdrop,(58,44)),190,228,"Change backdrop",58,44,haruhibackdrop)],"BACKGROUND",116,40)
#sets
fontdropdown.items[0].selected = True
shapedropdown.items[0].selected = True
#Fontsize buttons
fontsizebuttons = [Button("fontsize",comicsans.render(" -",True,BLACK),114,432,"Change fontsize",20,20,-1),
                    Button("fontsize",comicsans.render(" +",True,BLACK),250,432,"Change fontsize",20,20,1)]
#Font decoration buttons
fontdecorbuttons = [Button("textdec",timesnr.render(" B",True,BLACK),34,432,"Bold",20,20,"bold"),
                    Button("textdec",timesnr.render(" I",True,BLACK),54,432,"Italicize",20,20,"italic"),
                    Button("textdec",timesnr.render(" U",True,BLACK),74,432,"Underline",20,20,"underline")]
#shape width buttons
shapewidthbuttons = [Button("shapewidth",comicsans.render(" -",True,BLACK),114,432,"Change width",20,20,-1),
                   Button("shapewidth",comicsans.render(" +",True,BLACK),250,432,"Change width",20,20,1)]
#alpha buttons
alphabuttons = [Button("alpha",comicsans.render(" -",True,BLACK),132,160,"Change alpha value",20,20,-1),
                     Button("alpha",comicsans.render(" +",True,BLACK),268,160,"Change alpha value",20,20,1)]
#size change buttons
sizebuttons = [Button("sizechange",comicsans.render(" -",True,BLACK),34,432,"Decrease size",20,20,1),
               Button("sizechange",comicsans.render(" +",True,BLACK),204,432,"Increase size",20,20,0)]
#stamp edit buttons
stampeditbuttons = [Button("flip",flipicon,240,400,"Flip stamp vertically",20,20,(False,True)),
                    Button("flip",transform.rotate(flipicon,90),260,400,"Flip stamp horizontally",20,20,(True,False)),
                    Button("rotate",transform.flip(rotateicon,True,False),240,420,"Rotate stamp 90° counter-clockwise",20,20,90),
                    Button("rotate",rotateicon,260,420,"Rotate stamp 90° clockwise",20,20,-90)]
#----TOOL VARIABLES----#
currtool = penciltool #current tool
#buttons of all tools user can press (as well as other buttons such as save and open)
tools = [Button(penciltool,pencilsprite,20,100,"Pencil: 1 pixel line that follows your mouse"),
         Button(erasertool,eraser,20,150,"Eraser: Erases things to give you a second chance at artful Deadication"),
         Button(brushtool,paintbrush,20,200,"Brush: Nice thick strokes"),
         Button(spraytool,spraycan,20,250,"Spray-paint: Colours random pixels at clicked location"),
         Button(selectortool,dropper,20,300,"Colour selector: Change your mouse colour to colour at clicked location"),
         Button(textool,fancyA,20,350,"Text tool: Write some Deadicated text"),
         Button(selectool,dottedbox,80,100,"Select tool: Select an area and manipulate with Deadication"),
         Button(linetool,linesprite,80,150,"Line tool: Draw a line"),
         Button(shapetool,roundedrect,80,200,"Shape tool (Rect): Draw a rectangle by clicking and dragging"),
         Button(filltool,fillbucket,80,250,"Fill tool: Fill an area with a colour (Warning: uses a lot of CPU)"),
         Button(blurtool,bluricon,80,300,"Blur tool: Blur a 10px radius circle to blend in your \"works\" of Deadication"),
         Button(pixelatetool,pixelateicon,80,350,"Pixelate tool: Pixelate a 20px x 20px square"),
         Button("save",saveicon,1120,100,"Save your work of Deadication (Ctrl-S)",60,60),
         Button("open",openicon,1120,170,"Open a previously saved image (Ctrl-O) - right click to open without deleting current work (Ctrl-Shift-O)",60,60),
         Button("undo",undoicon,1120,240,"Undo last action on canvas (Ctrl-Z)",60,60),
         Button("redo",redoicon,1120,310,"Redo last undone action on canvas (Ctrl-Shift-Z)",60,60),
         Button("clear",clearicon,1120,380,"Clear the canvas (Ctrl-Space)",60,60),
         Button("paste",clipboard,1120,450,"Paste (Ctrl-V)",60,60)]
savebutton,openbutton = 12,13 #keeps track of save button and open button index in tools list
#stamp's 2D list, each nested list contains the stamps for one stamp page
stamps = [[Button(yunostamp,yunoface,600,690,"Paste the cute yet scary Yuno Gasai, of whom violence is no problem",50,50),
         Button(kotonohastamp,kotonohaface,660,690,"Paste the shy yet violent Kotonoha Katsura, who easily goes insane",50,50),
         Button(lucystamp,lucyface,720,690,"Paste the pretty yet ruthless Lucy, who has an amnesiac alter-ego known as Nyu",50,50),
         Button(inoristamp,inoriface,780,690,"Paste the quiet yet deadly Inori Yuzuriha, in whom the crazy Mana Ouma lives",50,50),
         Button(tokostamp,tokoface,840,690,"Paste the antisocial but sadistic Toko Fukawa, who has an alter-ego called Genocider Syo",50,50),
         Button(ryokostamp,ryokoface,900,690,"Paste the apparently cheerful but emotionless Ryoko Asakura, who'll use violence to achieve her goals",50,50)],
          [Button(yukkistamp,yukkiface,600,690,"Paste Yukiteru Amano - a wimpy boy who's the obsession of Yuno Gasai",50,50),
         Button(makotostamp,makotoface,660,690,"Paste Makoto Itou - a dumb boy who disrespects girls; Kotonoha Katsura's object of deadication",50,50),
         Button(koutastamp,koutaface,720,690,"Paste Kouta - a nice boy who is both Lucy's victim and crush",50,50),
         Button(shustamp,shuface,780,690,"Paste Shu Ouma - an average boy who gains a great power, and who Inori Yuzuriha loves",50,50),
         Button(byakuyastamp,byakuyaface,840,690,"Paste Byakuya Togami - a rich boy who looks down on others and is stalked by Toko Fukawa",50,50),
         Button(yukistamp,yukiface,900,690,"Paste Yuki Nagato - a taciturn girl who Ryoko Asakura will do ANYTHING to protect",50,50)],
          [Button(kitchenknifestamp,kitchenknifeicon,600,690,"Paste a kitchen knife - a convenient weapon if you like cooking",50,50),
         Button(butcherknifestamp,butcherknifeicon,660,690,"Paste a butcher knife - similar to a kitchen knife but stronger",50,50),
         Button(katanastamp,katanaicon,720,690,"Paste a katana - a traditional Japanese sword; a weapon of delicacy and efficiency",50,50),
         Button(axestamp,axeicon,780,690,"Paste an axe - a strong weapon that may come in handy on a trip to the woods...",50,50),
         Button(scissorsstamp,scissorsicon,840,690,"Paste a pair of scissors - great weapon that no one will expect",50,50),
         Button(cutterknifestamp,cutterknifeicon,900,690,"Paste a cutter knife - a stealthy weapon who no one will be alarmed by",50,50)]]
#stamp change buttons - for changing stamp pages
stampchangebuttons = [Button("stampchange",comicsans.render(" <",True,BLACK),840,670,"Stamp page forward",20,20,-1),
                      Button("stampchange",comicsans.render(" >",True,BLACK),930,670,"Stamp page backward",20,20,1)]
stampage = 0 #which stamp page are we on
tools += stamps[0] #adds the first page of stamps to tools
#----CANVAS----#
canvas = Rect(300,50,800,600) #canvas rect
draw.rect(screen,GREY,(299,49,802,602)) #draws canvas border
draw.rect(screen,WHITE,canvas) #draws canvas
cfiller = screen.copy().subsurface(canvas) #canvas filler
#------BACKGROUND------#
#header and subtitle
header = titlefont.render("YANDERE",True,BLACK) #header word 1 "YANDERE"
header2 = titlefont.render("SPLATTERBOARD",True,BLOODRED) #header word 2 "SPLATTERBOARD"
screen.blit(header,(440,0))
screen.blit(header2,(610,0))
#mini-titles
comicsans.set_bold(True) #bolds mini-titles
draw.rect(screen,BLACK,(19,70,62,24))
draw.rect(screen,WHITE,(19,70,60,22)) #background for tools mini-title
tooltitle = comicsans.render("TOOLS",True,BLACK) #Title of tools section
screen.blit(tooltitle,(20,70))
draw.rect(screen,BLACK,(599,660,236,24))
draw.rect(screen,WHITE,(599,660,234,22)) #background for stamps mini-title
ystamptitle = comicsans.render("STAMPS OF DEADICATION",True,BLOODRED) #Title of Yandere Character Stamps section
screen.blit(ystamptitle,(600,660))
comicsans.set_bold(False)
#----COLOR PALETTE----#
draw.rect(screen,BLACK,(19,475,262,72),1) #drawing background for palette buttons
draw.rect(screen,DARK_GREY,(20,476,260,70))
screen.blit(comicsans.render("COLOUR PALETTE",True,WHITE),(50,486)) #blitting title of color palette
draw.rect(screen,BLACK,(19,545,262,186)) #draws border for palette
palette = transform.scale(image.load("images/spectrum_chart.jpg"),(260,184)) #palette
palrect = Rect(20,546,260,184) #palette rect
pspot1 = (25,730) #spot of left mouse color on the palette
pspot2 = (25,659) #spot of right mouse color on the palette
palbuttons = [Button("color",Rect(50,506,20,20),50,506,"",20,20,BLACK),
              Button("color",Rect(70,506,20,20),70,506,"",20,20,WHITE),
              Button("color",Rect(90,506,20,20),90,506,"",20,20,RED),
              Button("color",Rect(110,506,20,20),110,506,"",20,20,GREEN),
              Button("color",Rect(130,506,20,20),130,506,"",20,20,BLUE),
              Button("color",Rect(150,506,20,20),150,506,"",20,20,PINK)]#buttons for more specific colors
custompalbuttons = [] #custom palette buttons (max-size 4)
draw.rect(screen,BLACK,(299,691,277,39))#border for gradient selector
gradsel = GradSel(300,692,275,36)#gradient selector
#----MOUSE COLOR BUTTONS----#
lcolbutton = Button("addcustom",Rect(300,656,30,30),300,656,"",30,30,lcol) #left mouse color button
rcolbutton = Button("addcustom",Rect(332,656,30,30),332,656,"",30,30,rcol) #right mouse color buttons
rcolbutton.selected = True #not really selected, but this allows for the right mouse color button to have a red border
#----INFO BUTTONS----#
#buttons that don't do anything but display info
infobuttons = [Button("",infobox,364,656,"To the left are MOUSE COLOUR INDICATORS - click them to add to CUSTOM COLOURS",20,20),
               Button("",infobox,260,400,"This translucent light-grey box is a TOOL INFORMATION BOX; it displays information about the current tool",20,20),
               Button("",infobox,261,476,"This dark grey box contains COLOUR CHANGE BUTTONS that change your mouse color as well as CUSTOM COLOURS",20,20),
               Button("",infobox,261,527,"The colorful box below is the COLOUR PALETTE, which allows you to select a large variety of colors",20,20)]
#----TOOL INFO BOX----#
toolinfo_box = Surface((260,65),SRCALPHA)
draw.rect(toolinfo_box,(185,185,185,185),(0,0,260,65))
screen.blit(toolinfo_box,(20,400))
#----BOTTOM STRIP OF INFO----#
bottomstrip = Surface((556,20),SRCALPHA)
bottomstrip.fill((150,150,150,200))
#----KEY VARIABLES----#
keytimer = 0 #timer for key pressed - allows for key holding
keypressed = "" #key pressed by user
#----VOLUME SLIDER----#
volslide = volSlider(1150,650,50,100)
#----TEMPORARY DRAWING BOARD----#
#-for transparency support
tempdraw = Surface((screen.get_width(),screen.get_height()),SRCALPHA)
tempdraw.set_clip(canvas) #clips temp draw
#----other important variables----#
lastclick = "" #keeps track of last click
filler = screen.copy() #screen filler - used for mouse sprites and toolbits and other temporary pop-ups
toolboxfiller = screen.subsurface(Rect(20,90,278,510)).copy() #tool box
undo_mem = [] #undo_memory for previous saves for the undo function
redo_mem = [] #redo_memory for saves removed by the undo function for the redo function
boxcp = None #clipboard for boxes (created by the select tool)
mousetimer = 0 #keeps track of when last mouse click happened - for the incrementing/decreasing buttons so users can hold them
buttonheld = Button("",Rect(0,0,0,0),0,0,"",0,0,BLACK) #button being held
fpstracker = pytime.Clock()
#----MAIN LOOP----#
while running:
    #----MUSIC HANDLER----#
    if not mixer.get_busy():
        song += 1
        if song >= len(music):
            #resets the playlist
            shuffle(music) #randomizes playlist
            song = 0
        music[song].play()
    screen.blit(filler,(0,0)) #fills the screen to hide toolbit, mouse sprites and other pop-ups
    #----EVENT LOOP----#
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            mb = mouse.get_pressed()
            mx,my = mouse.get_pos()
            if e.button == 4:
                #front scroll
                currtool.scroll(screen,True)
                continue
            elif e.button == 5:
                #back scroll
                currtool.scroll(screen,False)
                continue
            if canvas.collidepoint(mx,my):
                screen.set_clip(canvas)
                #if user clicks canvas
                lastclick = "canvas" #sets last click to canvas
                if not textool.hastextbox and not selectool.hasbox and not (currtool == shapetool and len(shapetool.points) > 0):
                    if len(undo_mem) >= 256:
                        del undo_mem[0] #limits undo_memory at 256
                    #makes sure we don't have an open text box or an open select box when we click, as that will just close the selected box and shouldn't be saved into undo_memory
                    redo_mem = [] #makes the redo option empty as it shouldn't do anything once new data is added to the screen
                    undo_mem.append(screen.copy().subsurface(canvas)) #adds a screenshot to the undo list undo_memory before the user's change to the canvas
                if e.button == 1:
                    currtool.lclick(screen) #calls tool's left click method
                elif e.button == 3:
                    currtool.rclick(screen) #calls tool's right click method
                screen.set_clip(None)
            elif fontdropdown.mainrect.collidepoint(mx,my) and currtool == textool or (fontdropdown.menudown and fontdropdown.menurect.collidepoint(mx,my)):
                #if user clicks font drop down menu
                lastclick = "fontdropdown"
                fontdropdown.clickon(screen)
            elif shapedropdown.mainrect.collidepoint(mx,my) and currtool == shapetool or (shapedropdown.menudown and shapedropdown.menurect.collidepoint(mx,my)):
                #if user clicks shape drop down menu
                lastclick = "shapedropdown"
                shapedropdown.clickon(screen)
            elif backdropdown.mainrect.collidepoint(mx,my) or (backdropdown.menudown and backdropdown.menurect.collidepoint(mx,my)):
                #if user clicks backdrop drop down menu
                lastclick = "backdropdown"
                backdropdown.clickon(screen)
            elif selectool.hasmenu and selectool.menurect.collidepoint(mx,my) and currtool == selectool:
                #if user clicks menu on select tool
                lastclick = "selectmenu"
                selectool.lclick(screen)
            elif gradsel.istouch():
                #if user clicked gradient selector
                lastclick = "gradsel"
                if e.button == 1:
                    #left click
                    gradsel.lclick(screen)
                elif e.button == 3:
                    #right click
                    gradsel.rclick(screen)
            elif palrect.collidepoint(mx,my):
                #if user clicks palette
                lastclick = "palette"
            else:
                #if user doesn't click palette or canvas
                if e.button == 2:
                    #makes sure nothing happens if the use uses middle click
                    continue
                lastclick = "" #set last click to "" (which means everything except canvas, drop down boxes and palette)
                #checks if we clicked volume slider
                if volslide.istouch():
                    lastclick = "volslide"
                    continue
                #following loop checks for tools/buttons and if we clicked them or not
                if currtool == textool:
                    for b in fontsizebuttons:
                        if b.istouch():
                            b.clickon(screen)
                            buttonheld = b
                            mousetimer = time() #sets time clicked and button held
                            lastclick = "fontsize"
                            break
                    for b in fontdecorbuttons:
                        if b.istouch():
                            b.clickon(screen)
                            b.selected = not b.selected #sets whether b is seleced or not (if it is it turns it off, otherwise it turns it on)
                            lastclick = "fontdecor"
                if currtool == shapetool:
                    for b in shapewidthbuttons:
                        if b.istouch():
                            b.clickon(screen)
                            buttonheld = b
                            mousetimer = time() #sets time clicked and button held
                            lastclick = "bordersize"
                            break
                if type(currtool) == Stamp:
                    for b in stampeditbuttons:
                        if b.istouch():
                            b.clickon(screen)
                            lastclick = "stampedit"
                            break
                if currtool in [penciltool,brushtool,spraytool,shapetool,linetool]:
                    for b in alphabuttons:
                        if b.istouch():
                            lastclick = "alphabutton"
                            buttonheld = b
                            mousetimer = time() #sets time clicked and button held
                            b.clickon(screen)
                            break
                if currtool in [erasertool,brushtool,spraytool,linetool] or type(currtool) == Stamp:
                    for b in sizebuttons:
                        if b.istouch():
                            lastclick = "sizebutton"
                            buttonheld = b
                            mousetimer = time() #sets time clicked and button held
                            b.clickon(screen)
                for b in palbuttons+custompalbuttons:
                    if b.istouch():
                        lastclick = "palbutton"
                        b.clickon(screen)
                        break
                for b in [lcolbutton,rcolbutton]:
                    if b.istouch():
                        lastclick = "mousebutton"
                        b.clickon(screen)
                        break
                for b in stampchangebuttons:
                    if b.istouch():
                        lastclick = "stampchange"
                        buttonheld = b
                        mousetimer = time() #sets time clicked and button held
                        b.clickon(screen)
                        break
                screen.set_clip(canvas)
                currtool.outside() #runs current tool's outside function, as user clicked outside of canvas
                screen.set_clip(None)
                for t in tools:
                    if t.istouch():
                        if t.func in ["save","open"]:
                            buttonheld = t #makes t the button held
                            break #doesn't do it on mouse down for save and open - does it on mouseup to avoid it acting funny
                        if t.func != currtool:
                            screen.blit(toolboxfiller,(20,90)) #blits toolbox when user changes tools
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
            if lastclick != "backdropdown":
                backdropdown.menudown = False #turns off menu in backdropdown if it was not clicked
        if e.type == MOUSEBUTTONUP:
            if lastclick == "canvas":
                if e.button not in [4,5]:
                    currtool.mouseup(screen) #tool's mouseup method
            else:
                #checks if user clicked a tool button
                #does on mouseup so save and open don't act all funny
                for i in [savebutton,openbutton]:
                    opt = tools[i] #option (save or open) selected
                    if opt.istouch():                
                        if e.button == 3:
                            #handles right clicking on button
                            opt.clickon(screen,True)
                        else:
                            #handles left clicking on button
                            opt.clickon(screen)
                        break
            buttonheld = Button("",Rect(0,0,0,0),0,0,"",0,0,BLACK) #clears held button
            mousetimer = 0 #resets mouse timer
        if e.type == KEYDOWN:
            #----KEY PRESS FUNCTIONS----#
            kp = key.get_pressed()
            keypressed = e.unicode #pressed key
            keytimer = time() #time pressed by user
            canundo = True #can the user undo under the circumstances (applies to redo as well)
            if textool.hastextbox or selectool.hasbox or (currtool == shapetool and len(shapetool.points) > 0) or mouse.get_pressed()[0] or mouse.get_pressed()[2]:
                #if the current tool has a text box, you cannot undo
                #if the current tool has a box, you cannot undo
                #if we are currently forming a polygon, we cannot undo
                #if we are holding down a mouse button, we cannot undo
                canundo = False
            if kp[K_z] and (kp[K_LCTRL] or kp[K_RCTRL]) and (kp[K_LSHIFT] or kp[K_RSHIFT]) and canundo:
                #if the user pressed Ctrl-Shift-Z will redo
                if len(redo_mem) > 0:
                    if len(undo_mem) >= 256:
                        del undo_mem[0] #removes the last thing undo_memorized if we're over the limit
                    undo_mem.append(screen.copy().subsurface(canvas)) #appends current screen to undo list
                    prevsave = redo_mem.pop(-1) #gets new screen from redo list
                    screen.blit(prevsave,(canvas[0],canvas[1]))
            elif kp[K_z] and (kp[K_LCTRL] or kp[K_RCTRL]) and canundo:
                #if the user presses Ctrl-Z will undo
                if len(undo_mem) > 0:
                    redo_mem.append(screen.copy().subsurface(canvas)) #appends the current screen to redo list
                    prevsave = undo_mem.pop(-1) #prevsave = last screen save
                    screen.blit(prevsave,(canvas[0],canvas[1])) #fills the screen with new save
            elif kp[K_SPACE] and (kp[K_LCTRL] or kp[K_RCTRL]):
                #clears the canvas if user presses CTRL and space
                if len(undo_mem) >= 256:
                    del undo_mem[0] #removes the last thing undo_memorized if we're over the limit
                redo_mem = [] #makes the redo option empty as it shouldn't do anything once new data is added to the screen
                undo_mem.append(screen.copy().subsurface(canvas)) #adds a screenshot to the undo list undo_memory before the user's change to the canvas
                draw.rect(screen,WHITE,canvas)
                tempdraw.fill((255,255,255,0)) #clears tempdraw
            elif kp[K_s] and (kp[K_LCTRL] or kp[K_RCTRL]):
                #if user presses CTRL-S will save
                if not canundo:
                    if type(currtool) == Select:
                        currtool.hasbox = False
                    elif type(currtool) == Text:
                        currtool.hastextbox = False
                mouse.set_visible(True)
                savename = filedialog.asksaveasfilename(defaultextension=".jpg")
                if savename:
                    image.save(screen.copy().subsurface(canvas), savename)
                mouse.set_visible(False)
            elif kp[K_o] and (kp[K_LCTRL] or kp[K_RCTRL]):
                #if user presses CTRL-O will open a file and paste it onto canvas
                if not canundo:
                    if type(currtool) == Select:
                        currtool.hasbox = False
                    elif type(currtool) == Text:
                        currtool.hastextbox = False
                mouse.set_visible(True)
                loadname = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.bmp;*.jpg;*.jpeg")])
                if loadname:
                    if len(undo_mem) >= 256:
                        del undo_mem[0] #removes the last thing undo_memorized if we're over the limit
                    redo_mem = []
                    undo_mem.append(screen.copy().subsurface(canvas))
                    if not kp[K_LSHIFT] and not kp[K_RSHIFT]:
                            draw.rect(screen,WHITE,canvas) #clears everything previously on the canvas if user does not hold shift
                    cfiller = screen.copy().subsurface(canvas)
                    opened_image = image.load(loadname)
                    img_ratio = opened_image.get_width()/opened_image.get_height()
                    if opened_image.get_width() >= opened_image.get_height():
                        width = (min(opened_image.get_width(),canvas[2]))
                        height = (int(width/img_ratio))
                    else:
                        height = (min(opened_image.get_height(),canvas[3]))
                        width = (int(height*img_ratio))
                    currtool = selectool #changes current tool to select tool
                    currtool.hasbox = True
                    currtool.selectedbox = transform.scale(opened_image,(width,height)) #makes opened image the box's image
                    currtool.x,currtool.y,currtool.width,currtool.height = 300,50,width,height #creating a select box around uploaded image
                mouse.set_visible(False)
            elif kp[K_v] and (kp[K_LCTRL] or kp[K_RCTRL]):
                #CTRL-V
                #pastes clipboard image
                if boxcp != None:
                    if None not in boxcp:
                        if len(undo_mem) >= 256:
                            del undo_mem[0] #removes the last thing undo_memorized if we're over the limit
                        undo_mem.append(screen.copy().subsurface(canvas)) #appends current screen to undo list
                        redo_mem = []
                        screen.set_clip(canvas)
                        if selectool.hasbox:
                            screen.blit(selectool.selectedbox,(selectool.x,selectool.y))
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
        if e.type == KEYUP:
            keypressed = ""
            keytimer = 0
            
    #----BACKGROUND----#
    mx,my = mouse.get_pos() #mouse position
    #----MOUSE COLOR BOXES----#
    #draws boxes that indicate color of both mouse buttons
    lcolbutton.arg2 = lcol
    rcolbutton.arg2 = rcol
    lcolbutton.display(screen)
    rcolbutton.display(screen)
    #----DROP DOWN BOXES----#
    #draw backdropdown
    backdropdown.drawbox(screen)
    #draw dropdownboxes if the respective tool is selected
    if currtool == textool:
        fontdropdown.drawbox(screen)
    if currtool == shapetool:
        shapedropdown.drawbox(screen)
    #----DRAWING PALETTE----#
    for b in palbuttons+custompalbuttons:
        b.display(screen)
    screen.blit(palette,palrect)
    #----DRAWING GRADIENT SELECTOR----#
    gradsel.draw(screen)
    #----DRAWING BUTTONS----#
    for b in tools+infobuttons:
        b.display(screen)
    if currtool == textool:
        #draws fontsizebuttons if textool is current tool
        for b in fontsizebuttons:
            b.display(screen)
        for b in fontdecorbuttons:
            b.display(screen)
    if currtool == shapetool:
        #draws shape border change buttons if shapetool is current tool
        for b in shapewidthbuttons:
            b.display(screen)
    if currtool in [erasertool,brushtool,spraytool,linetool] or type(currtool) == Stamp:
        #draws sizebuttons if the current tool has a size attribute (e.g. brush, eraser, stamps)
        for b in sizebuttons:
            b.display(screen)
    if type(currtool) == Stamp:
        #draws stamp edit buttons if, obviously, the current tool is a stamp
        for b in stampeditbuttons:
            b.display(screen)
    #----STAMP CHANGER----#
    for b in stampchangebuttons:
        b.display(screen)#displays stamp change buttons
    draw.rect(screen,WHITE,(860,670,70,20)) #drawing background for stamp page indicator
    draw.rect(screen,BLACK,(860,670,70,20),1)
    screen.blit(comicsans.render("Page "+str(stampage+1)+"/"+str(len(stamps)),True,BLACK),(861,670)) #blits page indicator
    #----SIZE INDICATORS AND CHANGERS----#
    if currtool == textool:
        draw.rect(screen,WHITE,(134,432,116,20))
        screen.blit(comicsans.render("Font-size: "+str(textool.fontsize),True,BLACK),(134,432)) #displays fontsize for textbox
    elif currtool == shapetool:
        draw.rect(screen,WHITE,(134,432,116,20))
        dispwidth = "Border size: "+str(shapetool.width) if shapetool.width > 0 else "No border (fill)"
        screen.blit(comicsans.render(dispwidth,True,BLACK),(134,432)) #displays width of shapetool for shape tool
    elif currtool in [erasertool,brushtool,spraytool,linetool] or type(currtool) == Stamp:
        draw.rect(screen,WHITE,(54,432,150,20))
        draw.rect(screen,BLACK,(54,432,150,20),1)
        try:
            size = currtool.size*2 if currtool.size != 0 else 1
            screen.blit(comicsans.render("Size: "+str(size),True,BLACK),(55,433))
        except:
            screen.blit(comicsans.render("Percentage: "+str(currtool.percentage)+"%",True,BLACK),(55,433))
    #----TRANSPARENCY INDICATOR----#
    if currtool in [penciltool,brushtool,spraytool,shapetool,linetool]:
        #displays transparency if transparency is available for tool
        draw.rect(screen,WHITE,(152,150,116,40))
        draw.rect(screen,BLACK,(152,150,116,40),1)
        comicsans.set_bold(True)
        screen.blit(comicsans.render("Opacity",True,BLACK),(154,150))
        comicsans.set_bold(False)
        screen.blit(comicsans.render(str(alpha)+"%",True,BLACK),(154,170)) #displays transparency for brush
        for b in alphabuttons:
            b.display(screen) #draws buttons
    #----MOUSE HOLD FUNCTIONS----#
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()
    if mb[0] or mb[2]:
        if canvas.collidepoint(mx,my) and lastclick == "canvas":
                screen.set_clip(canvas)
                currtool.cont(screen)
                screen.set_clip(None)
        else:
            if lastclick == "canvas" or currtool == textool:
                screen.set_clip(canvas)
                currtool.outside()
                screen.set_clip(None)
            if mousetimer != 0:
                #checks if mousetimer is set - if it is we call the button's click method
                if time() - mousetimer > 0.5:
                    if buttonheld.istouch():
                        buttonheld.clickon(screen)
            if palrect.collidepoint(mx,my) and lastclick == "palette":
                #if user clicked in palette, the following if statements will change the color of either his/her left mouse or his right mouse button
                if mb[0]:
                    lcol = screen.get_at((mx,my))
                    lcol = Color(lcol[0],lcol[1],lcol[2],int(alpha/100*255))#sets transparency
                    pspot1 = (mx,my) #changes position of left-mouse circle on canvas
                elif mb[2]:
                    rcol = screen.get_at((mx,my))
                    rcol = Color(rcol[0],rcol[1],rcol[2],int(alpha/100*255))#sets transparency
                    pspot2 = (mx,my) #changes position of right-mouse circle on canvas
            elif gradsel.istouch() and lastclick == "gradsel":
                #gradient selector mouse hold
                gradsel.cont(screen)
            elif volslide.istouch() and lastclick == "volslide":
                #volume slider mouse hold
                volslide.cont(screen)
    elif mb[1]:
        pass
    else:
        gradsel.mouseup(screen) #if user isn't clicking the mouse we call the gradient selector mouseup method
    #----KEY HOLD HANDLING----#
    if keytimer != 0:
        if time() - keytimer > 0.5:
            #allows for user to hold key down
            canundo = True #can the user undo under the circumstances (applies to redo as well)
            if textool.hastextbox or selectool.hasbox or (currtool == shapetool and len(shapetool.points) > 0) or mouse.get_pressed()[0] or mouse.get_pressed()[2]:
                #if the current tool has a text box, you cannot undo
                #if the current tool has a box, you cannot undo
                #if we are currently forming a polygon, we cannot undo
                #if we are holding down a mouse button, we cannot undo
                canundo = False
            if kp[K_z] and (kp[K_LCTRL] or kp[K_RCTRL]) and (kp[K_LSHIFT] or kp[K_RSHIFT]) and canundo:
                #if the user pressed Ctrl-Shift-Z will redo
                if len(redo_mem) > 0:
                    if len(undo_mem) >= 256:
                        del undo_mem[0] #removes the last thing undo_memorized if we're over the limit
                    undo_mem.append(screen.copy().subsurface(canvas)) #appends current screen to undo list
                    prevsave = redo_mem.pop(-1) #gets new screen from redo list
                    screen.blit(prevsave,(canvas[0],canvas[1]))
            elif kp[K_z] and (kp[K_LCTRL] or kp[K_RCTRL]) and canundo:
                #if the user presses Ctrl-Z will undo
                if len(undo_mem) > 0:
                    redo_mem.append(screen.copy().subsurface(canvas)) #appends the current screen to redo list
                    prevsave = undo_mem.pop(-1) #prevsave = last screen save
                    screen.blit(prevsave,(canvas[0],canvas[1])) #fills the screen with new save
            else:
                #if user held the key for more than 0.5 seconds, it calls the keypress function
                currtool.keypress(screen,keypressed)
                sleep(0.015) #delays the time a little bit when holding the key
    #----SCREEN SAVING----#  
    filler = screen.copy() #copies all updates into filler
    #----Temporary drawings that should never stick to screen (e.g. sprites and toolbits)----#
    #DRAWS TEMPORARY DRAWING BOARD FOR LINES - THIS IS TO SUPPORT TRANSPARENCY
    if mb[0] or mb[2] or len(shapetool.points) > 0:
        screen.blit(tempdraw,(0,0))
    #DRAWS GRADIENT SELECTOR SELECTED LINE
    gradsel.drawSel(screen)
    #DRAWS VOLUME SLIDER
    volslide.draw(screen)
    volslide.drawSel(screen)
    #DRAWS CIRCLES OF COLOR INDICATION ON PALETTE
    draw.circle(screen,WHITE,pspot1,10,1)
    draw.circle(screen,BLOODRED,pspot2,10,1)
    #----DRAWING BOTTOM STRIP BELOW THE PALETTE----#
    screen.blit(bottomstrip,(20,730))
    if canvas.collidepoint(mx,my):
        coords = "X: "+str(mx-300)+" Y: "+str(my-50)
    else:
        coords = "Off Canvas"
    screen.blit(lucidaconsole.render(coords+" L-Col: "+str(lcol[:3])+" R-Col: "+str(rcol[:3]),True,BLACK),(21,733))
    #DRAWS INFORMATION ON TOOL INFO BOX
    screen.blit(comicsans.render(currtool.__class__.__name__+" tool",True,BLACK),(30,412)) #blits tools' class name
    if currtool == shapetool:
        screen.blit(comicsans.render(shapetool.shape.title(),True,BLACK),(30,427)) #blits shape tool's shape
    if currtool == selectool and selectool.hasbox:
        screen.blit(comicsans.render("X: "+str(selectool.x-canvas[0])+" Y: "+str(selectool.y-canvas[1]),True,BLACK),(120,412)) #blits selected box's co-ords (relative to canvas)
        screen.blit(comicsans.render(str(selectool.width)+" x "+str(selectool.height),True,BLACK),(30,427)) #blits selected box's dimensions
    if type(currtool) == Stamp:
        #if the tool is a stamp labels dimensions
        if mb[2] and currtool.img != currtool.img2:
            screen.blit(comicsans.render(str(currtool.width2)+"px x "+str(currtool.height2)+"px",True,RED),(120,412)) #labels red if right clicking and the 2nd image is different from the first
        else:
            screen.blit(comicsans.render(str(currtool.width)+"px x "+str(currtool.height)+"px",True,BLACK),(120,412))
    #HANDLES DROP DOWN MENUS' MENU
    if fontdropdown.menudown:
        for i in fontdropdown.items:
            #sets all highlighted items in dropdown menu to highlighted or unhighlighted
            if i.istouch():
                i.highlighted = True
            else:
                i.highlighted = False
        fontdropdown.dropdown(screen) #draws menu items
    if shapedropdown.menudown:
        for i in shapedropdown.items:
            if i.istouch():
                i.highlighted = True
            else:
                i.highlighted = False
        shapedropdown.dropdown(screen)
    if backdropdown.menudown:
        for i in backdropdown.items:
            if i.istouch():
                i.highlighted = True
            else:
                i.highlighted = False
        backdropdown.dropdown(screen)
    #DRAWS TEXTBOX IF THE TEXT TOOL IS SELECTED AND A TEXTBOX IS OPEN
    screen.set_clip(canvas)
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
                draw.rect(screen,RED,(x-5,y-5,10,10),2)
                draw.rect(screen,WHITE,(x-4,y-4,8,8))
        screen.set_clip(None)
        #handles selected box's menu
        if selectool.hasmenu:
            for b in selectool.menu:
                b.display(screen)        
    screen.set_clip(None)

    #DRAWS FPS AT TOP OF SCREEN
    screen.blit(lucidaconsole.render("FPS: "+str(round(fpstracker.get_fps(),1)),True,BLACK),(5,7))
    #DRAWS TOOLBIT
    #following loop displays toolbit if the mouse is touching a tool button or an info button
    for b in tools+infobuttons+stampeditbuttons:
        if b.istouch():
            b.disptoolbit(screen)
            break
    #DRAWS MOUSE SPRITE
    if canvas.collidepoint(mx,my) and (not selectool.hasmenu or not selectool.menurect.collidepoint(mx,my)):
        #if the mouse is above the canvas and not above a menu, we draw a sprite
        mouse.set_visible(False)
        currtool.drawsprite(screen)
    else:
        #else we draw the mouse
        mouse.set_visible(True)
    display.flip()
    fpstracker.tick()
root.destroy()
quit()
