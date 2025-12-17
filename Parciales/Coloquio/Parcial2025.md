Aquí tienes el examen transcrito en formato Markdown, tal como me pediste.

# Parcial 2025 - 19/02/2025

## Ejercicio 1

¿Cuál de las siguientes opciones es verdadera con respecto a IPv4?

### a) No posee control de errores. Utiliza ICMP para esa funcionalidad

F

### b) Si se pierde un fragmento de un paquete IP fragmentado, el receptor debe solicitarle al emisor que le envíe el fragmento faltante

F

### c) El valor del Header Checksum no debe recalcularse en cada router ya que el contenido de la cabecera IP no se modifica entre un origen y un destino

F

### d) Si el campo TTL llega 0 en un router y éste lo tiene que descartar, lo hace silenciosamente. No le manda ningún aviso al origen

F

### e) Ninguna opción es verdadera

V

## Ejercicio 2

¿Cuál de las siguientes opciones es verdadera con respecto a ARP?

### a) Es un protocolo estático que debe ser configurado previamente para funcionar correctamente

F

### b) Se encapsula dentro de un paquete IPv4

F

### c) Al llegar un mensaje ARP Request a un router, éste lo retransmite por todos los puertos menos por el que lo recibió

F

### d) Permite obtener la dirección IPv4 asociada a una dirección MAC

F

### e) Ninguna de las opciones es verdadera

V

## Ejercicio 3

Dada las siguientes sentencias con respecto al DNS, indicar cuáles son verdaderas:

### a) DNS utiliza TCP para la transferencia de zona entre servidores

V

### b) Un root-server puede devolver la IP de cualquier nombre de dominio que se le consulte

F

### c) El registro SOA contiene la cantidad total de registros cargados en la zona

F

### d) Un nombre de dominio puede tener asociado un registro A y AAAA en forma simultánea

V

### e) Solo se puede definir un registro MX por dominio

F

## Ejercicio 4

¿Cuáles de las sentencias son verdaderas con respecto a TCP?

### a) Divide un stream de datos en pedazos llamados segmentos

V

### b) El MSS se indica en el saludo de 3 vías y se puede modificar a lo largo de la sesión

F

### c) Si el servidor no tiene un servicio escuchando en un puerto, responderá con un segmento con los flags R y A seteados ante un inicio de sesión

V, manda el ACK del SYN del cliente

### d) Como un canal TCP es unidireccional se necesitan 2 sesiones TCP simultáneas para poder enviar y recibir datos

F

### e) Un extremo enviará un TCP reconociendo un segmento aún cuando haya segmentos anteriores que no arribaron

F

## Ejercicio 5

¿Cuáles de las opciones son correctas con respecto al protocolo HTTP?

### a) Las versiones HTTP/1.1 y HTTP/2 son compatibles entre sí

F

### b) Ambos ejecutan sobre TCP y soportan conexiones persistentes

V

### c) En ambos protocolos el cliente puede solicitar y recibir varios objetos simultáneamente

F

### d) En HTTP/1.1 existe un funcionamiento similar al Server Push de HTTP/2

F

### e) Ambos protocolos utilizan los mismos métodos HTTP y códigos de estado

V

## Ejercicio 6

Indique V o F y justifique la respuesta:

- Si en UDP, un extremo recibe un datagrama fuera de orden lo descartará silenciosamente

F. UDP no tiene control de orden ni de duplicados, se los envia directamente a la aplicacion

## Ejercicio 7

Marque las opciones correctas sobre el protocolo DHCP:

### a) El mensaje DHCP Discover siempre es enviado a la dirección 255.255.255.255

V, No conoce nada el host, por ende manda broadcast

### b) DHCP utiliza TCP como protocolo de transporte

F

### c) DHCP solo permite asignar IP, máscara de subred, gateway y DNS

F, Permite tambien NTP TFTP nombre de host MTU rutas etc

### d) Al ser ofrecida por un servidor DHCP, el cliente se asegura que nadie más tiene asignada esa dirección IP y no necesita comprobar que otro la tenga asignada

F

### e) El mensaje DHCP Request puede ser enviado por el cliente o el servidor

F

### f) El mensaje DHCP Offer puede ser enviado en forma unicast o broadcast

V

## Ejercicio 8

Indicar cuales de las siguientes opciones son correctas:

### a) En IPv6 un paquete sólo puede ser fragmentado por el nodo origen

V

### b) La dirección de red 172.10.0.64/26 tiene a la IP 172.10.0.125/26 como broadcast

FF.FF.FF.11000000

F, es .127

### c) Un paquete fragmentado no puede volver a ser fragmentado

F

### d) La dirección 224.0.0.0/24 es una dirección válida para asignar a una red

F, Es multicast

### e) Las direcciones 127.0.0.1 y ::1 cumplen la misma función en IPv4 e IPv6 respectivamente

V

## Ejercicio 9

Responder V o F y justificar:

- En control de congestión cuando se alcanza el límite ssthresh se entra en la fase Slow Start

F. Al superar el ssthresh se entra a la fase congestion avoidance

## Ejercicio 10

En base a la siguiente topología y teniendo en cuenta que Rtr-A hace NAT para Red_Compras. Indique cuáles de las siguientes opciones son correctas considerando un paquete que le envía SRV_WEB a PC-A cuando dicho paquete se encuentra en la Red ISP.

_(Ver diagrama en la imagen original: PC-A [Red Compras] <-> Rtr-A <-> [Red ISP] <-> Rtr-B <-> SRV_WEB)_

### a) IP destino: 172.16.2.2

F

### b) MAC origen: MAC_Rtr-B_eth0

V

### c) IP destino: 163.10.5.129

V

### d) MAC origen: MAC_SRV_WEB_eth0

F

### e) MAC destino: MAC_PC-A_eth0

F

