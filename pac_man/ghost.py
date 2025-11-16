import pygame
import os

pygame.init()
width = 900 + 450
rectsize = width / 30
blinky_list,pinky_list,clyde_list,inky_list,pac_list = [],[],[],[],[]
cartoon_list,ghost_scary_list = [],[]
newtime = 0 
lastime = 8500

class Blinky: 
    def __init__(self,image): #load the ghost iamge
        
        self.using = image
    def image_get(count,width,height):
        blinky = pygame.image.load(os.path.join("photo", f"blinky{count}.png"))
        blinky = pygame.transform.scale(blinky,(width,height))
        return blinky
    def clyde_get(count,width,height):
        clyde = pygame.image.load(os.path.join("photo",f"clyde{count}.png"))
        clyde = pygame.transform.scale(clyde,(width,height))
        return clyde
    def pinky_get(count,width,height):
        pinky = pygame.image.load(os.path.join("photo",f"pinky{count}.png"))
        pinky = pygame.transform.scale(pinky,(width,height))
        return pinky
    def inky_get(count,width,height):
        inky = pygame.image.load(os.path.join("photo",f"inky{count}.png"))
        inky = pygame.transform.scale(inky,(width,height))
        return inky
    def pac_man_get(count,width,height):
        pac_man = pygame.image.load(os.path.join("photo",f"imagepac{count}.png"))
        pac_man = pygame.transform.scale(pac_man,(width,height))
        return pac_man
        
    def cartoon_get(count,width,height):
        cartoon = pygame.image.load(os.path.join("photo\cartoon",f"1 ({count}).png"))
        cartoon = pygame.transform.scale(cartoon,(width,height))
        return cartoon 
    def ghost_scary(count,width,height):
        scary = pygame.image.load(os.path.join("photo",f"scary{count}.png"))
        scary = pygame.transform.scale(scary,(width,height))
        return scary
    
#save the cartoon image for list
for i in range(0,2):
    blinky_list.append(Blinky.image_get(i,rectsize,rectsize))
    clyde_list.append(Blinky.clyde_get(i,rectsize,rectsize))
    pinky_list.append(Blinky.pinky_get(i,rectsize+4,rectsize+5))
    inky_list.append(Blinky.inky_get(i,rectsize,rectsize))

for i in range(0,5):
    pac_list.append(Blinky.pac_man_get(i,rectsize,rectsize))
for i in range(0,4):
    ghost_scary_list.append(Blinky.ghost_scary(i,rectsize,rectsize))
#for i in range(1,707):
 #   cartoon_list.append(Blinky.cartoon_get(i,600,600))


#print(blinky_list,clyde_list,pinky_list,inky_list)


count = 0
cartoon_speed = 75 
running = True

