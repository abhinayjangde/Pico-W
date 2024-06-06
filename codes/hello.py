import machine
import time
led = machine.Pin('LED', machine.Pin.OUT)
count=0
while(count<=5):
    led.on()
    time.sleep(0.5)
    count+=1
    led.off()
    time.sleep(0.5)
    