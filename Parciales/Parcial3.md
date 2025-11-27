# Parcial 3

## Ejercicio 1

### A

10.0.1.0/24

Comenzamos por la red que necesita 40 hosts, y seguimos para abajo

Se necesitan 6 bits para representar los 40 hosts. Por ende se puede utilizar la red
10.0.1.64/26

En base a las otras redes que sobran, podemos divir en una red para 30 hosts, para la cual tan solo necesitamos 5 bits
10.0.1.128/27

Por ultimo necesitamos una red para 10 hosts, por lo que necesitamos 4 bits
10.0.1.160/28

Para el resto de enlaces podemos utilizar redes /30, pues necesitamos un total de 4 ips por conexion punto a punto
10.0.1.176/30
10.0.1.180/30
10.0.1.184/30
10.0.1.188/30

| Broadcast |   IP red   |   Mascara   | Long Prefijo |
| :-------: | :--------: | :---------: | :----------: |
|   A-R1    | 10.0.1.160 | FF.FF.FF.C0 |     /28      |
|   R1-R0   | 10.0.1.176 | FF.FF.FF.FA |     /30      |
|   R1-R3   | 10.0.1.180 | FF.FF.FF.FA |     /30      |
|   R0-R2   | 10.0.1.184 | FF.FF.FF.FA |     /30      |
|   R3-C    | 10.0.1.128 | FF.FF.FF.B0 |     /27      |
|   R2-R4   | 10.0.1.188 | FF.FF.FF.FA |     /30      |
|   R4-B    | 10.0.1.64  | FF.FF.FF.A0 |     /26      |

### B

El router R0 deberia tener en su tabla

A-R1 y R1-R3 a la izquierda (Digamos Eth0)
R2-R3, R3-C, R2-R4, y R4-B a la derecha (Digamos Eth1)

### C

B puede tener su default gateway hacia el R4 y nada mas, todos los paquetes saldrian para ese lado y luego los routers se encargaran de rutearlo

## Ejercicio 2

2001:db8:1::/48

FFFF:FFFF:FFFF::
FFFF:FFFF:FFFF:FFFF::

Utilizaremos /64 debido a que es el estandar para subnetting en IPv6, puesto que nos da muchas subredes y hosts
Utilizare la red 2001:db8:1:1::/64

El R1 puede ser 2001:db8:1:1::1 y el R3 2001:db8:1:1::2

## Ejercicio 3

### A

A

### B

B

### C

C

### D

D

### E

E

### F

F

## Ejercicio 4

### A

Busca los Mail Exchangers de gmail.com
Se hizo una consulta del registro MX al dominio gmail.com de forma recursiva, pues se puede ver como en las flags esta la flag de RD y RA (Recursive desired y Recursive available)

### B

Se utilizo UDP en el puerto 53 al servidor 8.8.8.8, como se puede ver abajo del todo donde dice SERVER

### C

Deberia consultar por el registro A o AAAA del registro del MX de mayor prioridad

### D

Utilizara TCP en el puerto 25 (Default de SMTP)

### E

Podria mandar un Reset de la conexion TCP, un Timeout (no responde) o un codigo SMTP 421 y el servidor SMTP deberia o probar con otro mail exchanger o descartar el correo

