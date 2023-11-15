una loopera generativa

para cocrear con

Miel de Purga,

en pos de cerrar el MASS Encuentro, en Cali, Colombia.

Se utilizó whisper.cpp para ayudar la transcripción:


<img src="https://i.imgur.com/QYMjJ20.png">

la transcripción se aparejó a los loops

<img src="https://i.imgur.com/HszRXVH.png">

# Registro de proceso

## Primera versión
## Release notes
loopera de videos hecha con python y mpv inspirada en relatos de estallidos.

Tiene dos modos: secuencial y overlap.

Puedo controlar con el teclado tiempo de espera entre una aparición de próxima camada de videos o video, y la cantidad de videos a mostrar de una sola vez en modo overlap.

En un uso final (en esta versión) solo se verían los videos entrando y saliendo, ya que mandaría los videos a la pantalla final, no mostrando la interfaz con las letras. Esto porque considero bastante feo lo que imprime en consola en este momento de desarrollo. Al tener las transcripciones puedo aparejar los clips con las preguntas y respuestas - en una versión siguiente.

## Demo
[![Watch the video](https://i.imgur.com/iQkfcTJ.png)](https://youtu.be/Y5y7eKpcQfQ?si=_L5aUtEooRRSbce5)


## Segunda versión (actual)
## Release notes
loopera de videos hecha con python y mpv inspirada en relatos del estallido Colombiano, contado por estudiantes de danzas de UniValle. En colaboración con el proyecto de Javier Blanco.

Esta loopera tiene dos modos: secuencial y overlap.

Puedo controlar con el teclado tiempo de espera entre una aparición de próxima camada de videos o video, y la cantidad de videos a mostrar de una sola vez en modo overlap.

En un uso final (en esta versión) puedo elegir que se vean solo los videos entrando y saliendo, ya que puedo mandar los videos a la pantalla final, no mostrando la interfaz con las letras. Sino tengo las transcripciones aparejadas a los clips con las preguntas y respuestas - por lo que podemos mostrar todo en lo mismo, o una cosa en cada pantalla.

## video
[![Watch the video](https://i.imgur.com/NfwnMr4.png)](https://www.youtube.com/watch?v=xS7I7Vy3uNs)


///

# implementación en JS
## Correr

Levantar un local file server en este directorio, por ej

http-server --cors

luego abrir el archivo en el navegador

index_loopera.html

# Implementacion en python

micromamba activate video

python3 main.py
