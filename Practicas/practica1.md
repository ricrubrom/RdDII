# Practica 1

## Ejercicio 1

B

Modelo TPC/IP tiene 4 capas (Acceso a red, Internet, Transporte, Aplicacion)

## Ejercicio 2

### Inciso A

Los dispositivos que necesitan una direccion MAC son:

- Bridge/Switch (0-1 direccionesn), Capa Enlace
- Laptop con NIC Wifi y Ethernet (2 direcciones), Capa Aplicacion
- Switch ATM (0 direccion), Capa Enlace
- PC (Si tienen NIC, 1 direccion por NIC), Capa Aplicacion
- Smartphone (0-3, Depende si tiene wifi, bluetooth o un adaptador Ethernet), Capa aplicacion
- Bridge/Hub remoto (1 direccion), Capa enlace
- NIC Wifi (1 Direccion), Capa Enlace
- NIC Ethernet (1 Direccion), Capa Enlace
- Router Wifi y LAN (2 Direcciones), Capa Red

Fisica -> Bits
Enlace -> Tramas
Red -> Paquetes
Transporte -> Segmentos
Applicacion -> Data

### Inciso B

48 bits, 2 partes de 24

La primera parte OUI (Organizationally Unique Identifier), Identificar fabricante, Administrada por IEEE.

La segunda parte identifica cada dispositivo en si.

### Inciso C

Las invalidas son

- fe:ga:87:12:64:3a // Tiene una g
- ad:e6:b7:42:ef    // 5 bytes

La ultima direccion es valida, pero no puede ser de origen, debido a que es de broadcast.

### Inciso D

Todo F es broadcast
Si el bit menos significativo del primer octeto es 1 entonces es multicast
El resto son unicast

### Inciso E

EUI-48 -> 802.xx
EUI-64 -> 802.1CQ, PALMA

## Ejercicio 3

B, Origen

## Ejercicio 4

Todos switches solamente tendrian la MAC de Alejandria

## Ejercicio 5

C, Aleatorio

## Ejercicio 6

- 10GBaseLR
- 802.15.4
- 100GBASE-LR4
- 802.11n

## Ejercicio 7

C, Conjunto de destinos

## Ejercicio 8

C, menos el que recibio

## Ejercicio 9

### Inciso A

Dominio de colisiones es aquel en el que pueden ocurrir colisiones de paquetes. Esta separado por switches.

### Inciso B

Aumenta

### Inciso C

4 Dominios

## Ejercicio 10

B, IBSS

## Ejercicio 11

B, MAC Destino

## Ejercicio 12

B, tiempo aleatorio

Porque se espera un tiempo aleatorio, ante una colision no siempre se envian en el mismo orden

## Ejercicio 13

El dominio de broadcast es aquel en el que se pueden enviar mensajes de difusion. Esta separado por Routers. Hay un unico dominio de broadcast en ese punto

## Ejercicio 14

B, No

## Ejercicio 15

4 Direcciones MAC

## Ejercicio 16

D, Fisica estrella, Logica Bus?????

## Ejercicio 17

Switch

## Ejercicio 18

D, 4096

## Ejercicio 19

B, Aumenta

## Ejercicio 20

C, No cambia

## Ejercicio 21

8 Dominios de broadcast

## Ejercicio 22

Trunk

## Ejercicio 23

802.11n y 802.11b

## Ejercicio 24

### Inciso A



### Inciso B



### Inciso C



### Inciso D



## Ejercicio 25

C, Store and forward

## Ejercicio 26

### Inciso A



### Inciso B



## Ejercicio 27

### Caso 1

Destino Broadcast
Origen  52 54 00 12 34 56
Protocolo ARP

### Caso 2

Destino 52 54 00 12 34 57
Origen  52 54 00 12 34 56
Protocolo IPv4

### Caso 3

Destino 00 0d bc 14 d1 42
Origen  00 0d bc 53 1e c0
Protocolo 802.1Q//VLAN
Protocolo de la VLAN IPv4


### Caso 4

Destino 00 3a 99 69 71 c0
Origen  00 13 02 9f 22 e0
Receptor e0 5f b9 e5 b0 ac
Transmisor 00 00 aa aa 03 00
