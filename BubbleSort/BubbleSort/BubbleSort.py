import pygame
from sys import exit
import time




myList = [77,31,67,3,60]
num=len(myList)
pygame.init()
pygame.font.init()
windowDemoWidth = 700
WindowCodeWidth =300
windowHeight = 800
blockWidth = windowDemoWidth//len(myList)
screen = pygame.display.set_mode((windowDemoWidth+WindowCodeWidth, windowHeight))
screen.fill((0, 0, 0))
pygame.display.set_caption("Bubble Sort")
pygame.draw.rect(screen, (255,0,255), (windowDemoWidth, 0, WindowCodeWidth, windowHeight), 2) 
#fontNew=pygame.font.Font.set_bold(None,True)#font and size
font=pygame.font.Font(None,20)#font and size

code = [
        "temp=0",
        "def bubbleSort(list):",
        "        for i in range(len(list)):",
        "                for j in range(len(list)-1):",
        "                       if list[j]>list[j+1]:",
        "                             temp=list[j]",
        "                             list[j]=list[j+1]",
        "                             list[j+1]=temp"
        ]

def delay():
    time.sleep(1)

colorStack = {}



def draw_String(row:int, codeLine:str,color,addColor:bool):
    if addColor == True:
        if not colorStack.get(row)  :
            colorStack[row] = []
        colorStack[row].append(color)        
        screen.blit(font.render(codeLine, True, color), (windowDemoWidth+2, row*20)) 
    else:
        if colorStack[row] :
            colorStack[row].pop()   
        if colorStack[row] :
            screen.blit(font.render(codeLine, True, colorStack[row][0] ), (windowDemoWidth+2, row*20)) 
        else:
            screen.blit(font.render(codeLine, True, (0,0,255) ), (windowDemoWidth+2, row*20)) 
    
def draw_rect(x:int, y:int, width:int, number:int, oldNum:int, lastPlace:bool):
    if(lastPlace == False):
        pygame.draw.rect(screen, (0,0,255), (x, y, width, 40), 2)
        screen.blit(font.render(str(number), True, (255,255,255)), (x+width//2-15, y+10))        
        pygame.display.update()
        pygame.display.flip()
    else:
        screen.blit(font.render(str(oldNum), True, (0,0,0)), (x+width//2-15, y+10))
        screen.blit(font.render(str(number), True, (255,255,255)), (x+width//2-15, y+10))        
        pygame.display.update()
        pygame.display.flip()



def bubbleSort(myList):
    
    temp=0
    jtemp=0 # maintaining j loop last value
    boxSize=(windowDemoWidth-100)/3
    spaceSize=100/2
    for n in range(num):
        draw_rect(n*blockWidth,0,blockWidth,myList[n],0,False)
    time.sleep(0.1)
    
    for n in range(num):     
        draw_rect(n*blockWidth,40,blockWidth,myList[n],0,False)
    time.sleep(1)
    for x in range(0,3):
        draw_rect(x*boxSize+(x*spaceSize),80,boxSize,0,0,False)
    time.sleep(1)
    for i in range (num-1):

        if i > 0:
            draw_rect(0,80,boxSize,i,i-1,True) 
            time.sleep(2)

        for j in range(num-1-i):
            
            pygame.draw.rect(screen, (255,0,255), (j*blockWidth, 40, blockWidth*2, 40), 2) 
            time.sleep(2)
            draw_rect(boxSize+spaceSize,80,boxSize,j,jtemp,True)
            jtemp = j
            #pygame.draw.rect(screen, (255,0,255), ((j+1)*blockWidth, 40, blockWidth, 40), 2) 
            
            if myList[j]>myList[j+1]:
                time.sleep(1)
                draw_rect(2*boxSize+2*spaceSize,80,boxSize,myList[j],temp,True)
                temp=myList[j]
                time.sleep(2)
                
                draw_rect(j*blockWidth,40,blockWidth,myList[j+1],myList[j],True)
                myList[j]=myList[j+1]               
                draw_rect((j+1)*blockWidth,40,blockWidth,temp,myList[j+1],True)
                  
                myList[j+1]=temp
                
            pygame.draw.rect(screen, (0,0,255), (j*blockWidth, 40, blockWidth*2, 40), 2)
            #pygame.draw.rect(screen, (0,0,255), ((j-1)*blockWidth, 40, blockWidth, 40), 2)
    
    #time.sleep(2)                





    
    
bubbleSort(myList)
time.sleep(10)
pygame.quit()
exit()
 






