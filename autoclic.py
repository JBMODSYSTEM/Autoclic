from pyautogui import *
from tkinter import *
from tkinter import messagebox as MessageBox
import pyautogui
import time
import keyboard
import random
import win32api, win32con


# pyautogui.displayMousePosition()
# Position 888 X: 3406 y: 78 RGB (247,180,142)
# Position reload X: 3016 y: 118 RGB (247,180,142)
# Position blanco X: 2174 y: 1250
# Position negro X: 2392 y: 437




def click(x,y):
    win32api.SetCursorPos((x,y)) #----------------------------------> Posicion del cursor
    time.sleep(0.5) #-----------------------------------------------> Tiempo antes de precionar el boton del mouse luego de posicionarse
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) #-------> Boton precionado del mouse
    time.sleep(0.05) #----------------------------------------------> Tiempo de ejecucion entre precionar y soltar boton del mouse
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0) #---------> Boton suelto del mouse
    time.sleep(0.1) #-----------------------------------------------> Descanso entre cliks 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) #-------> Boton precionado del mouse
    time.sleep(0.05) #----------------------------------------------> Tiempo de ejecucion entre precionar y soltar boton del mouse
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0) #---------> Boton suelto del mouse

def temporizador():
    # while keyboard.is_pressed('q') == False:
    while 2 == 2 :
        time.sleep(10)
        click(3416,80)
        # print("Click 1 funcionando")
        time.sleep(5)
        click(3016,118)
        # print("Click 2 funcionando")
        # resultado = MessageBox.askquestion("Reiniciar", "¿Está seguro que desea reinciar?")
        # if resultado == "yes":
        #     time.sleep(0.01)
        # else:
        #     MessageBox.showwarning("Alerta", "Sección sólo para administradores.")

def exitprog():
    root.destroy()

root = Tk()
frame = Frame(root)
frame.pack()
frame.config(width=150,height=50)
Button(root, text = "Iniciar", command=temporizador).pack()
Button(root, text = "Cerrar", command=exitprog).pack()


root.wm_attributes("-topmost", True) # Esta es la línea importante.
root.mainloop()






# while keyboard.is_pressed('q') == False:
#     if pyautogui.pixel(2174, 1250) [0] == 0:
#         print(pyautogui.displayMousePosition())
#         time.sleep(5)
#         resultado = MessageBox.askquestion("Reiniciar", "¿Está seguro que desea reinciar?")
#         if resultado == "yes":
#             time.sleep(0.01)
#         else:
#             # print("Click 1 funcionando")
#             MessageBox.showwarning("Alerta", "Sección sólo para administradores.")

        

        # time.sleep(5)
        
        # click(3434,1024)
        # print("Click 2 funcionando")
