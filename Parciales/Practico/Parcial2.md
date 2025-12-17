# Parcial 2

## Ejercicio 1

### A

10.0.1.128/25 = 000001010.000000000.00000001.10000000
11111111.11111111.11111111.10000000

Debido a que tengo unicamente conexiones punto a punto, voy a utilizar /30, pues necesito 2 direcciones por enlace mas las de red y broadcast

Necesito un total de 9 redes

- 10.0.1.132/30
  - 10.0.1.133 → A
  - 10.0.1.134 → R1
  - 10.0.1.135 → Broadcast
- 10.0.1.136/30
  - 10.0.1.137 → R1
  - 10.0.1.138 → S
  - 10.0.1.140 → Broadcast
- 10.0.1.140/30
  - 10.0.1.141 → R1
  - 10.0.1.142 → R2
  - 10.0.1.143 → Broadcast
- 10.0.1.144/30
  - 10.0.1.145 → R1
  - 10.0.1.146 → R3
  - 10.0.1.147 → Broadcast
- 10.0.1.148/30
  - 10.0.1.149 → S
  - 10.0.1.150 → R2
  - 10.0.1.151 → Broadcast
- 10.0.1.152/30
  - 10.0.1.153 → R3
  - 10.0.1.154 → R2
  - 10.0.1.155 → Broadcast
- 10.0.1.156/30
  - 10.0.1.157 → R3
  - 10.0.1.158 → C
  - 10.0.1.159 → Broadcast
- 10.0.1.160/30
  - 10.0.1.161 → R2
  - 10.0.1.162 → R4
  - 10.0.1.163 → Broadcast
- 10.0.1.164/30
  - 10.0.1.165 → R4
  - 10.0.1.166 → B
  - 10.0.1.167 → Broadcast

### B

R1 Deberia tener o el Default Gateway por R3, cosa que todos los destinos que no tenga explicitamente en su tabla de ruteo vayan por ahi, o indicar que la red 10.0.1.164/30 se encuentra pasando por R3.

| Red Destino | Mask |  Next Hop  | Interfaz |
| :---------: | :--: | :--------: | :------: |
|   0.0.0.0   |  /0  | 10.0.1.146 |   eth3   |
| 10.0.1.164  | /30  | 10.0.1.146 |   eth3   |

Cualquiera de estas entradas funcionarian

### C

Default Gateway hacia R2
10.0.1.164/30 hacia B

| Red Destino | Mask |  Next Hop  | Interfaz |
| :---------: | :--: | :--------: | :------: |
|   0.0.0.0   |  /0  | 10.0.1.161 |   eth0   |
| 10.0.1.164  | /30  |     --     |   eth1   |

## Ejercicio 2

2001:db8:2::/42
FF:FF:F2::

En IPv6 se pueden hacer muchas subredes utilizando /64

La subred de A-R1 puede ser 2001:DB8:2::/64

El Host A podria tener la IP 2001:DB8:2::1, y su tabla de rooteo solamente necesita tener el default gateway a traves de R1, que podria tener la IP 2001:DB8:2::2

| Red Destino | Mask |   Next Hop    | Interfaz |
| :---------: | :--: | :-----------: | :------: |
|     ::      |  /0  | 2001:DB8:2::2 |   eth0   |

## Ejercicio 3

### A

SYN
ACK
FIN

### B

ISN A = 100
ISN B = 20

1: SN=ISN=100, ACK:- →  
2: SN=ISN=20, ACK:101 ←  
3: SN=101, ACK:21 →
4: SN=101, ACK:21 →
5: SN=21, ACK:601 ←
6: SN=601, ACK:21 →
7: SN=1101, ACK:21 →

### C

Como se pierde, este se vuelve a enviar y envia los datos siguientes

8: SN=1101, ACK:21 →
9: SN=21, ACK=1601 →
10: SN=1601, ACK=21 →

### D

WIN=8000B

Como se recibio un total de 2000B, el valor que va a enviar seria 8000-2000=6000B

## Ejercicio 4

### A

Debio consultar la direccion IP de la pagina <www.unlp.edu.ar>

El tipo de registro es A
El registro es <www.unlp.edu.ar>
Y al hacer el resolver recursivo del cliente, lo hace de forma recursiva

### B

Se utiliza el metodo GET, utilizando como programa cURL v7.81.0

### C

Se encapsula en el protocolo TCP e iria destinado al puerto 80 de TCP, puerto default de HTTP

### D

Le deberia hacer la consulta a uno de los servidores Root de forma iterativa, luego pasar a los TLD hasta llegar a los servidores autoritativos de unlp.edu.ar. La consulta que haria seria por el registro A de la pagina web

### E

En algun acceso HTTP anterior el servidor le envio la cookie al cliente mediante el encabezado de la respuesta.

En algun acceso HTTP el servidor respondio con el encabezado Set-Cookie