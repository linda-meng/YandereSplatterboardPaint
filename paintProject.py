from pygame import *
from random import *
from math import *
from tkinter import *
font.init()
#----METADATA----#
__author__ = "Yttrium Z (You Zhou)"
__date__ = "Not finished"
__purpose__ = "Grade 11 Project - Paint Program"
__name__ = "Yandere Splatterboard"
__copyright__ = "Yttrium Z 2015-2016"
#----PERMANENT CONSTANT DATA----#
#data that can never change no matter what user does
#MUSIC
#mixer.init()
#mixer.Sound("music/MiraiNikkiOP.ogg").play(-1)
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
crosscursor = transform.scale(image.load("images/crosscursor.gif"),(40,40))
yunoface = transform.scale(image.load("images/yunoface.png"),(60,60))
yunogasai = image.load("images/yunogasai.png")
#SETUP
root = Tk()
root.withdraw()
screen = display.set_mode((1200,750))
screen.fill(PINK)
display.set_caption("YANDERE SPLATTERBOARD - PAINT PROGRAM BY YOU ZHOU ~~~~~~GREAT ART TAKES DEADICATION~~~~~~")
running = True
#--------------------UI CLASSES (like textboxes, scroll boxes)--------------------#
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
        #changes starting to point to still follow the mouse
        #this is for more fluid painting
        mx,my = mouse.get_pos()
        self.sx = mx
        self.sy = my
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
        #changes starting point to still follow the mouse - more fluidity
        mx,my = mouse.get_pos()
        self.sx = mx
        self.sy = my
    def drawsprite(self,screen):
        mx,my = mouse.get_pos()
        draw.circle(screen,WHITE,(mx,my),self.size) #draws circle to show user how big eraser is
        super(Eraser,self).drawsprite(screen) #Calls on Tool class's default toolbit, as that fits the bill for the Eraser tool
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
        #changes starting point to still follow the mouse - fluidity
        mx,my = mouse.get_pos()
        self.sx = mx
        self.sy = my
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
#-------------------------------------------Stamp
class Stamp(Tool):
    #stamps images
    def __init__(self,img,img2=False):
        self.img = img #image the stamp will stamp
        self.width = self.img.get_width() #dimensions of stamp
        self.height = self.img.get_height()
        self.ratio = self.width/self.height #width:height ratio
        if not img2:
            self.img2 = img #image the stamp stamps when right clicked - default is current stamp
        else:
            self.img2 = img2
        self.icon = self.img
    def lclick(self,screen):
        #pastes image 1 at the middle on the mouse
        mx,my = mouse.get_pos()
        screen.blit(transform.scale(self.img,(self.width,self.height)),(mx-self.width/2,my-self.height/2))
    def rclick(self,screen):
        #pastes image 2 at the middle on the mouse
        mx,my = mouse.get_pos()
        screen.blit(transform.scale(self.img2,(self.width,self.height)),(mx-self.width//2,my-self.height//2))
    def scroll(self,screen,forward=True):
        if forward:
            #makes image smaller
            if min(self.width,self.height) > 20:
                #makes sure image is at least 20px wide and 20px high
                if self.width <= self.height:
                    self.width -= 3
                    self.height = int(self.width/self.ratio)
                else:
                    self.height -= 3
                    self.width = int(self.height*self.ratio)
        else:
            #makes image bigger
            if max(self.width,self.height) < 1024:
                #limits image width and height at 1024px
                if self.width >= self.height:
                    self.width += 3
                    self.height = int(self.width/self.ratio)
                else:
                    self.height += 3
                    self.width = int(self.height*self.ratio)
        self.icon = transform.scale(self.img,(self.width,self.height)) #sets icon to have same size as new image
    def drawsprite(self,screen):
        mx,my = mouse.get_pos()
        screen.blit(self.icon,(mx-self.width//2,my-self.height//2))
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
        mx,my = mouse.get_pos()
        screen.blit(self.icon,(mx,my-40))
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
        self.icon = fancyA
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
            #turns of text box if we have one
            self.hastextbox = False
            currtool.textbox.drawtext(screen)
        else:
            #draws a text box if we don't have one
            self.textbox = Textbox(mx,my,20,20,self.fontfamily,self.fontsize,rcol)
            self.hastextbox = True
    def keypress(self,screen,keypressed):
        #the only tool who uses this method
        #it allows the tool to interact with the user's keyboard
        if self.hastextbox:
            kp = key.get_pressed()
            if kp[K_RETURN]:
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
    def lclick(self,screen):
        global cfiller
        mx,my = mouse.get_pos()
        if self.hasbox:
            #if the box exists and user doesn't click it, the box disappears
            if not Rect(self.x,self.y,self.width,self.height).collidepoint(mx,my):
                screen.blit(cfiller,(300,50))
                self.hasbox = False
                screen.blit(self.selectedbox,(self.x,self.y))
            else:
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
            draw.rect(screen,BLACK,(self.x-1,self.y-1,self.width+2,self.height+2),1)
            self.forming = False
    def cont(self,screen):
        global cfiller
        mx,my = mouse.get_pos()
        if self.hasbox:
            screen.blit(cfiller,(300,50)) #makes sure box only appears once
            self.x = mx-self.dx
            self.y = my-self.dy
            draw.rect(screen,BLACK,(self.x-1,self.y-1,self.width+2,self.height+2),1)
            screen.blit(self.selectedbox,(self.x,self.y))
        elif self.forming:
            self.width = abs(self.x - mx) #width of rect is absolute distance between mouse-x and start-x
            self.height = abs(self.y - my) #height of rect is same idea as width, but with y-coords
            #the following two if statements set start x and start y to mx and my if they are greater
            screen.blit(cfiller,(300,50)) #makes sure box only appears once
            draw.rect(screen,BLACK,(min(self.x,mx)-1,min(self.y,my)-1,self.width+2,self.height+2),1)
    def outside(self):
        #removes the box if use pressed outside canvas
        global screen
        global cfiller
        if self.hasbox:
            screen.blit(cfiller,(300,50))
            self.hasbox = False
            screen.blit(self.selectedbox,(self.x,self.y))
    def drawsprite(self,screen):
        mx,my = mouse.get_pos()
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
        mx,my = mouse.get_pos()
        self.sx,self.sy = mx,my
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
            draw.ellipse(screen,self.col,(sx,sy,abs(self.sx-mx),abs(self.sy-my)),self.width)
#-------------------------------------------Fill Tool
class Fill(Tool):
    #fills an area with a colour
    def __init__(self):
        self.icon = fillbucket
        self.fcol = BLACK #fill colour - what the colour to change pixels into
        self.ccol = WHITE #change colour - what colours to change
    def lclick(self,screen):
        global lcol
        mx,my = mouse.get_pos()
        self.fcol = lcol #sets fill colour to left mouse colour
        self.ccol = screen.get_at((mx,my)) #sets change colour to where user clicked
        tochange = set()#set of pixels to change
        tochange.add((mx,my))
        while len(tochange) > 0:
            x,y = tochange.pop()
            if 300 < x < 1100 and 50 < y < 650:
                #changes the colour of all four directions
                if screen.get_at((x,y)) == self.ccol:
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
        tochange = set()#set of pixels to change
        tochange.add((mx,my))
        while len(tochange) > 0:
            x,y = tochange.pop()
            if 300 < x < 1100 and 50 < y < 650:
                #changes the colour of all four directions
                if screen.get_at((x,y)) == self.ccol:
                    screen.set_at((x,y),self.fcol)
                    tochange.add((x+1,y))
                    tochange.add((x-1,y))
                    tochange.add((x,y+1))
                    tochange.add((x,y-1))
    def drawsprite(self,screen):
        mx,my = mouse.get_pos()
        screen.blit(self.icon,(mx-40,my-40))
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
        self.selected = False #is this the current tool? (only applies to tool buttons)
        self.toolbit = toolbit
        self.arg2 = arg2 #2nd argument for button - optional. Tool buttons don't use this
    def display(self,screen):
        #displays button
        if self.highlighted:
            dispcol = RED
        else:
            dispcol = WHITE
        draw.rect(screen,dispcol,(self.x,self.y,self.width,self.height))
        if type(self.pic) == Surface:
            screen.blit(self.pic,[self.x,self.y])
        elif type(self.pic) == Rect:
            draw.rect(screen,self.arg2,self.pic)
        if self.selected:
            #If it's the selected tool, the border of the button is red, otherwise it's black
            draw.rect(screen,RED,(self.x,self.y,self.width,self.height),1)
        else:
            draw.rect(screen,BLACK,(self.x,self.y,self.width,self.height),1)
    def istouch(self):
        #is the mouse touching the button? Well this method says!
        mx,my = mouse.get_pos()
        rectform = Rect(self.x,self.y,self.width,self.height)
        return rectform.collidepoint(mx,my)
    def clickon(self,screen):
        global textool
        global currtool
        global lcol
        global rcol
        global shapetool
        if issubclass(type(self.func),Tool):
            #tool change button
            currtool = self.func
        elif self.func == "font":
            #font change button
            curtool = textool
            for t in tools:
                t.selected = False #makes all tools unselected
            tools[5].selected = True #makes text tool selected
            textool.fontfamily = self.arg2
            textool.textbox.changefont(self.arg2,textool.textbox.fontsize) #changes fontfamily
        elif self.func == "fontsize":
            #fontsize change button
            currtool = textool
            for t in tools:
                t.selected = False
            tools[5].selected = True
            newfontsize = textool.fontsize + self.arg2
            newfontsize = min(99,newfontsize)
            newfontsize = max(5,newfontsize) #limits new font size
            textool.fontsize = newfontsize
            textool.textbox.changefont(textool.textbox.fontfamily,newfontsize) #changes fontsize
        elif self.func == "shape":
            #shape change button
            currtool = shapetool
            for t in tools:
                t.selected = False
            tools[8].selected = True
            shapetool.shape = self.arg2 #changes shapetool to shape
            if self.arg2 == "ellipse":
                tools[8].pic = ellipsesprite
                shapetool.icon = ellipsesprite
            elif self.arg2 == "rect":
                tools[8].pic = roundedrect
                shapetool.icon = roundedrect
        elif self.func == "color":
            #color change button
            mb = mouse.get_pressed()
            if mb[0]:
                lcol = self.arg2
            elif mb[2]:
                rcol = self.arg2
    def disptoolbit(self,screen):
        #displays the toolbit so that user can know what button's tool does
        global comicsans
        mx,my = mouse.get_pos()
        draw.rect(screen,BLACK,(mx,my-35,500,35))
        screen.blit(comicsans.render(self.toolbit,True,BLOODRED),(mx+5,my-30))

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
yunostamp = Stamp(yunogasai) #yuno gasai stamp
#DROP DOWN BOXES
fontdropdown = DropDownBox(20,390,[Button("font",comicsans.render("Comic Sans MS",True,BLACK),20,410,"Change Font-Family",200,20,"comicsansms"),
                                   Button("font",arial.render("Arial",True,BLACK),20,430,"Change Font-Family",200,20,"arial")],"SELECT FONT")
shapedropdown = DropDownBox(120,200,[Button("shape",comicsans.render("Rectangle",True,BLACK),120,220,"Change Shape",170,20,"rect"),
                                     Button("shape",comicsans.render("Ellipse",True,BLACK),120,240,"Change Shape",170,20,"ellipse")],"CHANGE SHAPE")
#^drop down box for fonts
fontdropdown.items[0].selected = True #sets first item in dropdownboxes to be selected
shapedropdown.items[0].selected = True
#Fontsize buttons
fontsizebuttons = [Button("fontsize",comicsans.render(" <",True,BLACK),60,370,"Change fontsize",20,20,-1),
                   Button("fontsize",comicsans.render(" >",True,BLACK),100,370,"Change fontsize",20,20,1)]
#----TOOL VARIABLES----#
currtool = penciltool #current tool
tools = [Button(penciltool,pencilsprite,20,100,"Pencil: 1 pixel line that follows your mouse"),
         Button(erasertool,eraser,20,150,"Eraser: Gives you a second chance at artful Deadication"),
         Button(brushtool,paintbrush,20,200,"Brush: Nice thick strokes"),
         Button(spraytool,spraycan,20,250,"Spray-paint: Colours random pixels at clicked location"),
         Button(selectortool,dropper,20,300,"Colour selector: Change your mouse colour to colour at clicked location"),
         Button(textool,fancyA,20,350,"Text tool: Write some Deadicated text"),
         Button(selectool,dottedbox,80,100,"Select tool: Select an area and manipulate with Deadication"),
         Button(linetool,linesprite,80,150,"Line tool: Draw a line"),
         Button(shapetool,roundedrect,80,200,"Shape tool: Draw a shape to give your Deadication some structure"),
         Button(filltool,fillbucket,80,250,"Fill tool: Fill an area up with a colour"),
         Button(yunostamp,yunoface,550,690,"Paste the cute yet scary Yuno Gasai",60,60)] #buttons of all tools user can press
tools[0].selected = True #the penciltool button is selected, so I set it so
#----CANVAS----#
canvas = Rect(300,50,800,600) #canvas rect
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
ystamptitle = comicsans.render("YANDERE CHARACTER STAMPS",True,BLOODRED) #Title of Yandere Character Stamps section
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

#----MAIN LOOP----#
while running:
    screen.blit(filler,(0,0)) #fills the screen to hide toolbit, mouse sprites and other pop-ups
    #----EVENT LOOP----#
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            mb = mouse.get_pressed()
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
                    if len(mem) < 256:
                        if type(currtool) == Text:
                            if not currtool.hastextbox:
                                #makes sure the turning off of a textbox doesn't proc a memory addition
                                mem2 = [] #makes the redo option empty as it shouldn't do anything once new data is added to the screen
                                mem.append(screen.copy()) #adds a screenshot to the undo list memory before the user's change to the canvas                            
                        elif type(currtool) == Select:
                            if not currtool.hasbox:
                                #makes sure moving a selected box doesn't proc this
                                mem2 = [] #makes the redo option empty as it shouldn't do anything once new data is added to the screen
                                mem.append(screen.copy()) #adds a screenshot to the undo list memory before the user's change to the canvas  
                        else:
                            mem2 = [] #makes the redo option empty as it shouldn't do anything once new data is added to the screen
                            mem.append(screen.copy()) #adds a screenshot to the undo list memory before the user's change to the canvas
                    if mb[0]:
                        currtool.lclick(screen) #calls tool's left click method
                    elif mb[2]:
                        currtool.rclick(screen) #calls tool's right click method
                screen.set_clip(None)
            elif palrect.collidepoint(mx,my):
                #if user clicks palette
                lastclick = "palette"
            elif fontdropdown.mainrect.collidepoint(mx,my) or (fontdropdown.menudown and fontdropdown.menurect.collidepoint(mx,my)):
                #if user clicks font drop down menu
                lastclick = "fontdropdown"
                fontdropdown.clickon(screen)
            elif shapedropdown.mainrect.collidepoint(mx,my) or (shapedropdown.menudown and shapedropdown.menurect.collidepoint(mx,my)):
                #if user clicks shape drop down menu
                lastclick = "shapedropdown"
                shapedropdown.clickon(screen)
            else:
                #if user doesn't click palette or canvas
                lastclick = "" #set last click to "" (which means everything except canvas and palette)
                screen.set_clip(canvas)
                currtool.outside() #runs current tool's outside function, as user clicked outside of canvas
                screen.set_clip(None)
                #following loop checks for tools and if we clicked them or not
                for b in palbuttons:
                    if b.istouch():
                        b.clickon(screen)
                for b in fontsizebuttons:
                    if b.istouch():
                        b.clickon(screen)
                for t in tools:
                    if t.istouch():
                        if t.func != currtool:
                            #if the tool button clicked is not the current tool button, it becomes unselected and the new one becomes selected
                            for t2 in tools:
                                if t2.func == currtool:
                                    t2.selected = False
                                    break
                            t.clickon(screen)
                            t.selected = True
                        break
            if lastclick != "fontdropdown":
                fontdropdown.menudown = False #turns off menu in fontdropdown if it was not clicked
            if lastclick != "shapedropdown":
                shapedropdown.menudown = False #turns off menu in shapedropdown if it was not clicked
        if e.type == MOUSEBUTTONUP:
            if lastclick == "canvas":
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
                    if loadname[-4:] == ".jpg":
                        ext = ""
                    else:
                        ext = ".jpg"
                    image.save(screen.copy().subsurface(canvas), loadname + ext)
                mouse.set_visible(False)   
            elif kp[K_o] and (kp[K_LCTRL] or kp[K_RCTRL]):
                #if user presses CTRL-O will open a file and paste it onto canvas
                if not canundo:
                    if type(currtool) == Select:
                        currtool.hasbox = False
                    elif type(currtool) == Text:
                        currtool.hastextbox = False

                loadname = filedialog.askopenfilename()
                mouse.set_visible(True)
                if loadname:
                    if loadname[-4:] in [".jpg",".png",".gif",".bmp"]:
                        if len(mem) < 256:
                            mem2 = []
                            mem.append(screen.copy())
                        if not kp[K_LSHIFT] and not kp[K_RSHIFT]:
                            draw.rect(screen,WHITE,canvas) #clears everything previously on the canvas if user does not hold shift
                        opened_image = image.load(loadname)
                        img_ratio = opened_image.get_width()/opened_image.get_height()
                        if opened_image.get_width() >= opened_image.get_height():
                            width = (min(opened_image.get_width(),800))
                            height = (int(width/img_ratio))
                        else:
                            height = (min(opened_image.get_height(),600))
                            width = (int(height*img_ratio))
                        screen.blit(transform.scale(opened_image,(width,height)),(300,50))
                    else:
                        print("Invalid image")
                mouse.set_visible(False)
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
    draw.rect(screen,PINK,(80,370,20,20))
    screen.blit(comicsans.render(str(textool.textbox.fontsize),True,BLACK),(80,370)) #draws fontsize for textbox
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
            screen.blit(currtool.selectedbox,(currtool.x,currtool.y))
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
quit()
        
