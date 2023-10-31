from tokenize import String
from xmlrpc.client import Boolean, boolean
import pygame
from pygame.locals import *
import time
from sys import exit

myList = [3,4,5]
pygame.init()
pygame.font.init()
windowDemoWidth = 700
WindowCodeWidth =300
windowHeight = 800
blockWidth = windowDemoWidth//len(myList)
recursionCount:int = 0
screen = pygame.display.set_mode((windowDemoWidth+WindowCodeWidth, windowHeight))
pygame.display.set_caption("Mergesort")
pygame.draw.rect(screen, (255,0,255), (windowDemoWidth, 0, WindowCodeWidth, windowHeight), 2)#################    
font=pygame.font.Font(None,20)#font and size

code = [
        "def mergeSort(myList):",
        "    if len(myList) > 1:",
        "        mid = len(myList) // 2",
        "        left = myList[:mid]",
        "        right = myList[mid:]",
        "        # Recursive call on each half",
        "        mergeSort(left)",
        "        mergeSort(right)",
        "        # Two iterators for traversing the two halves",
        "        i = 0",
        "        j = 0",
        "        # Iterator for the main list",
        "        k = 0 ",
        "        while i < len(left) and j < len(right):",
        "            if left[i] <= right[j]:",
        "              # The value from the left half has been used",
        "              myList[k] = left[i]",
        "              # Move the iterator forward",
        "              i += 1",
        "            else:",
        "                myList[k] = right[j]",
        "                j += 1",
        "            # Move to the next slot",
        "            k += 1",
        "        # For all the remaining values",
        "        while i < len(left):",
        "            myList[k] = left[i]",
        "            i += 1",
        "            k += 1",
        "        while j < len(right):",
        "            myList[k]=right[j]",
        "            j += 1",
        "            k += 1 "
        ]

def delay():
    time.sleep(3)
colorStack = {}###############

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


for x in range(len(code)):
    draw_String(x,code[x],(0,0,255),True)
    pygame.display.update()   
    


def draw_rect(x:int, y:int, width:int, number:int, oldNum:int, merged:bool):
    if(merged == False):
        pygame.draw.rect(screen, (0,0,255), (x, y, width, 40), 2)
        screen.blit(font.render(str(number), True, (255,0,0)), (x+width//2-15, y+10))        
        pygame.display.update()
        pygame.display.flip()
    else:
        pygame.draw.rect(screen, (0,255,0), (x, y, width, 40), 2)
        screen.blit(font.render(str(oldNum), True, (0,0,0)), (x+width//2-15, y+10))
        screen.blit(font.render(str(number), True, (255,255,255)), (x+width//2-15, y+10))        
        pygame.display.update()
        pygame.display.flip()

def recCountIncreement():
    globals()["recursionCount"] += 1

def recCountDecrement():
    globals()["recursionCount"] -= 1
    
def mergeSort(myList,skip:int):
    delay()
    draw_String(0,code[0],(255,0,skip*25),True)
    pygame.draw.rect(screen, (255,0,skip*25), (skip*blockWidth, 100*recursionCount, len(myList)*blockWidth, 100), 2)
    pygame.display.flip()
    delay()
    for x in range(len(myList)):
        draw_rect(skip*blockWidth+x*blockWidth,100*recursionCount,blockWidth,myList[x],0,False)
        pygame.display.update()
    localRecCount = recursionCount
    delay()
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        leftCopy = myList[:mid]        
        right = myList[mid:]
        rightCopy = myList[mid:]
        delay()
        draw_String(0,code[0],(255,0,skip*25),False)
        draw_String(3,code[3],(255,0,skip*25),True)
        for x in range(len(left)):
            draw_rect(skip*blockWidth+x*blockWidth,100*localRecCount+50,blockWidth,left[x],0,False)
            pygame.display.update()
        delay()
        draw_String(3,code[3],(255,0,skip*25),False)
        draw_String(4,code[4],(255,0,skip*25),True)        
        for x in range(len(right)):
            draw_rect(skip*blockWidth+len(left)*blockWidth+x*blockWidth,100*localRecCount+50,blockWidth,right[x],0,False)
            pygame.display.update()
        # Recursive call on each half
        recCountIncreement()  
        draw_String(4,code[4],(255,0,skip*25),False)
        draw_String(6,code[6],(255,0,skip*25),True)
        mergeSort(left,skip)
        for x in range(len(left)):
            draw_rect(skip*blockWidth+x*blockWidth,100*localRecCount+50,blockWidth,left[x],leftCopy[x],True)
            pygame.display.update()
        delay()
        recCountDecrement()
        draw_String(6,code[6],(255,0,skip*25),False)
        draw_String(7,code[7],(255,0,skip*25),True)
        mergeSort(right,skip+len(left))
        delay()
        for x in range(len(right)):
            draw_rect(skip*blockWidth+len(left)*blockWidth+x*blockWidth,100*localRecCount+50,blockWidth,right[x],rightCopy[x],True)
            pygame.display.update()
        
        recCountDecrement()

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
              # The value from the left half has been used
              draw_rect(skip*blockWidth+k*blockWidth,100*localRecCount,blockWidth,left[i],myList[k],True)              
              myList[k] = left[i]
              delay()
              # Move the iterator forward
              i += 1
            else:
                draw_rect(skip*blockWidth+k*blockWidth,100*localRecCount,blockWidth,right[j],myList[k],True)
                myList[k] = right[j]
                delay()
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            draw_rect(skip*blockWidth+k*blockWidth,100*localRecCount,blockWidth,left[i],myList[k],True)
            myList[k] = left[i]
            delay()
            i += 1
            k += 1

        while j < len(right):
            draw_rect(skip*blockWidth+k*blockWidth,100*localRecCount,blockWidth,right[j],myList[k],True)
            myList[k]=right[j]
            delay()
            j += 1
            k += 1
    else:
        recCountIncreement()




        




        """



def mergeSort(myList,skip:int):
    delay()
    draw_String(0,code[0],(255,0,skip*25),True)
    pygame.draw.rect(screen, (255,0,skip*25), (skip*blockWidth, 100*recursionCount, len(myList)*blockWidth, 100), 2)
    pygame.display.flip()
    delay()
    for x in range(len(myList)):
        draw_rect(skip*blockWidth+x*blockWidth,100*recursionCount,blockWidth,myList[x],0,False)
        pygame.display.update()
    localRecCount = recursionCount
    delay()
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        leftCopy = myList[:mid]        
        right = myList[mid:]
        rightCopy = myList[mid:]
        delay()
        draw_String(0,code[0],(255,0,skip*25),False)
        draw_String(3,code[3],(255,0,skip*25),True)
        for x in range(len(left)):
            draw_rect(skip*blockWidth+x*blockWidth,100*localRecCount+50,blockWidth,left[x],0,False)
            pygame.display.update()
        delay()
        draw_String(3,code[3],(255,0,skip*25),False)
        draw_String(4,code[4],(255,0,skip*25),True)        
        for x in range(len(right)):
            draw_rect(skip*blockWidth+len(left)*blockWidth+x*blockWidth,100*localRecCount+50,blockWidth,right[x],0,False)
            pygame.display.update()
        # Recursive call on each half
        recCountIncreement()  
        draw_String(4,code[4],(255,0,skip*25),False)
        draw_String(6,code[6],(255,0,skip*25),True)
        mergeSort(left,skip)
        for x in range(len(left)):
            draw_rect(skip*blockWidth+x*blockWidth,100*localRecCount+50,blockWidth,left[x],leftCopy[x],True)
            pygame.display.update()
        delay()
        recCountDecrement()
        draw_String(6,code[6],(255,0,skip*25),False)
        draw_String(7,code[7],(255,0,skip*25),True)
        mergeSort(right,skip+len(left))
        delay()
        for x in range(len(right)):
            draw_rect(skip*blockWidth+len(left)*blockWidth+x*blockWidth,100*localRecCount+50,blockWidth,right[x],rightCopy[x],True)
            pygame.display.update()
        
        recCountDecrement()

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
              # The value from the left half has been used
              draw_rect(skip*blockWidth+k*blockWidth,100*localRecCount,blockWidth,left[j],myList[k],True)              
              myList[k] = left[i]
              delay()
              # Move the iterator forward
              i += 1
            else:
                draw_rect(skip*blockWidth+k*blockWidth,100*localRecCount,blockWidth,right[j],myList[k],True)
                myList[k] = right[j]
                delay()
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            draw_rect(skip*blockWidth+k*blockWidth,100*localRecCount,blockWidth,left[i],myList[k],True)
            myList[k] = left[i]
            delay()
            i += 1
            k += 1

        while j < len(right):
            draw_rect(skip*blockWidth+k*blockWidth,100*localRecCount,blockWidth,right[j],myList[k],True)
            myList[k]=right[j]
            delay()
            j += 1
            k += 1
    else:
        recCountIncreement()









        """

























mergeSort(myList,0)
time.sleep(10)
pygame.quit()
print("hello")
exit()



