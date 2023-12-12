from machine import UART, Pin, PWM
import time
uart1 = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

ledbuiltin = Pin('LED', Pin.OUT) #version pico W
ledbuiltin.on()
time.sleep(3)
ledbuiltin.off()

# --------------init moteur------------------
servo = PWM(Pin(0)) #broche 0
servo.freq(50)         
servo.duty_u16(3000)       
# ----------------------------------------

while True :
    if uart1.any()>0 : 
        message=uart1.read()
        message_decode = message.decode() 	
        print(message)
        if '0' in  message_decode : #bretzel entier
            servo.duty_u16(3000) # commande moteur  
        else :
            servo.duty_u16(7000) # commande moteur
