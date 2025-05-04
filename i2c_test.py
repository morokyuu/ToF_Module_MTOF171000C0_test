from machine import Pin, I2C
import time

i2c = I2C(0,scl=Pin(17),sda=Pin(16),freq=100000)

## address scan for ToF module.
## this process is for confirming
addr = i2c.scan()
print(addr)
## module ID = 0x52
## i2c.scan() = [82]d = 0x52

led = Pin(25, Pin.OUT)

## measure loop
while True:
    i2c.writeto(82,b'\xd3')
    data = i2c.readfrom(82,2)
    data = int.from_bytes(data,'big')
    print(f'{data}')
    time.sleep(0.01)
    led.toggle()
