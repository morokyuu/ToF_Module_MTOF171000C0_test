from machine import Pin, I2C
import time

## module ID = 0x52 = 82d
## 100kHz clk max
i2c = I2C(0,scl=Pin(17),sda=Pin(16),freq=100000)

led = Pin(25, Pin.OUT)

## measure loop
while True:
    ## Distance measure command 0xD3
    i2c.writeto(82,b'\xd3')
    ## Read the distance data(mm) for 2bytes.
    data = i2c.readfrom(82,2)
    ## binary array to int
    data = int.from_bytes(data,'big')
    print(f'{data}')
    
    time.sleep(0.01)
    led.toggle()
