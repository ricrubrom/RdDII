# Simulacro de Examen - Redes de Datos (Nivel Parcial)

**Instrucciones:** Seleccione la o las opciones correctas. Puede haber ninguna, una o varias respuestas verdaderas en cada punto.

## Ejercicio 1

Dada la red IPv4 **172.16.20.0/22**, ¿cuáles de las siguientes direcciones IP son direcciones de **host válidas** utilizables para asignar a una PC?

### a) 172.16.20.255

V

### b) 172.16.23.255

F

### c) 172.16.22.0

V

### d) 172.16.24.1

F

### e) 172.16.20.0

F

## Ejercicio 2

Con respecto al establecimiento y cierre de conexiones TCP, marque las correctas:

### a) El consumo de números de secuencia (SEQ) ocurre tanto al enviar datos como al enviar los flags SYN o FIN

V

### b) El flag RST se utiliza para rechazar una conexión cuando no hay un servicio escuchando en el puerto destino

V

### c) El "Three-Way Handshake" garantiza que ambos extremos estén listos y hayan acordado los números de secuencia iniciales

V

### d) Una vez enviado un segmento con el flag FIN, ese extremo cierra su conexión inmediatamente y no puede recibir más datos

F

### e) El ACK en el saludo de tres vías confirma el número de secuencia del otro extremo sumándole 1

V

## Ejercicio 3

Sobre el sistema DNS y sus registros:

### a) Un registro de tipo **NS** (Name Server) indica qué servidor es autoritativo para una zona específica

V

### b) Es obligatorio que todo registro **MX** apunte a un nombre de dominio que tenga un registro **CNAME** asociado

F

### c) Las consultas iterativas generan menos carga en el servidor Raíz (Root) que las consultas recursivas puras hechas hacia él

V

### d) El archivo de zona inversa utiliza registros de tipo **PTR** para mapear IPs a nombres

V

### e) DNS utiliza exclusivamente UDP puerto 53 para todas sus operaciones

F

## Ejercicio 4

Analice las siguientes afirmaciones sobre IPv6:

### a) La dirección `::1` es funcionalmente equivalente a `127.0.0.1` en IPv4

V

### b) Una dirección que comienza con `fe80::` es enrutable en internet

F

### c) IPv6 elimina el uso de NAT (Network Address Translation) como necesidad para ampliar el espacio de direcciones

V

### d) El campo "Next Header" en IPv6 cumple una función similar al campo "Protocol" en IPv4

V

### e) El tamaño mínimo del encabezado IPv6 es de 20 bytes

F

## Ejercicio 5

Sobre los protocolos de Correo Electrónico (SMTP, POP3, IMAP):

### a) SMTP utiliza el puerto 25 para la comunicación entre servidores de correo (MTA a MTA)

V

### b) IMAP (puerto 143/993) permite gestionar carpetas directamente en el servidor y mantiene el estado de los mensajes (leído/no leído)

V

### c) Si un usuario envía un correo desde su celular, utiliza POP3 para subir el correo a su servidor

F

### d) El registro SPF en DNS ayuda a prevenir el spoofing indicando qué IPs están autorizadas a enviar correo por un dominio

V

### e) SMTP es un protocolo basado en texto ASCII, similar a HTTP/1.1

V

## Ejercicio 6

En una red Ethernet con switches y routers, cuando un Host A envía un paquete IP a un Host B que está en una red remota:

### a) La dirección MAC de origen en la trama cambia en cada salto de router

V

### b) La dirección IP de destino en el paquete cambia en cada salto de router para indicar el próximo gateway

F

### c) El TTL del paquete IP se decrementa en 1 cada vez que atraviesa un switch de capa 2

F

### d) El Router recalcula el Checksum del encabezado IPv4 antes de reenviar el paquete

V

### e) La dirección MAC de destino de la trama que sale del Host A corresponde a la interfaz del Default Gateway

V

## Ejercicio 7

¿Cuáles de las siguientes opciones son verdaderas respecto a HTTP?

### a) Los códigos de estado 4xx indican errores del lado del cliente (ej. Recurso no encontrado o falta de permisos)

V

### b) HTTP/1.1 requiere abrir una nueva conexión TCP por cada imagen que se descarga de una página web

F

### c) En una petición GET, los datos enviados por el usuario pueden verse en la URL

V

### d) HTTP es un protocolo "Stateful" (con estado), por lo que recuerda nativamente las peticiones anteriores del usuario

F

### e) El header `Host` es obligatorio en las peticiones HTTP/1.1

V

## Ejercicio 8

Respecto a la fragmentación en redes IP:

### a) En IPv4, si el bit DF (Don't Fragment) está en 1 y el paquete es mayor al MTU, el router lo descarta y envía un ICMP

V

### b) En IPv6, la fragmentación solo puede ser realizada por el nodo origen, nunca por routers intermedios

V

### c) El reensamblado de los fragmentos se realiza en cada router intermedio para verificar el checksum

F

### d) El campo "Offset" indica la posición del fragmento en relación con el inicio del paquete original

V

### e) Todos los fragmentos de un mismo paquete original comparten el mismo valor de "Identification" (ID)

V

## Ejercicio 9

Indique V o F y justifique:
_El mecanismo de **Control de Flujo** en TCP utiliza la variable `cwnd` (Congestion Window) para evitar desbordar el buffer del receptor._

F. Utiliza la rwnd, que es la ventana de recepcion. Control de congestion utiliza cwnd

## Ejercicio 10

Indique V o F y justifique:
_Si un servidor DHCP se encuentra en una subred distinta a la del cliente, es imposible que el cliente obtenga dirección IP, ya que el mensaje DHCP DISCOVER es de broadcast y los routers no reenvían broadcast por defecto._

F. Existe el DHCP Proxy, en el que el router de la red contacta al servidor DNS de manera unicast, y luego le asigna una ip al host

