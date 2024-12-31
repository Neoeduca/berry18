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
