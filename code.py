import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

btn1_pin = board.GP16
btn2_pin = board.GP17
btn3_pin = board.GP18
btn4_pin = board.GP19
btn5_pin = board.GP20
btn6_pin = board.GP21
btn7_pin = board.GP14
btn8_pin = board.GP15
btn9_pin = board.GP13

keyboard = Keyboard(usb_hid.devices)

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN

btn7 = digitalio.DigitalInOut(btn7_pin)
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.DOWN

btn8 = digitalio.DigitalInOut(btn8_pin)
btn8.direction = digitalio.Direction.INPUT
btn8.pull = digitalio.Pull.DOWN

btn9 = digitalio.DigitalInOut(btn9_pin)
btn9.direction = digitalio.Direction.INPUT
btn9.pull = digitalio.Pull.DOWN







while True:
    if btn1.value:
        print ("button 1 pressed, ALT + TAB")
        keyboard.press(Keycode.ALT, Keycode.TAB)
        time.sleep(0.2)
        keyboard.release(Keycode.ALT, Keycode.TAB)
    if btn2.value:
        print ("button 2 pressed, CTRL + TAB ")
        keyboard.press(Keycode.CONTROL, Keycode.TAB)
        time.sleep(0.2)
        keyboard.release(Keycode.CONTROL, Keycode.TAB)
    if btn3.value:
        print ("button 3 pressed, SHIFT + TAB ")
        keyboard.press(Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB)
        time.sleep(0.2)
        keyboard.release(Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB)
    if btn4.value:
        print ("button 4 pressed, CTRL + C")
        keyboard.press(Keycode.CONTROL, Keycode.V)
        time.sleep(0.2)
        keyboard.release(Keycode.CONTROL, Keycode.V)
    if btn5.value:
        print ("button 5 pressed, CTRL + V")
        keyboard.press(Keycode.CONTROL, Keycode.C)
        time.sleep(0.2)
        keyboard.release(Keycode.CONTROL, Keycode.C)
    if btn6.value:
        print ("button 6 pressed, WINDOWS + V")
        keyboard.press(Keycode.GUI, Keycode.V)
        time.sleep(0.2)
        keyboard.release(Keycode.GUI, Keycode.V)
    if btn7.value:
        print ("button 7 pressed, CTRL + T")
        keyboard.press(Keycode.CONTROL, Keycode.T)
        time.sleep(0.2)
        keyboard.release(Keycode.CONTROL, Keycode.T)
    if btn8.value:
        print ("button 8 pressed, CTRL + W")
        keyboard.press(Keycode.CONTROL, Keycode.W)
        time.sleep(0.2)
        keyboard.release(Keycode.CONTROL, Keycode.W)
    if btn9.value:
        print ("button 9 pressed, SPACEBAR")
        keyboard.press(Keycode.SPACEBAR)
        time.sleep(0.2)
        keyboard.release(Keycode.SPACEBAR)



    time.sleep(0.1)
 

#code.py


