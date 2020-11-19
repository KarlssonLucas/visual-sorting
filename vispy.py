import pygame
import random

pygame.init()
screen = pygame.display.set_mode([1000, 500])
running = True

list = []

def generateGraph(arr):
    for i in range(0,500):
        l = [random.randint(1,2000)]
        arr = arr + l
    return arr

def drawGraph(arr):
    screen.fill((255,255,255))
    p = 0
    for i in arr:
        pygame.draw.rect(screen, (255,0,0), (p, 500, 5, i), 10)
        p += 2

def isSorted(arr):
    for i in range(0,len(arr)-2):
        if not (arr[i] <= arr[i+1]):
            return False
    return True

def median_of_three(a, b, c):
    return sorted([a, b, c])[1]

def sort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        middleindex = int((len(array) - 1)/2)
        pivot = median_of_three(array[0], array[len(array)-1], array[middleindex])
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
            drawGraph(array)
            pygame.display.update()
        return sort(less)+equal+sort(greater)
    else:
        return array 

list = generateGraph(list)
while running:
    pygame.time.Clock().tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    drawGraph(list)
    if not isSorted(list):
        list = sort(list)

    pygame.display.flip()
pygame.quit()
