from motores import Auto
from time import sleep

autito = Auto(14,15)  #Pines donde tengo conectado los motores
autito.probar(94, 88) #función para probar hasta encontrar aquellos que me permiten ir derecho
autito.angulos(94,88)  #Ajusto los angulos que probé anteriormente

#Ciclo de movimiento
autito.avanzar()
sleep(3)
autito.detener()
sleep(1)
autito.derecha()
sleep(3)
autito.detener()
sleep(1)
autito.izquierda()
sleep(3)
autito.detener()
sleep(1)
autito.retroceder()
sleep(3)
autito.detener()
