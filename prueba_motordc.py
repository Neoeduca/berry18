from motordc import MotorDC
from time import sleep
from utime import ticks_diff,ticks_ms

#MotorDC(EN,IN1,IN2,encoder)

motor1 = MotorDC(15,4,5,26)
motor2 = MotorDC(14,2,3,28)

#velocidad de 0 a 100. se recomienda partir en 60 por la caja reductora
motor1.velocidad(100)
motor2.velocidad(100)

tiempo = ticks_ms()
while ticks_diff(ticks_ms(),tiempo)<=10000:
    
    motor1.moveradelante()
    motor2.moveradelante()
    print(motor1.rpm(),"---",motor2.rpm()) #el metodo rpm obtiene las rpm del motor usando el encoder
    sleep(0.1)

motor1.detener()
motor2.detener()