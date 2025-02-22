'''Clase para manejar motores DC con encoder + puente H L298N y placa berry18

Cada motor necesita:

EN         --> Pin PWM para control de velocidad                    | conexion puente h
IN1, IN2   --> Pines digitales para control de sentido de movimiento| conexion puente h
encoder    --> Pin de interrupciones para leer el encoder           | conexion motor DC con encoder

'''

from machine import Pin, PWM 
from utime import ticks_ms, ticks_diff

class MotorDC:
    def __init__(self,EN,IN1,IN2,encoder):
        self.IN1 = Pin(IN1,Pin.OUT)
        self.IN2 = Pin(IN2,Pin.OUT)
        self.pwm = PWM(Pin(EN, Pin.OUT))
        self.speed = 70 #70% duty cycle por defecto. Valores de 0 a 100 requeridos
        
        self.resolucion_encoder = 11*99 #encoder 11 ticks + caja reductora 1:99
        self.encoder=Pin(encoder,Pin.IN)
        self.pulsos = 0 # para leer encoder
        self.t_pasado = ticks_ms() #para calcular RPM
        self.encoder.irq(trigger=Pin.IRQ_RISING, handler=self.handler_encoder) #interrupcion en subida y función handler a ejecutar 

    def handler_encoder(self,pin):
        self.pulsos += 1 #lee pulsos del encoder
    
    def rpm(self):
        #funcion que calcula las RPM del motor
        t_actual = ticks_ms() #tomamos tiempo actual
        t_transcurrido = ticks_diff(t_actual,self.t_pasado)/1000.0 # diferencia con t_pasado en segundos
        rpms=0
        try:#a veces daba ZeroDivisinError
            rpms = (self.pulsos / self.resolucion_encoder)/t_transcurrido * 60 #calcula RPM
        except:
            pass
        #reseteamos pulsos leidos y actualizamos tiempos
        self.pulsos = 0
        self.t_pasado = t_actual
        return rpms

    def moveradelante(self):
        #logica puente h para una dirección si se invierte gira en sentido contrario
        self.IN1.value(1)
        self.IN2.value(0)
        
        self.pwm.freq(15000) # frecuencia alta para evitar sonidos en el motor
        self.pwm.duty_u16(self.speed*655) #transforma speed (porcentaje) a dutycycle 
        
    def moveratras(self):
        self.IN1.value(0)
        self.IN2.value(1)
        self.pwm.freq(15000)
        self.pwm.duty_u16(self.speed*655)
        
    def detener(self):
        self.IN1.value(0)
        self.IN2.value(0)
    
    def velocidad(self,vel):
        self.speed = vel
        
        

    


