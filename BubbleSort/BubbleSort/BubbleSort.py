import pygame
from sys import exit
import time

myList = [23,45,3,78,12,45,34]
order = 'descending'
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
        "   for i in range(len(list)):",
        "       for j in range(len(list)-1):",
        "           if list[j]>list[j+1]:",
        "               temp=list[j]",
        "               list[j]=list[j+1]",
        "               list[j+1]=temp"
        ]

def delay():
    time.sleep(.1)

def compare(a:int, b:int, ascending:bool):
    if(ascending):
        return a>b
    else:    
        return a<b

def draw_String(row:int, codeLine:int, addColour):
    if addColour==True:
        colour=(255,0,0)
    else:
        colour=(0,0,255)

    screen.blit(font.render(codeLine,True,colour),(windowDemoWidth+2, row*20))

for x in range(len(code)):
    draw_String(x,code[x],False)

"""
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
   """ 
def draw_rect(x:int, y:int, width:int, number:int, oldNum:int, lastPlace:bool):
    if(lastPlace == False):
        pygame.draw.rect(screen, (0,0,255), (x, y, width, 40), 2)
        screen.blit(font.render(str(number), True, (255,0,255)), (x+width//2-15, y+10))        
        pygame.display.update()
        pygame.display.flip()
    else:
        screen.blit(font.render(str(oldNum), True, (0,0,0)), (x+width//2-15, y+10))
        screen.blit(font.render(str(number), True, (255,255,255)), (x+width//2-15, y+10))        
        pygame.display.update()
        pygame.display.flip()



def bubbleSort(myList):
    delay()
    draw_String(0,code[0],True)
    delay()
    draw_String(1,code[1],True)
    temp=0
    jtemp=0 # maintaining j loop last value
    boxSize=(windowDemoWidth-100)/3
    spaceSize=100/2
    screen.blit(font.render("Given List",True,(255,0,0)),(2, 2))
    for n in range(num):
        draw_rect(n*blockWidth,22,blockWidth,myList[n],0,False)
    delay()
    screen.blit(font.render("Ordering List",True,(255,0,0)),(2, 62))
    for n in range(num):     
        draw_rect(n*blockWidth,84,blockWidth,myList[n],0,False)
    delay()
    screen.blit(font.render("i",True,(255,0,0)),(boxSize/2, 126))
    screen.blit(font.render("j",True,(255,0,0)),(boxSize+spaceSize+boxSize/2, 126))
    screen.blit(font.render("temp",True,(255,0,0)),((boxSize+spaceSize)*2, 126))
    for x in range(0,3):
        draw_rect(x*boxSize+(x*spaceSize),148,boxSize,0,0,False)
    delay()
    for i in range (num-1):
        draw_String(2,code[2],True)
        draw_String(3,code[3],False)
        time.sleep(2)
        if i > 0:
            draw_rect(0,148,boxSize,i,i-1,True) 
            time.sleep(2)

        for j in range(num-1-i):
            time.sleep(1)
            draw_String(3,code[3],True)
            
            pygame.draw.rect(screen, (255,0,255), (j*blockWidth, 84, blockWidth*2, 40), 2) 
            time.sleep(2)
            draw_rect(boxSize+spaceSize,148,boxSize,j,jtemp,True)
            jtemp = j
            #pygame.draw.rect(screen, (255,0,255), ((j+1)*blockWidth, 40, blockWidth, 40), 2) 
            '''if order=="ascending":

                if myList[j]>myList[j+1]:
                    time.sleep(1)
                    a=True
            else:
                if myList[j]<myList[j+1]:
                    time.sleep(1)
                    a=True
            if a==True: '''
            if(compare(myList[j],myList[j+1],order=="ascending")):
                time.sleep(1)
                draw_rect(2*boxSize+2*spaceSize,148,boxSize,myList[j],temp,True)
                draw_String(4,code[4],True)
                temp=myList[j]
                #draw_String(5,code[5],True)
                time.sleep(2)                
                draw_rect(j*blockWidth,84,blockWidth,myList[j+1],myList[j],True)
                draw_String(5,code[5],True)
                myList[j]=myList[j+1]   
                #draw_String(6,code[6],True)
                draw_rect((j+1)*blockWidth,84,blockWidth,temp,myList[j+1],True)
                draw_String(6,code[6],True)
                myList[j+1]=temp
                draw_String(5,code[5],False)
                draw_String(7,code[7],True) 

                    
            pygame.draw.rect(screen, (0,0,255), (j*blockWidth, 84, blockWidth*2, 40), 2)
            #pygame.draw.rect(screen, (0,0,255), ((j-1)*blockWidth, 40, blockWidth, 40), 2)
    
    #time.sleep(2)                




bubbleSort(myList)
time.sleep(10)
pygame.quit()
exit()
 






