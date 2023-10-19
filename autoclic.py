from pyautogui import *
from tkinter import *
from tkinter import messagebox as MessageBox
import time
import win32api, win32con


#-*-*-*-*-*-*-*-*-*-*-*-*-*-* Funcion para el click *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
def click(x,y): 
    win32api.SetCursorPos((x,y)) #----------------------------------> Posicion del cursor
    time.sleep(0.03) #-----------------------------------------------> Tiempo antes de precionar el boton del mouse luego de posicionarse
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) #-------> Boton precionado del mouse
    time.sleep(0.03) #----------------------------------------------> Tiempo de ejecucion entre precionar y soltar boton del mouse
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0) #---------> Boton suelto del mouse
    time.sleep(0.05) #-----------------------------------------------> Descanso entre cliks 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) #-------> Boton precionado del mouse
    time.sleep(0.03) #----------------------------------------------> Tiempo de ejecucion entre precionar y soltar boton del mouse
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0) #---------> Boton suelto del mouse


def temporizador():
    while 2 == 2 :
        time.sleep(600)
        click(141,104)
        time.sleep(1)
        click(197, 205)


def exitprog():
    root.destroy()


root = Tk()
frame = Frame(root)
frame.pack()
frame.config(width=60,height=50)


Button(root, text = "Iniciar", command=temporizador).pack(side=LEFT)
Button(root, text = "Cerrar", command=exitprog).pack(side=LEFT)


root.wm_attributes("-topmost", True) # Esta es la línea importante de superposicion de pantalla .
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

# -------------------------------------------- Desuso ------------------------------------#



# pyautogui.displayMousePosition()

        # j, k = pyautogui.position()
        # MessageBox.showwarning("Alerta","j: {}, k: {}".format(j, k))
        # break

# pyinstaller --windowed --onefile --icon=./icono.ico autoclic.py