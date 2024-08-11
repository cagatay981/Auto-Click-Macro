from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Listener, KeyCode
import threading
import time

mouse = MouseController()

# Değişkenler
r_tusu = KeyCode(char='r')
f_tusu = KeyCode(char='f')
sol_tiklama = False
sag_tiklama = False
cps = 30  # Saniyede tıklama sayısı (Clicks Per Second)

print("""
x--------------------x
|    autoclicker     |
|                    |
|  sol   ve   sağ    |
|   r          f     |
|                    |
x--------------------x
""")

# Sol tıklama fonksiyonu
def sol_tikla():
    while sol_tiklama:
        mouse.click(Button.left)
        time.sleep(1 / cps)

# Sağ tıklama fonksiyonu
def sag_tikla():
    while sag_tiklama:
        mouse.click(Button.right)
        time.sleep(1 / cps)

# Tuş basma fonksiyonları
def on_press(key):
    global sol_tiklama, sag_tiklama

    if key == r_tusu:
        sol_tiklama = not sol_tiklama
        if sol_tiklama:
            threading.Thread(target=sol_tikla).start()

    elif key == f_tusu:
        sag_tiklama = not sag_tiklama
        if sag_tiklama:
            threading.Thread(target=sag_tikla).start()

# Klavye dinleyici başlatma
with Listener(on_press=on_press) as listener:
    listener.join()
