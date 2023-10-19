# -*- coding: utf-8 -*-
from pynput.mouse import Button, Controller
import time
from screen_search import Search
 
mouse = Controller()



def click_raton_posicion (x,y):
    mouse.position = (x, y)
    print('Now we have moved it to {0}'.format(
        mouse.position))
    # Press and release
    mouse.press(Button.left)
    time.sleep(0.08)
    mouse.release(Button.left)
    time.sleep(0.08)
    mouse.press(Button.left)
    time.sleep(0.08)
    mouse.release(Button.left)
    time.sleep(1)
 
 
 
def imagen():
    search = Search("img/img.png")
    pos = search.imagesearch()
    print('dasda')
    if pos[0] == -1:
        return False
    else:
        return pos
    

def imagen2():
    search = Search("img/888_2.png")
    pos = search.imagesearch()
    print('dasda2')
    if pos[0] == -1:
        return False
    else:
        return pos
 
def imagen3():
    search = Search("img/continue.png")
    pos = search.imagesearch()
    print('No se encontró')
    if pos[0] == -1:
        return False
    else:
        return pos
 
 
while True:
    time.sleep(5)
    # mouse.position = (2034, 107)
    # mouse.press(Button.left)
    # time.sleep(0.08)
    # mouse.release(Button.left)
    # time.sleep(1)


    coordenadas = imagen()
    #si encuentro
    if coordenadas!= False:
        click_raton_posicion (coordenadas[0], coordenadas[1])
    time.sleep(0.5)

    coordenadas = imagen3()
    #si encuentro2
    if coordenadas!= False:
        click_raton_posicion (coordenadas[0], coordenadas[1])
    time.sleep(0.5)

    coordenadas = imagen2()
    #si encuentro2
    if coordenadas!= False:
        click_raton_posicion (coordenadas[0], coordenadas[1])
    time.sleep(0.5)