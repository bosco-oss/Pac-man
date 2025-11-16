import pygame
import sys
from pyvidplayer import Video
import random 
import os 
import math
import ghost

pygame.init()

width = 900
height = width + width * 0.09
rectsize = width / 30  #blocksize
speed = 1 # Pac-Man speed
pac_man_o = 0
FPS = 120 # fps

count,count2 = 0,120
newtime,lastime = 0,8500
blinky = 0
number = 0
radius1 = rectsize * 8
ban_number = [3,4,5,6,7,8,9]
ghost_scary_time = 0
cartoontime,cartoonlasttime,cartooncount = 0,10000,1
vid = Video("photo/Untitled video - Made with Clipchamp.mp4")
vid.set_size((width + 800,height - 30))
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pac-Man")

pac_man_speed,ghost_speed,ghost_speed_pinky,ghost_speed_inky,ghost_speed_cylde = 0.07,0.06,0.065,0.069,0.063

pac_man,detecpac = [2,2],[0,0] 
moving = [0, 0]  
newlist = [2,2]
control = [""]

blinky_location = [3,2]
blinky_moving = [3,2]
detec_list = [""]

pinky_location = [3,2]
pinky_movingg = [3,2]
pink_detec_list = [""]

clyde_location = [3,2]
clyde_movingg = [3,2]
clyde_detec_list = [""]

inky_location = [3,2]
inky_movingg = [3,2]
inky_detec_list = [""]

ghost_scary_mode = False

def fun(val):
    return val[1]

map = [
    [6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5],
    [3, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 3],
    [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
    [3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
    [3, 3, 2, 3, 0, 0, 3, 1, 3, 0, 0, 0, 3, 1, 3, 3, 1, 3, 0, 0, 0, 3, 1, 3, 0, 0, 3, 2, 3, 3],
    [3, 3, 1, 7, 4, 4, 8, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 7, 4, 4, 8, 1, 3, 3],
    [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
    [3, 3, 1, 6, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 5, 1, 3, 3],
    [3, 3, 1, 7, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 8, 1, 3, 3],
    [3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
    [3, 7, 4, 4, 4, 4, 5, 1, 3, 7, 4, 4, 5, 0, 3, 3, 0, 6, 4, 4, 8, 3, 1, 6, 4, 4, 4, 4, 8, 3],   
    [7, 4, 4, 4, 4, 5, 3, 1, 3, 6, 4, 4, 8, 0, 7, 8, 0, 7, 4, 4, 5, 3, 1, 3, 6, 4, 4, 4, 4, 8],
    [0, 0, 0, 0, 0, 3, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 3, 0, 0, 0, 0, 0],
    [4, 4, 4, 4, 4, 8, 3, 1, 3, 3, 0, 6, 4, 4, 9, 9, 4, 4, 5, 0, 3, 3, 1, 3, 7, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 5, 3, 1, 3, 3, 0, 7, 4, 4, 4, 4, 4, 4, 8, 0, 3, 3, 1, 3, 6, 4, 4, 4, 4, 4],
    [0, 0, 0, 0, 0, 3, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 3, 0, 0, 0, 0, 3],
    [6, 4, 4, 4, 4, 8, 3, 1, 3, 3, 0, 6, 4, 4, 4, 4, 4, 4, 5, 0, 3, 3, 1, 3, 7, 4, 4, 4, 4, 5],
    [3, 6, 4, 4, 4, 4, 8, 1, 7, 8, 0, 7, 4, 4, 5, 6, 4, 4, 8, 0, 7, 8, 1, 7, 4, 4, 4, 4, 5, 3],
    [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
    [3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
    [3, 3, 1, 7, 4, 5, 3, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 3, 6, 4, 8, 1, 3, 3],
    [3, 3, 2, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1,"u",1, 1,"u",1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 2, 3, 3],
    [3, 7, 4, 5, 1, 3, 3, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 3, 3, 1, 6, 4, 8, 3],
    [3, 6, 4, 8, 1, 7, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 8, 1, 7, 4, 5, 3],
    [3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
    [3, 3, 1, 6, 4, 4, 4, 4, 8, 7, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 8, 7, 4, 4, 4, 4, 5, 1, 3, 3],
    [3, 3, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 3, 3],
    [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
    [3, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 3],
    [7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8]
]
class calculator:   
    def blinky_moving(): #the map detec
        global ghost_scary_mode
        calculator_list = []
        if map[blinky_location[1]][blinky_location[0] + 1] not in ban_number and detec_list[0] != "left": 
            calculator_list.append(("right",abs((blinky_location[0] + 2 - newlist[0]) ** 2 + (blinky_location[1] - newlist[1]) ** 2)))
        if map[blinky_location[1]][blinky_location[0] - 1] not in ban_number  and detec_list[0] != "right":
            calculator_list.append(("left",abs((blinky_location[0] - 2 - newlist[0]) ** 2 + (blinky_location[1] - newlist[1]) ** 2)))
            #print("left")
        if map[blinky_location[1] + 1][blinky_location[0]] not in ban_number and detec_list[0] != "up": 
            calculator_list.append(("down",abs((blinky_location[0] - newlist[0]) ** 2 + (blinky_location[1] + 2 - newlist[1]) ** 2)))
            #print("down")
        if map[blinky_location[1] - 1][blinky_location[0]] not in ban_number + ["u"] and map[blinky_location[1]][blinky_location[0]] != "u" and detec_list[0] != "down":
            calculator_list.append(("up",abs((blinky_location[0] - newlist[0]) ** 2 + (blinky_location[1] - 2 - newlist[1]) ** 2)))

            #print("up")
        if ghost_scary_mode == 0:calculator_list.sort(key = fun)
        else:calculator_list = [random.choice(calculator_list)]
        #print(calculator_list)
        if blinky_moving[0] < blinky_location[0]:  #follow the  block
            blinky_moving[0] += ghost_speed
            if blinky_moving[0] + ghost_speed > blinky_location[0]:
                blinky_moving[0] = math.ceil(blinky_moving[0]) 
        if blinky_moving[0] > blinky_location[0]:
            blinky_moving[0] -= ghost_speed
            if blinky_moving[0] - ghost_speed < blinky_location[0]:
                blinky_moving[0] = int(blinky_moving[0]) 
        if blinky_moving[1] < blinky_location[1]:
            blinky_moving[1] += ghost_speed
            if blinky_moving[1] + ghost_speed > blinky_location[1]:
                blinky_moving[1] = math.ceil(blinky_moving[1]) 
        if blinky_moving[1] > blinky_location[1]:
            blinky_moving[1] -= ghost_speed
            if blinky_moving[1] - ghost_speed < blinky_location[1]:
                   blinky_moving[1] = int(blinky_moving[1]) 
                
        if blinky_moving == blinky_location: #trunning and save the direction
            if calculator_list[0][0] == "right":
                    blinky_location[0] += 1
                    detec_list[0] = "right"
            if calculator_list[0][0] == "left":
                    blinky_location[0] -= 1
                    detec_list[0] = "left"
            if calculator_list[0][0] == "down":
                    blinky_location[1] += 1
                    detec_list[0] = "down"
            if calculator_list[0][0] == "up":
                    blinky_location[1] -= 1
                    detec_list[0] = "up"
    def pinky_moving():
        calculator_list = [] 
        mathusingx = 0
        mathusingy = 0
        if moving == [-speed,0]:
            mathusingx = -4
            mathusingy = 0
        if moving == [speed,0]: 
            mathusingx = 4
            mathusingy = 0
        if moving == [0,speed]:
            mathusingy = 4
            mathusingx = -4
        if moving == [0,-speed]: 
            mathusingy = -4
            mathusingx = 0
        if map[pinky_location[1]][pinky_location[0] + 1] not in ban_number and pink_detec_list[0] != "left": 
            #print("right")
            calculator_list.append(("right",abs((pinky_location[0] + 2 - (newlist[0] + mathusingx)) ** 2 + (pinky_location[1] - (newlist[1] + mathusingy)) ** 2)))
        if map[pinky_location[1]][pinky_location[0] - 1] not in ban_number  and pink_detec_list[0] != "right":
            calculator_list.append(("left",abs((pinky_location[0] - 2 - (newlist[0] + mathusingx)) ** 2 + (pinky_location[1] - (newlist[1] + mathusingy)) ** 2)))
           #print("left")
        if map[pinky_location[1] + 1][pinky_location[0]] not in ban_number and pink_detec_list[0] != "up": 
            calculator_list.append(("down",abs((pinky_location[0] - (newlist[0] + mathusingx)) ** 2 + (pinky_location[1] + 2 - (newlist[1] + mathusingy)) ** 2)))
            #print("down")aa
        if map[pinky_location[1] - 1][pinky_location[0]] not in ban_number + ["u"] and pink_detec_list[0] != "down":
            calculator_list.append(("up",abs((pinky_location[0] - (newlist[0] + mathusingx)) ** 2 + (pinky_location[1] - 2 - (newlist[1] + mathusingy)) ** 2)))
            #print("up")
        if ghost_scary_mode == 0:calculator_list.sort(key = fun)
        else:calculator_list = [random.choice(calculator_list)]
        #print(calculator_list)
        if pinky_movingg[0] < pinky_location[0]:
            pinky_movingg[0] += ghost_speed_pinky
            if pinky_movingg[0] + ghost_speed_pinky > pinky_location[0]:
                pinky_movingg[0] = math.ceil(pinky_movingg[0]) 
        if pinky_movingg[0] > pinky_location[0]:
            pinky_movingg[0] -= ghost_speed_pinky
            if pinky_movingg[0] - ghost_speed_pinky < pinky_location[0]:
                pinky_movingg[0] = int(pinky_movingg[0]) 
        if pinky_movingg[1] < pinky_location[1]:
            pinky_movingg[1] += ghost_speed_pinky
            if pinky_movingg[1] + ghost_speed_pinky > pinky_location[1]:
                pinky_movingg[1] = math.ceil(pinky_movingg[1]) 
        if pinky_movingg[1] > pinky_location[1]:
            pinky_movingg[1] -= ghost_speed_pinky
            if pinky_movingg[1] - ghost_speed_pinky < pinky_location[1]:
                pinky_movingg[1] = int(pinky_movingg[1]) 
                
        if pinky_movingg == pinky_location: 
            if calculator_list[0][0] == "right":
                pinky_location[0] += 1
                pink_detec_list[0] = "right"
            if calculator_list[0][0] == "left":
                pinky_location[0] -= 1
                pink_detec_list[0] = "left"
            if calculator_list[0][0] == "down":
                pinky_location[1] += 1
                pink_detec_list[0] = "down"

            if calculator_list[0][0] == "up":
                pinky_location[1] -= 1
                pink_detec_list[0] = "up"
        #print(mathusingx,mathusingy)f                   
    def clyde_moving(): #the map detec
        pygame.draw.circle(screen,(255,255,255),(pac_man[0] * rectsize + rectsize / 2,pac_man[1] * rectsize + rectsize / 2),radius1,4)
        
        calculator_list = [] 
        location = []
        if(((pac_man[0] - clyde_movingg[0]) ** 2) + ((pac_man[1] - clyde_movingg[1]) ** 2)) < 18:
            location = [0,21]
            #print("hi")
        else:
            location = newlist 
            #print("lose")

        if map[clyde_location[1]][clyde_location [0] + 1] not in ban_number and clyde_detec_list[0] != "left": 
            #print("right")
            calculator_list.append(("right",abs((clyde_location[0] + 2 -  location[0]) ** 2 + (clyde_location[1] -  location[1]) ** 2)))
        if map[clyde_location [1]][clyde_location[0] - 1] not in ban_number  and clyde_detec_list[0] != "right":
            calculator_list.append(("left",abs((clyde_location[0] - 2 -  location[0]) ** 2 + (clyde_location[1] -  location[1]) ** 2)))
            #print("left")
        if map[clyde_location[1] + 1][clyde_location[0]] not in ban_number and clyde_detec_list[0] != "up": 
            calculator_list.append(("down",abs((clyde_location[0] - location[0]) ** 2 + (clyde_location[1] + 2 -  location[1]) ** 2)))
            #print("down")
        if map[clyde_location[1] - 1][clyde_location[0]] not in ban_number + ["u"] and clyde_detec_list[0] != "down":
            calculator_list.append(("up",abs((clyde_location[0] -  location[0]) ** 2 + (clyde_location[1] - 2 -  location[1]) ** 2)))
            #print("up")
        if ghost_scary_mode == 0:calculator_list.sort(key = fun)
        else:calculator_list = [random.choice(calculator_list)]
        #print(calculator_list)
        if clyde_movingg[0] < clyde_location[0]:  #follow the  block
            clyde_movingg[0] += ghost_speed_cylde
            if clyde_movingg[0] + ghost_speed_cylde > clyde_location[0]:
                clyde_movingg[0] = math.ceil(clyde_movingg[0]) 
        if clyde_movingg[0] > clyde_location[0]:
            clyde_movingg[0] -= ghost_speed_cylde
            if clyde_movingg[0] - ghost_speed_cylde < clyde_location[0]:
                clyde_movingg[0] = int(clyde_movingg[0]) 
        if clyde_movingg[1] < clyde_location[1]:
            clyde_movingg[1] += ghost_speed_cylde
            if clyde_movingg[1] + ghost_speed_cylde > clyde_location[1]:
                clyde_movingg[1] = math.ceil(clyde_movingg[1]) 
        if clyde_movingg[1] > clyde_location[1]:
            clyde_movingg[1] -= ghost_speed_cylde
            if clyde_movingg[1] - ghost_speed_cylde < clyde_location[1]:
                   clyde_movingg[1] = int(clyde_movingg[1]) 
                
        if clyde_movingg == clyde_location: #trunning and save the direction
            if calculator_list[0][0] == "right":
                    clyde_location[0] += 1
                    clyde_detec_list[0] = "right"
            if calculator_list[0][0] == "left":
                    clyde_location[0] -= 1
                    clyde_detec_list[0] = "left"
            if calculator_list[0][0] == "down":
                    clyde_location[1] += 1
                    clyde_detec_list[0] = "down"
            if calculator_list[0][0] == "up":
                    clyde_location[1] -= 1
                    clyde_detec_list[0] = "up"
    def inky_moving(): #the map detec
        calculator_list = [] 
        mathusingx,mathusingy = 0,0

        if moving == [-speed,0]:
            mathusingx = newlist[0] - 2 
            mathusingy = newlist[1]
        if moving == [speed,0]: 
            mathusingx = newlist[0] + 2 
            mathusingy = newlist[1]
        if moving == [0,speed]:
            mathusingx = newlist[0] 
            mathusingy = newlist[1] + 2 
        if moving == [0,-speed]: 
            mathusingx = newlist[0] - 2
            mathusingy = newlist[1] - 2 
        pygame.draw.rect(screen,"white",[mathusingx * rectsize,mathusingy * rectsize,rectsize,rectsize])
        mathusingx = mathusingx + mathusingx - blinky_location[0]
        mathusingy =  mathusingy + mathusingy - blinky_location[1]
        pygame.draw.rect(screen,'white',[mathusingx * rectsize,mathusingy * rectsize,rectsize,rectsize])

        pygame.draw.line(screen,(255,255,255),[mathusingx * rectsize,mathusingy * rectsize],[blinky_location[0] * rectsize,blinky_location[1]*rectsize],5)
        #print(abs(mathusingx),abs(mathusingy))
        
        if map[inky_location[1]][inky_location[0] + 1] not in ban_number and inky_detec_list[0] != "left": 
            #print("right")
            calculator_list.append(("right",((inky_location[0] + 2 -  mathusingx) ** 2 + (inky_location[1] -  mathusingy) ** 2)))
        if map[inky_location[1]][inky_location[0] - 1] not in ban_number  and inky_detec_list[0] != "right":
            calculator_list.append(("left",((inky_location[0] - 2 - mathusingx) ** 2 + (inky_location[1] -  mathusingy) ** 2)))
           #print("left")
        if map[inky_location[1] + 1][inky_location[0]] not in ban_number and inky_detec_list[0] != "up": 
            calculator_list.append(("down",((inky_location[0] -  mathusingx) ** 2 + (inky_location[1] + 2 -  mathusingy) ** 2)))
            #print("down")
        if map[inky_location[1] - 1][inky_location[0]] not in ban_number and inky_detec_list[0] != "down":
            calculator_list.append(("up",((inky_location[0] -  mathusingx) ** 2 + (inky_location[1] - 2 -  mathusingy) ** 2)))
            #print("up")
        if ghost_scary_mode == 0:calculator_list.sort(key = fun)
        else:calculator_list = [random.choice(calculator_list)]
        #print(calculator_list)

        if inky_movingg[0] < inky_location[0]:
            inky_movingg[0] += ghost_speed_inky
            if inky_movingg[0] + ghost_speed_inky > inky_location[0]:
                inky_movingg[0] = math.ceil(inky_movingg[0]) 
        if inky_movingg[0] > inky_location[0]:
            inky_movingg[0] -= ghost_speed_inky
            if inky_movingg[0] - ghost_speed_inky < inky_location[0]:
                inky_movingg[0] = int(inky_movingg[0]) 
        if inky_movingg[1] < inky_location[1]:
            inky_movingg[1] += ghost_speed_inky
            if inky_movingg[1] + ghost_speed_inky > inky_location[1]:
                inky_movingg[1] = math.ceil(inky_movingg[1]) 
        if inky_movingg[1] > inky_location[1]:
            inky_movingg[1] -= ghost_speed_inky
            if inky_movingg[1] - ghost_speed_inky < inky_location[1]:
                inky_movingg[1] = int(inky_movingg[1]) 
                 
        if inky_movingg == inky_location: 
            if calculator_list[0][0] == "right":
                inky_location[0] += 1
                inky_detec_list[0] = "right"
            if calculator_list[0][0] == "left":
                inky_location[0] -= 1
                inky_detec_list[0] = "left"
            if calculator_list[0][0] == "down":
                inky_location[1] += 1
                inky_detec_list[0] = "down"

            if calculator_list[0][0] == "up":
                inky_location[1] -= 1
                inky_detec_list[0] = "up"
            

clock = pygame.time.Clock()
cartoon = True
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: 
            cartoon = False   
    if cartoon:
        vid.draw(screen,(-250,10))
        pygame.display.update()
    
    if cartoon == False:
        key = pygame.key.get_pressed() # control pac man 
        
        if key[pygame.K_a]:
            control[0] = "left"
            x = newlist[0] - speed 
            y = newlist[1]
            if map[y][x] not in ban_number:
                pac_man_o = 180
                moving = [-speed, 0] 
        
        elif key[pygame.K_d]:
            control[0] = "right"
            x = newlist[0] + speed 
            y = newlist[1]
            if map[y][x] not in ban_number:
                pac_man_o = 360
                moving = [speed, 0]
        
        elif key[pygame.K_w]:
            control[0] = "up"
            y = newlist[1] - speed 
            x = newlist[0]
            if map[y][x] not in ban_number:
                pac_man_o = 90
                moving = [0, -speed]

        elif key[pygame.K_s]: 
            control[0] = "down"
            y = newlist[1] + speed 
            x = newlist[0]
            if map[y][x] not in ban_number:
                pac_man_o = -90
                moving = [0, speed]

        
        newx = newlist[0] + moving[0] #calculator
        newy = newlist[1] + moving[1] 
        
        if map[newy][newx] not in ban_number:
            if pac_man == newlist:
                newlist[0] = newx
                newlist[1] = newy
                map[newy][newx] = 0

        
        if pac_man != newlist: #pac man moving
            number += 0.19
            if pac_man[0] < newlist[0]:
                pac_man[0] += pac_man_speed 
                if pac_man[0] + pac_man_speed > newlist[0]:
                    pac_man[0] = math.ceil(pac_man[0]) 
            
            if pac_man[0] > newlist[0]:
                pac_man[0] -= pac_man_speed
                if pac_man[0] -  pac_man_speed < newlist[0]:
                    pac_man[0] = int(pac_man[0]) 
            
            if pac_man[1] < newlist[1]:
                pac_man[1] += pac_man_speed
                if pac_man[1] + pac_man_speed > newlist[1]:
                    pac_man[1] = math.ceil(pac_man[1]) 
                    
            if pac_man[1] > newlist[1]:
                pac_man[1] -= pac_man_speed
                if pac_man[1] - pac_man_speed < newlist[1]:
                    pac_man[1] = int(pac_man[1])
            #print(pac_man,newlist)
        if map[newy][newx] == 2:
                ghost_scary_mode = True
                ghost_scary_time = 12000
        if ghost_scary_time <= 0:
            ghost_scary_mode = False
        if ghost_scary_mode:
            ghost_scary_time -= 10
            print("mode_on")
            
    # if map location in 2 ,2 change 3 (3 = draw the normal block
        color = (22,53,234)
        food_color = (254,184,151)
        PI = math.pi
        screen.fill("black")
        if count2 >= 1200: # save the timer number
            count2 = 240
            count = 240
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == 1:
                    pygame.draw.circle(screen, food_color, (j * rectsize + (0.5 * rectsize), i * rectsize + (0.5 * rectsize)), 4)
                if map[i][j] == 2:
                    if count >= count2 and count <= count2 + 120: 
                        pygame.draw.circle(screen, food_color, (j * rectsize + (0.5 * rectsize), i * rectsize + (0.5 * rectsize)), 10)
                if map[i][j] == "u":
                    pygame.draw.circle(screen, food_color, (j * rectsize + (0.5 * rectsize), i * rectsize + (0.5 * rectsize)), 4)
                if map[i][j] == 3:
                    pygame.draw.line(screen, color , (j * rectsize + (0.5 * rectsize), i * rectsize),
                                    (j * rectsize + (0.5 * rectsize), i * rectsize + rectsize), 3)
                if map[i][j] == 4:
                    pygame.draw.line(screen, color, (j * rectsize, i * rectsize + (0.5 * rectsize)),
                                    (j * rectsize + rectsize, i * rectsize + (0.5 * rectsize)), 3)
                if map[i][j] == 5:
                    pygame.draw.arc(screen, color, [(j * rectsize - (rectsize * 0.4)) - 2, (i * rectsize + (0.5 * rectsize)), rectsize, rectsize],
                                    0, PI / 2, 3)
                if map[i][j] == 6:
                    pygame.draw.arc(screen, color,
                                    [(j * rectsize + (rectsize * 0.5)), (i * rectsize + (0.5 * rectsize)), rectsize, rectsize], PI / 2, PI, 3)
                if map[i][j] == 7:
                    pygame.draw.arc(screen, color, [(j * rectsize + (rectsize * 0.5)), (i * rectsize - (0.4 * rectsize)), rectsize, rectsize], PI,
                                    3 * PI / 2, 3)
                if map[i][j] == 8:
                    pygame.draw.arc(screen, color,
                                    [(j * rectsize - (rectsize * 0.4)) - 2, (i * rectsize - (0.4 * rectsize)), rectsize, rectsize], 3 * PI / 2,
                                    2 * PI, 3)
                if map[i][j] == 9:
                    pygame.draw.line(screen, 'white', (j * rectsize, i * rectsize + (0.5 * rectsize)),
                                    (j * rectsize + rectsize, i * rectsize + (0.5 * rectsize)), 3)

                    #change the bigsteak for timer
        #steak spawn calculator
        if ghost_scary_mode:
            if ghost_scary_time < 3200:
                ghost_catoon = 4
        else:ghost_catoon = 2
        if count == count2 + 240:
            count2 += 240
        count += 8

        #print(newlist,pac_man)
        if lastime > 60000: 
            lastime = 8500            
            newtime = 0    
        #cartoon update
        if newtime >= lastime:
            blinky += 1
            if blinky >= ghost_catoon:
                blinky = 0
        # the calculator time
        if newtime >= lastime:
            lastime += 8500
        newtime += 600

        
        #print(blinky_location) 
        if round(number) >= len(ghost.pac_list):
            number = 0
        """""""""""""""""""""
        if pac_man[0] == blinky_moving[0] or pac_man[1] == blinky_moving[1]:
            if abs(pac_man[0] - blinky_moving[0] + pac_man[1] - blinky_moving[1]) < 1:
                print("lost")
        if pac_man[0] == clyde_movingg[0] or pac_man[1] == clyde_movingg[1]:
            if abs(pac_man[0] - clyde_movingg[0] + pac_man[1] - clyde_movingg[1]) < 1:
                print("lost")

        if pac_man[0] == pinky_movingg[0] or pac_man[1] == pinky_movingg[1]:
            if abs(pac_man[0] - pinky_movingg[0] + pac_man[1] - pinky_movingg[1]) < 1:
                print("lost")

        if pac_man[0] == inky_movingg[0] or pac_man[1] == inky_movingg[1]:
            if abs(pac_man[0] - inky_movingg[0] + pac_man[1] - inky_movingg[1]) < 1:
                print("lost")

        
        else:
            print("nothing")
        """""""""""""""""""""""
        #print(pac_man,blinky_moving)
            
            
        
        #print(lastime,newtime)
        
        #draw ghost
        calculator.blinky_moving() 
        calculator.pinky_moving()
        calculator.clyde_moving()
        calculator.inky_moving()
        if not ghost_scary_mode:
            if blinky >= 2:blinky = 1

            screen.blit(ghost.blinky_list[blinky],(blinky_moving[0] * rectsize - 5,blinky_moving[1] * rectsize - 5))
            screen.blit(ghost.pinky_list[blinky],(pinky_movingg[0] * rectsize - 5,pinky_movingg[1] * rectsize - 5))
            screen.blit(ghost.clyde_list[blinky],(clyde_movingg[0] * rectsize - 5 ,clyde_movingg[1] * rectsize - 5 ))
            screen.blit(ghost.inky_list[blinky],(inky_movingg[0] * rectsize - 5,inky_movingg[1] * rectsize - 5))
        else:
            screen.blit(ghost.ghost_scary_list[blinky],(blinky_moving[0] * rectsize - 5,blinky_moving[1] * rectsize - 5))
            screen.blit(ghost.ghost_scary_list[blinky],(pinky_movingg[0] * rectsize - 5,pinky_movingg[1] * rectsize - 5))
            screen.blit(ghost.ghost_scary_list[blinky],(clyde_movingg[0] * rectsize - 5 ,clyde_movingg[1] * rectsize - 5 ))
            screen.blit(ghost.ghost_scary_list[blinky],(inky_movingg[0] * rectsize - 5,inky_movingg[1] * rectsize - 5))
        # draw Pac-Man
        rotated_image = pygame.transform.rotate(ghost.pac_list[round(number)], pac_man_o)

        # Blit the rotated image onto the screen
        screen.blit(rotated_image, (pac_man[0] * rectsize - 5, pac_man[1] * rectsize - 5))
        # update scream
        pygame.display.flip()
        
        clock.tick(FPS)
#quit Pygame
pygame.quit()
sys.exit()