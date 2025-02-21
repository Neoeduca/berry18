from motordc import MotorDC
from time import sleep
from utime import ticks_diff,ticks_ms

motor1 = MotorDC(15,4,5,26)
motor2 = MotorDC(14,2,3,28)

motor1.velocidad(100)

tiempo = ticks_ms()
while ticks_diff(ticks_ms(),tiempo)<=10000:
    
    motor1.moveratras()
    motor2.moveradelante()
    print(motor1.rpm(),"---",motor2.rpm())
    sleep(0.1)

motor1.detener()
motor2.detener()