# -*- coding: utf-8 -*-

import turtle  # importo una librería que me permite generar gráficas de ventana

window = turtle.Screen()  # creo una nueva ventana
dave = turtle.Turtle()  # creo una tortuga (punto de partida que ira graficando)

dave.forward(50)  # creo una linea 50 unidades a la derecha
# roto el angulo de movimiento 90 grados, es decir, proximo movimiento será hacia arriba
dave.left(90)
dave.forward(50)  # ahora me muevo linealmente 50 unidades hacia arriba
dave.left(90)  # ... loop del proceso hasta formar un cuadrado
dave.forward(50)
dave.left(90)
dave.forward(50)
dave.left(90)

# lo coloco para que la ventana no se me cierre apenas finalice la animación
turtle.mainloop()
