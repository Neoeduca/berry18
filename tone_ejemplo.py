from tone import Buzzer

buzzer = Buzzer(5)

buzzer.on(440) #Dejo encendido un LA
sleep(2)
buzzer.off()   #Apago el buzzer



buzzer.on(261) #Dejo encendido un DO
sleep(2)
buzzer.on(532) #Cambio a un DO Mayor
sleep(2)
buzzer.off()


buzzer.tone(261, 0.5, 0.1)  #Toco un DO por 0.5s y luego un silencio de 0.1 (entre notas)
buzzer.tone(440, 0.5, 0.1)
buzzer.tone(532, 0.5, 0.1)
buzzer.tone(261, 0.5) #Idem, pero no tiene un silencio al final