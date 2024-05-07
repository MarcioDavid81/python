import pyautogui
import time
pyautogui.PAUSE = 1

# Abre o menu iniciar
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://sistema.connectere.agr.br/usuarios/sign_in")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(926, 630)
time.sleep(1)
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(42, 266)
time.sleep(1)
pyautogui.click(729, 611)
time.sleep(10)
pyautogui.click(256, 541)
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")