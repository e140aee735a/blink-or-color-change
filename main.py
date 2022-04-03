from m5stack import *
from m5ui import *
from uiflow import *
import time

setScreenColor(0x84b71e)








while True:
  if btnA.isPressed():
    setScreenColor(0xc05db1)
    wait(2)
    setScreenColor(0x0d2563)
  else:
    for count in range(3):
      M5Led.on()
      wait(1)
      M5Led.off()
      wait(1)
  wait_ms(2)
