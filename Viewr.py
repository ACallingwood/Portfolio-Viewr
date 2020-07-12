# Sys Config and Window Size
import pygame
Title = "Viewr"
pygame.init()
X = 960
Y = 540
black = (0,0,0)
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128)
# Set Display 
display = pygame.display.set_mode((X, Y )) 
pygame.display.set_caption(Title)

# Fonts and Font Sizes / Labeling font/file calls
Headerfont = pygame.font.Font('freesansbold.ttf', 20)
Regfont = pygame.font.Font('freesansbold.ttf', 14)
headertext = Headerfont.render("Welcome to "+ Title, True, white)
cycle = 0
textRect = headertext.get_rect()
callfile = pygame.image.load
banner = callfile("banner1.png").convert_alpha()
contact = "Viewr by Amber. R. Collinsworth"
maincontact = contact
# Define Artwork params
class file():
    def __init__(self, filename,artname,creation,notes):
        self.filename = filename
        self.artname = artname
        self.creation = creation
        self.notes = notes



"""
About the Artist / Files list
"""
def artist():
    global cycle
    global contact
    global headertext
    global cycle
    artist = "Artist: Jessica Colyer"
    
    if cycle == 0:
        headertext = Headerfont.render("Welcome to "+ Title, True, white)
        contact = maincontact
    else: 
         headertext = Headerfont.render(artist, True, white)
         contact = "https://colyerjessica.weebly.com/gallery.html"
    
cover = file("ACViewrCover.png", "Artwork showcased with Python","Alpha Ver. 01.01.2020", "You may swap images by clicking the 'left' or 'right' keys on your keyboard.")
# Other file names for my future use
# ACViewrCover.png
# "sky.png"
                   # File Name           # Artwork Name         # Creation Date         #Notes
f1	=file(	"f7712782.png"	,	"Concept and Design"	,"2017 Demo work"	,"Shading, concept, and color")
f2	=file(	"p6389469.jpg"	,	"Ace Maker",     	"2016"	,	        "Photography")
f3	=file(	"p6848937.jpg"	,	"Morning Bird",	        "2015"	,	        "Photography")
f4	=file(	"p9075815.jpg"	,	"Butterfly",	        "2018"	,	        "Photography")
f5	=file(	"pse1794917.jpg"	,"Humming Bird",	"2015"	,	        "Photography")
f6	=file(	"pse3008986.jpg"	,"Highlight- AM",	"2013"	,	        "Digital Design")
f7	=file(	"pse6183376.jpg"	,"Line work- AM",	"2013"	,	        "Digital Design")


flist = [cover,f1,f2,f3,f4,f5,f6,f7]


"""
Internal Functions
"""

# Check and Update the Cycle to Loop
def checkcy():
    global cycle
    if cycle == len(flist):
        cycle = 1
    elif cycle == -len(flist):
        cycle = len(flist)




# Updates the variables that the textboses use based on current cycle 
def findnotes():
    global filename
    global artname
    global creation
    global notes
    global cycle
    global image
    global headertext
    checkcy()
    
    filename = (flist[cycle].filename)
    artname = (flist[cycle].artname)
    creation = (flist[cycle].creation)
    notes = (flist[cycle].notes)
    image = callfile(filename).convert_alpha()
                


# Updates the new variables to the display
def textdisp():
    global nametext
    global creationtext
    global contacttext
    global notestext
    #Font set
    nametext = Regfont.render(artname, True, white)
    creationtext = Regfont.render(creation, True, white)
    contacttext = Regfont.render(contact, True, white)
    notestext = Regfont.render(notes, True, white)

    # notes text location
    display.blit(banner,(335,400)) # Red/black banner behind text 
    display.blit(headertext, textRect) 
    textRect.center = (X-450, Y // 5+351) # Header text location    
    display.blit(nametext, textRect) 
    textRect.center = (X-450, Y // 5+371) # artname text location
    display.blit(creationtext, textRect)
    textRect.center = (X-450, Y // 5+400) # creation text location    
    display.blit(contacttext, textRect)
    textRect.center = (X-450, Y // 5+421) # contact text location    
    display.blit(notestext, textRect) 
    textRect.center = (X-170, Y // 5+351)

    
"""
End of Internal functions and set up - Pygame starts here
"""


launch = True
print(str(len(flist))+ " Images loaded")

while launch:
    checkcy()
    # Background and window format
    findnotes()
    textdisp()
    display.fill(black)
    display.blit(image,(0,0)) # Visual image
    textdisp()

    for event in pygame.event.get() :


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:                
                cycle = cycle+1
                checkcy()


                
                artist()
                print("Vewing image " + str(cycle))

                
            elif event.key == pygame.K_LEFT:
                checkcy()
                cycle = cycle -1 
                artist()
                print("Vewing image " + str(cycle))


            
        elif event.type == pygame.QUIT : 
            pygame.quit() 
            quit() 

    #display.blit(image(0,0))
    #display.blit(headertext, textRect)
    #textRect.center = (X // 2, Y // 5+300) 

        # Refresh Screen   
    pygame.display.update()  


