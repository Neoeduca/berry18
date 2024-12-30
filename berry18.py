from time import sleep
from machine import Pin, PWM

class Servo360:
    def __init__(self, servo_pin:int):
        self.servo = PWM(Pin(servo_pin))
        self.servo.freq(50)
        self.grados = 90
        self.estado = 0
        
    def probar(self, grados:int):
        print("probando con ", grados)
        self._girar(grados, grados)
        sleep(3)  
        print("frenando con 90")
        self.detener()
        print("Si no frena, requiere calibración manual")
        sleep(1)  
        
    def velocidad(self, grados:int):
        self.grados=grados
    
    def girar(self):
        if(self.grados != self.estado):
            self._girar(self.grados, self.grados)
            self.estado = self.grados
    
    def detener(self):
        self.velocidad(90)
        self._girar(self.grados, self.grados)
        
    def _girar(self, grados1, grados2):
        duty = int((12.346*grados1**2 + 7777.8*grados2 + 700000))
        self.servo.duty_ns(duty)


    

class Auto:
    def __init__(self, motor1:Servo360, motor2:Servo360):
        self.motor1 = motor1
        self.motor2 = motor2
        self.estado = 0
        
    def probar(self, grados_1, grados_2):
        print("probando con ", grados_1, " y ", grados_2)
        self.motor1._girar(grados_1, grados_1)
        self.motor2._girar(grados_2, grados_2)
        sleep(3)  
        print("frenando con 90")
        self.motor1.detener()
        self.motor2.detener()
        print("Si no frena, requiere calibración manual")
        sleep(1)  
    
    def velocidad(self, grados_1, grados_2):
        self.motor1.velocidad(grados_1)
        self.motor2.velocidad(grados_2)
        
    def avanzar(self):
        if self.estado!=1:
            self.motor1.girar()
            self.motor2.girar()
            self.estado=1
        
    def detener(self):
        if self.estado!=4:
            self.motor1.detener()
            self.motor2.detener()
            self.estado=4

    def retroceder(self):
        if self.estado!=6:
            self.motor1._girar(self.motor1.grados, self.motor2.grados)
            self.motor2._girar(self.motor2.grados, self.motor1.grados)
            self.estado=6
            
    def izquierda(self):
        if self.estado!=2:
            self.motor1._girar(self.motor2.grados, self.motor2.grados)
            self.motor2._girar(self.motor2.grados, self.motor2.grados)
            self.estado=2

    def derecha(self):
        if self.estado!=3:
            self.motor1._girar(self.motor1.grados, self.motor1.grados)
            self.motor2._girar(self.motor1.grados, self.motor1.grados)
            self.estado=3


class HCSR04:   
    def __init__(self):
        self.trig_pin = Pin(18, Pin.OUT) 
        self.echo_pin = Pin(19, Pin.IN)
        self.SOUND_SPEED=340
    def medir(self):
        self.trig_pin.value(0)
        sleep_us(5)
        self.trig_pin.value(1)
        sleep_us(10)
        self.trig_pin.value(0)
        ultrason_duration = time_pulse_us(self.echo_pin, 1, 30000) # Renvoie le temps de propagation de l'onde (en µs)
        distance_cm = self.SOUND_SPEED * ultrason_duration / 20000
        return distance_cm

