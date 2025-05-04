from machine import Pin, I2C
import time

## reference URL
## https://www.socle-tech.com/doc/IC%20Channel%20Product/ToF%20Module%20MTOF171010C0%20Application%20Notes.pdf
## https://www.socle-tech.com/doc/IC%20Channel%20Product/MTOF171000C0%20ToF%20module%20specification.pdf
## https://docs.micropython.org/en/latest/library/machine.I2C.html#machine-i2c

## module ID = 0x52 = 82d
## 100kHz clk max
## For uart RXTpin is used for ChipSelect-Pin at I2C mode.
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
