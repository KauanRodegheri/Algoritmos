import pyautogui
from time import sleep
import datetime
agora=datetime.datetime.now()
agora=str(agora.time())

pyautogui.PAUSE = 0.5
    #ABRINDO NAVEGADOR
pyautogui.press('win')
pyautogui.write('whatsapp')
pyautogui.press('enter')
    #DENTRO DO WPP
sleep(1)
pyautogui.click(x=265, y=188)

    #NA CONVERSA
if agora>='00:00:00' and agora<='05:59:59':
    pyautogui.write('Boa madrugada meu amor, dorme com Deus')
    pyautogui.hotkey('ctrl','shift','e')
    sleep(0.5)
    pyautogui.write('s2')
    pyautogui.click(x=539, y=352)
    pyautogui.press('esc')
    pyautogui.press('esc')
    pyautogui.press('enter')
if agora>='06:00:00' and agora<='11:59:59':
    pyautogui.write('Bom Dia meu amor, tudo certo?')
    pyautogui.press('enter')
if agora>='12:00:00' and agora<='17:59:59':
    pyautogui.write('Boa tarde meu amor, como ta ai?')
    pyautogui.press('enter')
if agora>='18:00:00' and agora<='23:59:59':
    pyautogui.write('AIIIIIIIIIIIINNNNNNNNNNNNN QUE DELICIA O VERAO')
    pyautogui.press('enter')


