from machine import Pin, PWM 
from utime import ticks_ms, ticks_diff

class MotorDC:
    def __init__(self,EN,IN1,IN2,encoder):
        self.IN1 = Pin(IN1,Pin.OUT)
        self.IN2 = Pin(IN2,Pin.OUT)
        self.pwm = PWM(Pin(EN))
        self.speed = 70
        
        self.resolucion_encoder = 11*99
        self.encoder=Pin(encoder,Pin.IN)
        self.pulsos = 0
        self.t_pasado = ticks_ms()
        self.encoder.irq(trigger=Pin.IRQ_RISING, handler=self.handler_encoder)

    def handler_encoder(self,pin):
        self.pulsos += 1
    
    def rpm(self):
        t_actual = ticks_ms()
        t_transcurrido = ticks_diff(t_actual,self.t_pasado)/1000.0
        rpms=0
        try:
            rpms = (self.pulsos / self.resolucion_encoder)/t_transcurrido * 60
        except:
            pass
        self.pulsos = 0
        self.t_pasado = t_actual
        return rpms

    def moveradelante(self):
        self.IN1.value(1)
        self.IN2.value(0)
        self.pwm.freq(15000)
        self.pwm.duty_u16(self.speed*655)
        
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
        
        

    


