# Parcial 3

## Ejercicio 1

### A

Hay 8 Dominios de Broadcast

Utilizando el bloque 10.0.1.0/24

Comenzando por la red con mas hosts, necesitamos un total de 43 ips en esa red (40 hosts+R4+Red+Broadcast)
Puedo utilizar 6 bits de host para identificar los hosts, quedando con 26 bits de mascara
10.0.1.0/26
FFFFFFA0

Luego para la red del host C necesitamos un total de 33 ips (30 hosts, R3, Red, Broadcast)
Por ende vamos a utilizar la siguiente /26
10.0.1.64/26

Para la red de A necesitamos 13 ips (10 hosts, R1, Red, Broadcast), por lo que podemos utilizar un /28
10.0.1.128/28

Para las 5 redes restantes puedo utilizar un /30, pues solo necesito 4 ips (Los dos punto a punto, red y broadcast)
10.0.1.144/30
10.0.1.148/30
10.0.1.152/30
10.0.1.156/30
10.0.1.160/30

Ahora hago la tabla

| Dominio |    Red     |   Mascara   | Long Prefijo |
| :-----: | :--------: | :---------: | :----------: |
|  A-R1   | 10.0.1.128 | FF.FF.FF.F0 |     /28      |
|  R1-R0  | 10.0.1.144 | FF.FF.FF.FA |     /30      |
|  R1-R3  | 10.0.1.148 | FF.FF.FF.FA |     /30      |
|  R0-R2  | 10.0.1.152 | FF.FF.FF.FA |     /30      |
|  R3-R2  | 10.0.1.156 | FF.FF.FF.FA |     /30      |
|  R3-C   | 10.0.1.64  | FF.FF.FF.A0 |     /26      |
|  R2-R4  | 10.0.1.160 | FF.FF.FF.FA |     /30      |
|  R4-B   |  10.0.1.0  | FF.FF.FF.A0 |     /26      |

### B

Supongamos que eth0 esta a la izquierda y eth1 a la derecha

| Red Destino | Mask |  Next Hop  | Interfaz |
| :---------: | :--: | :--------: | :------: |
|  10.0.1.0   | /26  | 10.0.1.154 |   eth1   |
|  10.0.1.64  | /26  | 10.0.1.145 |   eth0   |
| 10.0.1.128  | /28  | 10.0.1.145 |   eth0   |
| 10.0.1.144  | /30  |     --     |   eth0   |
| 10.0.1.152  | /30  |     --     |   eth1   |
| 10.0.1.148  | /30  | 10.0.1.145 |   eth0   |
| 10.0.1.156  | /30  | 10.0.1.154 |   eth1   |
| 10.0.1.160  | /30  | 10.0.1.154 |   eth1   |

### C

| Red Destino | Mask | Next Hop | Interfaz |
| :---------: | :--: | :------: | :------: |
|   0.0.0.0   |  /0  | 10.0.1.1 |   eth0   |

## Ejercicio 2

2001:db8:1::/48

Debido a la gran cantidad de IPs de IPv6, voy a utilizar un /64 que nos permite generar muchas redes con millones de hosts
La red que utilizaria seria 2001:db8:1::/64, con los dos dispositivos teniendo las siguientes ips

R1=2001:db8:1::1
R3=2001:db8:1::2

## Ejercicio 3

MSS=1400B

### A

El objetivo de Control de Flujo es no inundar al servidor de peticiones, mientras que el objetivo de Control de Congestion es evitar congestionar la red en si.

### B

Control de congestion domina entre T=1 y T=33, mientras que Control de congestion domina entre T=33 y T=39

### C

En T=3 Se encuentra en Slow Start, pues esta creciendo exponencialmente, se trata de una fase de control de congestion

En T=27 se encuentra en Congestion Avoidance, pues esta creciendo linealmente. Tambien se trata de una fase de control de congestion

### D

Como se puede ver, en T=4 (CWND=8) pasa de slow start a Congestion Avoidance, es decir, que el ssthresh es 8, y tanto viendo la figura como contando nosotros mismos, podemos obtener que para T=6 el CWND es 10.

### E

En T=12 detecta un triple ACK, ante lo cual realiza fast recovery, quedando el ssthresh a la mitad del CWND maximo alcanzado, en este caso 15/2=7.5->8, y asigna CWND a este mismo ssthresh

T=19 detecta un timeout, lo cual se puede ver ya que pasa de 15 a 1 en un instante. Hace la misma cuenta para el ssthresh, este quedando en 8 otra vez, pero el CWND vuelvea hacer slow start desde 1

### F

Como el MSS=1400B, y en el tramo final es una recta plana con cwnd=18, la ventana que debe devolver es
Window=18x1400=25200. Como se puede ver, el valor entra en el limite de 16 bits, por lo que no es necesario el escalado

## Ejercicio 4

### A

El cliente consulto por los Mail Exchangers de gmail.com

El tipo de registro es MX
El registro que consulta es gmail.com
Y lo hace de forma recursiva, pues se ve en las flags tanto rd(Recursion Desired) y ra(Recursion Available)

### B

Realizo la consulta al servidor 8.8.8.8 utilizando UDP en el puerto 53, tal como se ve en la seccion SERVER

### C

Debe consultar la direccion IP (tipo A) del registro gmail-smtp-in.1.google.com?

### D

Utiliza el protocolo TCP en el puerto 25 (Default de SMTP)

### E

Puede rechazar la conexion de 3 formas

Mandar un RESET de la conexion TCP
No responder y mandar un timeout
Codigo SMTP 521

