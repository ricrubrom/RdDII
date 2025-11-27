# Parcial 1 - 13/12/23

## Ejercicio 1

Ruteo Dinamico

## Ejercicio 2

Cual de las siguientes opciones es verdadera?

- Un servidor tiene una dirección IP permanente. V
- Un cliente está siempre escuchando a que el servidor le envíe algo.
- En DNS, el TTL indica el tiempo máximo que se puede esperar una respuesta de un servidor.
- No es posible que un cliente y un servidor ejecuten en la misma máquina.
- No pueden existir dos servidores diferentes escuchando en el mismo puerto pero uno en TCP y el otro en UDP.
- Todas las opciones son verdaderas.

## Ejercicio 3

Ruteo Dinamico

## Ejercicio 4

- Si el servidor cierra la sesión después de enviar el objeto requerido es no persistente. V
- HTTP es capaz de hacer un seguimiento de las acciones que va desarrollando un cliente. F
- Si se tiene una página HTML con 5 imágenes entonces por HTTP/1.0 serán necesarios hacer 6 requerimientos pero por HTTP/1.1 solo uno. F
- En el método GET los datos se envían en cuerpo del mensaje. F
- Ninguna opción es verdadera. F

## Ejercicio 5

### A

No es autoritativa, pues la respuesta no proviene de cualquiera de los servidores de autoridad, ademas que la flag de autoridad no esta activa.

### B

Se deberia hacer a cualquiera de los 3 servidores ahi listados. Se puede saber si una respuesta es autoritativa si la flag de aa esta activa y si la ip de la respuesta viene de uno de estos servidores. Sabemos tambien las IP por la misma salida del comando en la seccion de Authority Section

### C

Se esta solicitando el registro A, pues se puede ver en la seccion de Question

### D

Realizo la consulta a un resolver recursivo con IP 209.144.50.138

## Ejercicio 6

- SMTP Para envio, puerto 25
- POP 3 con puerto 110, o IMAP con puerto 143 para recepcion
- Entre servidores SMTP, puerto 25

## Ejercicio 7

Que una consulta DNS sea recursiva significa que el cliente envia la consulta y espera a la respuesta final, El servidor que recibe la consulta es el que se encarga de consultar a los demas servidores hasta encontrar un servidor que tenga la ip almacenada, la cual le devuelve al cliente.

