'''Programa para testear la placa completa'''

from machine import Pin, PWM, time_pulse_us
from time import sleep, sleep_ms, sleep_us, ticks_diff, ticks_us
import utime as time

class servo360:
    def __init__(self, servo_pin:int):
        self.servo = PWM(Pin(servo_pin))
        self.servo.freq(50)
        self.grados_anterior= 90
        
    def girar(self, grados):
        duty = int((12.346*grados**2 + 7777.8*grados + 700000))
        self.servo.duty_ns(duty)

    def detener(self):
        self.servo.duty_ns(0)
    
    def barrer(self):
        for i in range(0, 180, 5):
            print(i)
            self.girar(i)
            sleep(0.2)
        self.detener()

class Qti:
    def __init__(self, pin):
        self.pin = pin
        
    
    def RCtime(self):    
        sensor = Pin(self.pin, Pin.OUT)
        sensor.on() 
        sleep_ms(1)
        
        sensor = Pin(self.pin, Pin.IN) 
        sensor.off()
        start_time = ticks_us()
        while sensor.value():
            pass
        end_time = ticks_us()

        return ticks_diff(end_time, start_time)
    

    def medir(self):
        return self.RCtime()

class Ultrasonico:   
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
        ultrason_duration = time_pulse_us(self.echo_pin, 1, 30000)
        distance_cm = self.SOUND_SPEED * ultrason_duration / 20000
        return distance_cm

class Buzzer:
    def __init__(self, pin: int) -> None:
        self.pin = Pin(pin)
        self.buzzer = PWM(self.pin)
    
    def on(self, frecuencia: int=440) -> None:
        self.buzzer.freq(frecuencia)
        self.buzzer.duty_u16(2**15)
        
    def off(self) -> None:
        self.buzzer.duty_u16(0)
        
    def tone(self, frecuencia: int, duracion: float, silencio: float = 0) -> None:
        """
        Reproduce un tono con la frecuencia especificada durante la duración dada,
        seguido de un silencio opcional.
        
        :param frecuencia: Frecuencia del tono en Hz.
        :param duracion: Duración del tono en segundos.
        :param silencio: Duración del silencio entre tonos (por defecto 0).
        """
        self.on(frecuencia)
        sleep(duracion)
        self.off()
        sleep(silencio)
        
        
def test(i):
    if 0<=i<=1:
        boton = Pin(i, Pin.IN, Pin.PULL_UP)
        print("Se testeará por 5 segundos")
        start_time = ticks_us()
        while ticks_diff(ticks_us(), start_time)<5_000_000:
            print(boton.value())
            sleep(0.1)
        
    elif 2<=i<=4: #test leds
        led = Pin(i, Pin.OUT)
        for i in range(3):
            led.on()
            sleep(0.4)
            led.off()
            sleep(0.4)
    elif i == 5:
        #cambiar luego por una cancioncita corta
        buzzer = Buzzer(i)
        for i in range(5):
            buzzer.on()
            sleep(0.4)
            buzzer.off()
            sleep(0.4)
    elif 6<= i <= 12:
        qti = Qti(i)
        print("Se testeará por 5 segundos")
        start_time = ticks_us()
        while ticks_diff(ticks_us(), start_time)<5_000_000:
            print(qti.medir())
            sleep(0.1)
    elif 13<= i<=15:
        servo = servo360(i)
        servo.barrer()
    elif i == 16:
        servo13 = servo360(13)
        servo14 = servo360(14)
        for i in range(0, 180, 5):
            print(i)
            servo13.girar(i)
            servo14.girar(i)
            sleep(0.2)
        servo13.detener()
        servo14.detener()
    elif i == 17:
        servo13 = servo360(13)
        servo15 = servo360(15)
        for i in range(0, 180, 5):
            print(i)
            servo13.girar(i)
            servo15.girar(i)
            sleep(0.2)
        servo13.detener()
        servo15.detener()
    elif i == 18:
        servo14 = servo360(14)
        servo15 = servo360(15)
        for i in range(0, 180, 5):
            print(i)
            servo14.girar(i)
            servo15.girar(i)
            sleep(0.2)
        servo14.detener()
        servo15.detener()
    elif i == 19:
        us = Ultrasonico()
        print("Se testeará por 10 segundos")
        start_time = ticks_us()
        while ticks_diff(ticks_us(), start_time)<10_000_000:
            print(us.medir())
            sleep(0.1)
            
            
while True:
    r = int(input('''¿Cuál pin GP quiere testear: 1-15?
0,1			botones
2,3,4		leds
5			buzzer
6 - 12		QTI
13,14,15	Servo

Además
16			Servos 13 y 14 juntos
17			Servos 13 y 15 juntos
18			Servos 14 y 15 juntos
19			Ultrasónico

Indique número:'''))
    test(r)

