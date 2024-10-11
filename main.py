# Imports
from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
import time

# Set up I2C and the pins we're using for it
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
# ADC init
adc0=ADC(26)
adc1=ADC(27)
adc2=ADC(28)
adc4=ADC(4)
# Short delay to stop I2C falling over
time.sleep(1) 

# Define the display and size (128x32)
display = SSD1306_I2C(128, 32, i2c)
cf = 3.3 / (65535)
# Clear the display first
display.fill(0) 
while True :
    v0=adc0.read_u16()*cf
    v1=adc1.read_u16()*cf
    v2=adc2.read_u16()*cf
    v4=adc4.read_u16()*cf
    temp = 27 - (v4 - 0.706)/0.001721
    display.fill(0)
    display.text("ADC0: "+str(round(v0,2))+" V",0,0)
    display.text("ADC1: "+str(round(v1,2))+" V",0,8)
    display.text("ADC2: "+str(round(v2,2))+" V",0,16)
    display.text("TEMP: "+str(round(v4,0))+" C",0,24)
    time.sleep(1)

# Update the display
    display.show()
