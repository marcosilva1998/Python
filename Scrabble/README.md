# ScrabbleAR-Grupo29

Integrantes:

  Batisti Matias, Legajo: 15083/0
  Delmas Leonardo, Legajo: 15993/3
  Silva Moreno Marco Natan, Legajo: 16234/2

El juego:

  ScrabbleAR es un juego basado en el popular juego de mesa Scrabble, que consiste en formar palabras de dos o más letras, y colocarlas horizontal o verticalmente sobre un tablero de 15x15 casillas, de manera que puedan ser leídas de izquierda a derecha ó de arriba hacia abajo. A diferencia del Scrabble tradicional, para simplificar la estrategia del juego, las palabras no deben cruzarse. En ScrabbleAR se juega contra la computadora y se re-definen algunas de las reglas del juego original. En particular, respecto a las palabras a construir, sólo se podrán utilizar palabras clasificadas como adjetivos, sustantivos y verbos, de acuerdo a cómo se configure el juego. También es posible configurar la cantidad de fichas los puntajes de las mismas y el tiempo.

  Partida:

  Al comenzar la partida, se le asigna 7 fichas a ambos jugadores para que posteriormente(de forma aleatoria) se indique quien empieza primero.
  El juego se termina si: se acaban las fichas, si el tiempo se acaba , ó en caso de que el jugador no disponga mas intentos de intercambio de fichas(dispone de 3 intentos de intercambio), deben quedar menos de 50 fichas en la bolsa y haber sucedido al menos diez rondas, el jugador tendrá la opción de finalizar la partida. Al finalizar, de acuerdo a lo establecido con anterioridad, se procederá a evaluar puntajes y determinar un ganador.

  En el tablero existen ciertas casillas que pueden tanto beneficiarte como perjudicarte: multiplica los puntos de la letra x2 ó x3 y resta -2 o -3 a la palabra, de acuerdo a la casilla/s ocupadas.    

  La partida pospuesta permanece guardada hasta que se determine un ganador, luego de eso la partida se elimina. Esto fue definido en base a la posibilidad de multiples usuarios y la limitación de poder posponer una sola partida.  

El programa:

  El programa principal es ScrabbleAR.py, su ejecución requiere un IDE que admita Python 3.6.8 y las dependencias declaradas en la sección 'Dependencias' de este archivo. Las dependencias pueden instalarse mediante el comando 'pip install' luego de instalar Python versión 3.6.8 ó posterior. Para abrir el juego deberá ejecutar el programa principal.
  Para instalar las dependencias desde requirements.txt utilizar: pip install -r requirements.txt .

  Carpetas contenidas en ScrabbleAR-Grupo29:

    ScrabbleAR_Datos
    ScrabbleAR_Imagenes_png
    ScrabbleAR_Py
    ScrabbleAR_Sonidos

  Dependencias:

    Python 3.6.8
    Pattern 3.6
    PySimpleGUI 4.22.0
    Playsound 1.2.2
    Tkinter 2.7

  Licencias:

    Playsound: TaylorSMarks/playsound is licensed under the MIT License(https://github.com/TaylorSMarks/playsound).
    Sonidos extraidos de : https://www.zapsplat.com/sound-effect-categories/.
    Fondo blanco obtenido : <a href="https://www.vecteezy.com/free-vector/white-texture%22%3EWhite Texture Vectors by Vecteezy</a>.
    Fuente utilizada en el diseño de las imagenes: CoffeeTin Initials.ttf; Diseñador:	Rick Mueller; Licencia: libre;
    Link:	http://moorstation.org/typoasis/designers/mueller/index.htm.

  Consideraciones:

    El sonido se ejecutará en Linux, pero debido a que la dependencia 'playsound' no tiene la funcionalidad 'block' disponible para Linux se producirá un delay, para mas información acceda a https://github.com/TaylorSMarks/playsound.
    Puede ocurrir un error si , se cierra la partida con la X mientras que hay algun pop up abierto , debido a que no podemos deshabilitar momentaneamente la X, podriamos deshabilitarla permanentemene si se requiere.
