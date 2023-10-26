import pyautogui as pe
import contas
import time
import os
import Indicadores

os.startfile('C:\WINDOWS\system32\mstsc.exe')
time.sleep(2)

pe.hotkey('enter')
time.sleep(2)

#abre o SFI
pe.moveTo(51,237)
pe.doubleClick()
time.sleep(3)

#faz login
pe.typewrite(contas.login)
pe.hotkey('enter')
time.sleep(2)
pe.typewrite(contas.senha)
pe.hotkey('enter')

#abre o balcão e gera o relatório de produtos
pe.hotkey('3')
time.sleep(1)
pe.hotkey('5')
time.sleep(3)
pe.hotkey('R')
time.sleep(1)
pe.hotkey('4')
time.sleep(1) 
pe.hotkey('8')
time.sleep(1) 
pe.hotkey('enter')
pe.hotkey('enter')

#insere a data requerida
pe.typewrite(Indicadores.dataAnterior) #data inicial
pe.hotkey('enter')
pe.typewrite(Indicadores.dataAnterior) #data final
pe.hotkey('enter')
time.sleep(10) #espera gerar excel

#salva o arquivo no computador
pe.hotkey('f12') #salvar como
time.sleep(2)
pe.typewrite('relatorio') #nome do arquivo
time.sleep(2)
pe.hotkey('f4') #altera repositório
pe.hotkey('esc')
pe.typewrite('Z:\Marcos\Dev') #repositório desejado
time.sleep(5)
pe.hotkey('enter')
time.sleep(1)
pe.hotkey('enter')
time.sleep(1)
pe.hotkey('enter')
time.sleep(1)
#seleciona salvar sem mover o mouse
pe.hotkey('tab')
pe.hotkey('tab')
pe.hotkey('tab')
pe.hotkey('tab')
pe.hotkey('tab')
pe.hotkey('tab')
pe.hotkey('tab')
pe.hotkey('tab')
pe.hotkey('tab')
pe.hotkey('tab')
pe.hotkey('tab')
pe.hotkey('tab')
pe.hotkey('tab')
pe.hotkey('enter')
time.sleep(1)
pe.hotkey('tab')
time.sleep(1)
pe.hotkey('enter')
time.sleep(3)
pe.hotkey('alt', 'tab')
pe.hotkey('alt', 'f4') #fecha o arquivo

#manda fechar o sistema
pe.hotkey('ctrl', 'c')
time.sleep(1)
pe.hotkey('esc')
time.sleep(1)
pe.typewrite("s")
time.sleep(1)
pe.hotkey('enter')

#fecha a conexão remota
pe.hotkey('alt', 'f4')



