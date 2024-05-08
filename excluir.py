import pyautogui
import time
pyautogui.PAUSE = 1

connectere = ("https://sistema.connectere.agr.br/usuarios/sign_in")


pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(connectere)
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(865, 633) # Clique no campo de email
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(10)
pyautogui.click(40, 270) # Clique no menu de comercial
time.sleep(5)
pyautogui.click(1138, 480) # Clique no botão de adicionar produto
time.sleep(20)
pyautogui.click(509, 495) # Clique no campo fabricante
pyautogui.write("fabricante")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.write("fungicida")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.write("opereta plus")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.write("litro")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter") # Clique no botão de salvar
time.sleep(5)
pyautogui.click(1634, 285) # Clique no botão + produto