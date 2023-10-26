import pyautogui as pe
import contas
import time
import os

pe.hotkey('win', 'e')
time.sleep(1)
pe.hotkey('f4')
time.sleep(1)
pe.hotkey('shift', 'home')
time.sleep(1)
pe.typewrite('Z:\Relatorio Gerencial')
time.sleep(1)
pe.hotkey('enter')
time.sleep(1)
pe.hotkey('down')
time.sleep(1)
pe.hotkey('enter')
time.sleep(10)

pe.hotkey('alt', 'tab')
time.sleep(1)
pe.hotkey('up')
time.sleep(1)
pe.hotkey('enter')
time.sleep(1)






#
pe.hotkey('win')
pe.typewrite("Bloco")
time.sleep(1)
pe.hotkey('enter')
time.sleep(1)
pe.write("Terminou de atualizar")
time.sleep(2)

pe.hotkey('alt', 'tab')
time.sleep(5)
pe.hotkey('ctrl', 'home')
time.sleep(1)
pe.hotkey('alt')
time.sleep(1)
pe.hotkey('c')
time.sleep(1)
pe.hotkey('k')
time.sleep(1)
pe.hotkey('l')
time.sleep(1)
pe.hotkey('ctrl', 't')
pe.hotkey('ctrl', 'c')



from tkinter import *

root = Tk()

altura_monitor = root.winfo_screenheight()
largura_monitor = root.winfo_screenwidth()
  
print("Monitor atual - width x height = %d x %d (pixels)" %(largura_monitor, altura_monitor))

if largura_monitor > 1366:
    porcentagem = 1366 / largura_monitor
    largura_monitor = largura_monitor * porcentagem

print("Largura atual = %d" %(largura_monitor))

altura_monitor = altura_monitor