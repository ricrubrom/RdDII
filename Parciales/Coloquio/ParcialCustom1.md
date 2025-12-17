Aquí tienes el simulacro de examen basado en los temas de los parciales de 2024 y 2025, formateado en Markdown.

# Simulacro de Examen - Redes de Datos

## Ejercicio 1

¿Cuál de las siguientes afirmaciones es correcta respecto a la capa de Transporte (TCP/UDP)?

### a) UDP garantiza la entrega ordenada de datos si el tamaño del datagrama es menor al MTU

F

### b) En el cierre de conexión TCP, si un extremo envía un FIN, no puede recibir más datos del otro extremo

F

### c) El Control de Flujo en TCP utiliza la ventana deslizante para evitar saturar al receptor

V

### d) UDP realiza control de congestión reduciendo la tasa de envío si detecta pérdida de paquetes

F

### e) El campo checksum en UDP es obligatorio en IPv4 pero opcional en IPv6

F

## Ejercicio 2

Con respecto al protocolo DNS y su funcionamiento:

### a) Una consulta iterativa delega la responsabilidad de encontrar la respuesta final al servidor consultado

F

### b) Los servidores Raíz (Root Servers) almacenan la base de datos completa de todos los dominios de Internet

F

### c) Si un servidor DNS autoritativo recibe una consulta por un registro que no tiene, devuelve un error NXDOMAIN inmediatamente

F

### d) Se utiliza TCP puerto 53 principalmente cuando la respuesta supera los 512 bytes (ej. transferencias de zona o respuestas grandes con DNSSEC)

V

### e) El registro CNAME permite asociar una dirección IP directamente a un alias

F

## Ejercicio 3

Analice el siguiente escenario de correo electrónico:
_Un usuario configura su cliente de correo (Outlook) en su laptop para bajar los correos, borrarlos del servidor y guardarlos localmente._
Indique la opción correcta:

### a) El protocolo utilizado para la descarga es IMAP

F

### b) El cliente utiliza SMTP en el puerto 110 para descargar los correos

F

### c) El cliente utiliza POP3, lo cual explica que los correos se borren del servidor tras la descarga

V

### d) El envío de correos desde la laptop al servidor de salida se realiza mediante POP3 Push

F

### e) Se requiere un registro MX apuntando a la IP de la laptop del usuario para recibir el correo

F

## Ejercicio 4

¿Cuál de las siguientes sentencias sobre IPv6 es verdadera?

### a) El encabezado base de IPv6 tiene un tamaño variable dependiendo de las opciones incluidas

F

### b) Fragmentación: Los routers intermedios pueden fragmentar paquetes si el MTU del siguiente enlace es menor

F

### c) Una dirección de tipo Link-Local (fe80::/10) es enrutable a través de Internet

F

### d) Utiliza el campo Hop Limit que cumple una función análoga al TTL de IPv4

V

### e) El protocolo ARP se sigue utilizando en IPv6 pero encapsulado en paquetes ICMPv6

F

## Ejercicio 5

Suponga que un Host A envía un segmento TCP al Host B. El Host A tiene una ventana de congestión (cwnd) de 8000 bytes y el Host B anuncia una ventana de recepción (rwnd) de 4000 bytes.
¿Cuántos bytes puede enviar el Host A antes de detenerse a esperar un ACK?

### a) 8000 bytes

F

### b) 12000 bytes (la suma de ambas)

F

### c) 4000 bytes (el mínimo entre cwnd y rwnd)

V

### d) Depende del MSS negociado

F

### e) El Host A enviará datos hasta que detecte 3 ACKs duplicados

F

## Ejercicio 6

Indique la opción correcta respecto al direccionamiento y subredes IPv4:

### a) La dirección 172.16.1.255/23 es la dirección de broadcast de su subred

V

### b) La sumarización de las redes 192.168.0.0/24 y 192.168.1.0/24 resulta en la red 192.168.0.0/23

V

### c) Una máscara /28 permite tener 16 hosts utilizables por subred

F

### d) La dirección 127.0.0.50 es una dirección pública válida en Internet

F

### e) Todas las opciones anteriores son falsas

F

## Ejercicio 7

Sobre HTTP y sus versiones:

### a) HTTP/1.0 introdujo las conexiones persistentes por defecto para evitar el handshake TCP en cada objeto

F

### b) El problema de Head-of-Line Blocking en capa de aplicación se soluciona en HTTP/1.1 gracias al Pipelining

F

### c) HTTP/2 utiliza un formato binario y permite multiplexación de streams en una única conexión TCP

V

### d) HTTPS requiere que el servidor DNS soporte registros de tipo "SECURE"

F

### e) En un mensaje HTTP Response, el código 301 indica "Not Found"

F

## Ejercicio 8

Indique cuál de las siguientes opciones es verdadera respecto a DHCP y ARP:

### a) Cuando un cliente DHCP renueva su IP (DHCP Request), siempre lo hace mediante Broadcast

F

### b) ARP Gratuitous se utiliza para detectar conflictos de direcciones IP en la red local

V

### c) Un servidor DHCP debe estar obligatoriamente en la misma subred física que el cliente, no puede estar en otra red

F

### d) La tabla ARP de un host almacena la asignación entre direcciones IP y puertos TCP

F

### e) El mensaje DHCP Offer contiene la dirección MAC del cliente en el campo de dirección IP destino del paquete IP

F

## Ejercicio 9

Indique V o F y justifique:

- En el control de congestión TCP, si ocurre un Timeout (tiempo de espera agotado) antes de recibir un ACK, el emisor reduce su ventana de congestión (cwnd) a 1 MSS y reinicia en modo Slow Start.

V. Eso es lo que ocurre con TCP Reno.

## Ejercicio 10

Indique V o F y justifique:

- Si un paquete IP atraviesa 3 routers desde el origen al destino, la dirección IP de origen y la dirección MAC de origen se modifican en cada salto para reflejar el router que está retransmitiendo el paquete.

F. Solo se modificara la direccion MAC. La IP origen se mantendra la del host origen

