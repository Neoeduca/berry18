from time import sleep, sleep_us
from machine import Pin, PWM, time_pulse_us

class Servo360:
    def __init__(self, servo_pin:int):
        self.servo = PWM(Pin(servo_pin))
        self.servo.freq(50)
        self.grados_anterior= 90
        
    def girar(self, grados):
        if(self.grados_anterior != grados):
            self.grados_anterior = grados
            self._girar(grados, grados)
            
    
    def detener(self):
        self.girar(90)
    
    def _girar(self, grados1, grados2):
        duty = int((12.346*grados1**2 + 7777.8*grados2 + 700000))
        self.servo.duty_ns(duty)


    

class Auto:
    def __init__(self, pin_motor1, pin_motor2):
        self.motor1 = Servo360(pin_motor1)
        self.angulo_motor1 = 90
        self.angulo2_motor1 = 90
        
        self.motor2 = Servo360(pin_motor2)
        self.angulo_motor2 = 90
        self.angulo2_motor2 = 90
        
        self.estado = 0
        
    def probar(self, grados_1, grados_2):
        print("probando con ", grados_1, " y ", grados_2)
        self.motor1.girar(grados_1)
        self.motor2.girar(grados_2)
        sleep(3)  
        print("frenando con 90")
        self.motor1.detener()
        self.motor2.detener()
        print("Si no frena, requiere calibración manual")
        sleep(1)  
    
    def angulos(self, grados_1, grados_2):
        self.angulo_motor1 = grados_1
        self.angulo_motor2 = grados_2
    def angulos2(self, grados_1, grados_2):
        self.angulo2_motor1 = grados_1
        self.angulo2_motor2 = grados_2
        
    def avanzar(self):
        if self.estado!=1:
            self.motor1.girar(self.angulo_motor1)
            self.motor2.girar(self.angulo_motor2)
            self.estado=1
        
    def detener(self):
        if self.estado!=4:
            self.motor1.detener()
            self.motor2.detener()
            self.estado=4

    def retroceder(self):
        if self.estado!=6:
            self.motor1._girar(self.angulo_motor1, self.angulo_motor2)
            self.motor2._girar(self.angulo_motor2, self.angulo_motor1)
            self.estado=6
            
    def izquierda(self):
        if self.estado!=2:
            self.motor1.girar(self.angulo_motor2)
            self.motor2.girar(self.angulo_motor2)
            self.estado=2

    def derecha(self):
        if self.estado!=3:
            self.motor1.girar(self.angulo_motor1)
            self.motor2.girar(self.angulo_motor1)
            self.estado=3
            
