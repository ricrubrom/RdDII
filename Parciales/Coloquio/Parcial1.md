# Parcial 1 - 11/12/2024

## Ejercicio 1

¿Cuáles de las siguientes opciones son verdaderas con respecto a HTTP/1.1?

### a) Por defecto, las sesiones son persistentes

V

### b) Es un protocolo binario, por lo que lo hace compatible con HTTP/2

F

### c) El servidor mantiene el estado de todas las sesiones activas

F

### d) En el método GET los parámetros se pasan en el body del mensaje

F

### e) Si se usa HTTPS, todo el mensaje HTTP viaja encriptado

V

## Ejercicio 2

Indique cuál de las siguientes opciones es verdadera con respecto a IPv6:

### a) Un nodo sólo puede tener configurada una dirección IPv6 por interface de red

F

### b) 2001::1bb3:9ca:1::1/64 es una dirección IPv6 válida

F

### c) El protocolo Neighbour Discovery requiere ICMPv6 para funcionar

V

### d) El checksum en IPv6 permite detectar errores en un paquete

F

### e) No contiene ningún mecanismo para poder extender el protocolo

F

## Ejercicio 3

Indique V o F y justifique su respuesta:

- En HTTP/2, no es posible solicitar un nuevo recurso sino se recibió completamente el recurso solicitado previamente

F. Es posible debido a que en HTTP/2 se implemento la multiplexacion de peticiones sobre una unica conexion.

## Ejercicio 4

Juan envía un mail desde su cuenta <juan@micorreo.com> a María cuya cuenta es <maria@abc.com>. Indique cuáles de las siguientes opciones son correctas.

### a) La PC de María consultará por el registro MX del dominio micorreo.com

F

### b) María podría utilizar el protocolo SMTP para leer el correo que le envió Juan

F

### c) El servidor correo del dominio abc.com recibirá una conexión TCP al puerto 25 desde el servidor de correo del dominio micorreo.com

V

### d) María podría utilizar IMAP para leer el correo que le envió Juan

V

### e) Como María ve la misma estructura de carpetas y mails en su PC y en su teléfono celular, entonces está usando POP3

F

## Ejercicio 5

En base a la siguiente captura, seleccione las respuestas correctas.

`IP 1.1.1.1.80 > 2.2.2.2.19362: Flags [SA], seq 26454, ack 27316, win 38200, MSS 1000`

### a) 1.1.1.1 podrá enviar un máximo de 38200 bytes de datos a 2.2.2.2 sin recibir ACK

F

### b) 1.1.1.1 está iniciando una conexión a 2.2.2.2 (es decir, 1.1.1.1 será el cliente)

F

### c) 2.2.2.2 le podrá enviar a 1.1.1.1 hasta 38 segmentos de tamaño máximo sin recibir un ACK

V

### d) Si 2.2.2.2 intenta enviar más de 38200 bytes de datos a 1.1.1.1, este activará el mecanismo de control de congestión

F

### e) El número de secuencia inicial de 2.2.2.2 es 27315

V

## Ejercicio 6

Indicar cuál de las siguientes opciones son correctas con respecto a UDP:

### a) Si se envía un mensaje a un puerto de un nodo en el que no está escuchando un servicio, ese nodo contestará con un mensaje ICMP Port Unreachable

V

### b) Si llega un mensaje duplicado, el receptor lo descartará sin avisarle al emisor

F

### c) Un receptor ordenará las datagramas antes de pasarlos a la capa de aplicación

F

### d) Ninguna de las opciones anteriores es verdadera

F

## Ejercicio 7

Indique cuáles de las siguientes opciones son verdaderas con respecto a DNS:

### a) Para funcionar utiliza el puerto 53 en UDP/TCP

V

### b) Si un administrador desea modificar el TTL de un registro lo puede hacer en cualquier servidor que tenga ese registro en su caché

F

### c) La consulta que se hace desde una PC a su DNS local es iterativa

F

### d) Un servidor DNS puede ser configurado para no responder recursivamente

V

### e) Para solicitar una dirección IPv4 o IPv6 se debe consultar por el registro A

F

## Ejercicio 8

¿Cuáles de las siguientes opciones son verdaderas con respecto a IPv4?

### a) Si tengo una red con 30 dispositivos, entonces la IP 163.10.20.32/27 puede usarse para cubrirla completamente

V

### b) Si un paquete es fragmentado por un router, el siguiente router en el camino también siempre lo debe rearmarlo

F

### c) El valor 1 del campo Protocol indica que en el payload va un mensaje HTTP

F

### d) La dirección IPv4 200.5.8.0/22 sumariza las siguientes redes: 200.5.8.0/23, 200.5.10.0/24 y 200.5.11.0/24

V

### e) Si un router decrementa el campo TTL de un paquete a 0, lo descarta y no le indica nada al emisor

F

## Ejercicio 9

Indicar V o F y justificar:

- En control de congestión, un emisor pasa del modo Slow Start a Congestion Avoidance cuando recibe 3 ACKs duplicados

F. Pasa a congestion avoidance cuando se supera el ssthresh. Al recibir 3 ACKs duplicados pasa a slow start o a fast recovery

## Ejercicio 10

Indique cuáles de las siguientes opciones son verdaderas:

### a) En DHCP, el orden del intercambio de mensajes es: Discover, Offer, Request y ACK

V

### b) Si el emisor y el receptor están en la misma red, entonces el ARP Request puede ser de tipo Unicast

F o V. Preguntar al profe si cuenta el caso de renovar la entrada de la tabla ARP

### c) El tamaño de ventana de recepción en TCP se anuncia en el saludo de 3 vías y se puede ir modificando a lo largo de la comunicación

V

### d) La dirección fe80::4437:39ff:fe65:f518/64 es una dirección IPv6 válida para asignar a un servidor web que deba ser accesible en Internet

F

### e) En cada datagrama UDP sólo es posible transportar un único paquete QUIC

F

