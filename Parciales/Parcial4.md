# Parcial 4

## Ejercicio 1

- Permite la autoconfiguración de equipos.V
- Tiene direcciones de mayor longitud que IPv4.V
- Prohíbe la fragmentación en routers.V
- Comprueba mediante el checksum que la cabecera del datagrama no haya sufrido errores de transmisión.F No hay checksum de cabezera, se encarga capa de transporte

## Ejercicio 2

Para 2044 ips se necesitan 11 bits de hosts. Por ende se necesita como maximo un /21. Un /20 incluso estaria mal, pues tendria mas de 2000 ips inutilizadas

132.10.56.0/21V
147.23.20.0/20F Desperdicio
158.42.18.0/22F Insuficientes
199.269.48.0/21V

## Ejercicio 3

1. Syn, SN=4999, ACK=-, Data=0
2. Syn Ack, SN=1999, ACK=5000, Data=0
3. Ack, SN=5000, ACK=2000, Data=0
4. PSH ACK, SN=5000, ACK=2000, Data=500
5. PSH ACK, SN=2000, ACK=5500, Data=300
6. PSH ACK, SN=5500, ACK=2300, Data=300
7. PSH ACK, SN=5800, ACK=2300, Data=200
8. ACK, SN=2300, ACK=6000, Data=0

## Ejercicio 4

### A

Si solamente los ultimos 2 no se mandaron, tendria 500 bytes en la ventana, por lo que anunciaria que la ventana suya es 2000-500=1500 bytes

### B

Se lo conoce como control de flujo, y su objetivo es no saturar al receptor

## Ejercicio 5

| Red Destino | Mask |  Next Hop  | Interfaz |
| :---------: | :--: | :--------: | :------: |
|   0.0.0.0   |  /0  | 163.10.5.2 |   eth0   |
| 105.4.3.192 | /28  |     --     |   eth2   |
| 172.16.9.0  | /29  |     --     |   eth1   |
| 105.4.3.128 | /26  | 172.16.9.2 |   eth1   |
| 10.10.20.64 | /26  | 172.16.9.1 |   eth1   |

## Ejercicio 6

### A

Se deberia ejecutar entre PC-A y su Gateway, Rtr B, Entre Rtr b y Rtr C, y por ultimo entre Rtr c y PC-E

### B

Al pasar por el switch no habria cambios, seria la siguiente
Trama Ethernet (cabecera L2)

- Destino MAC: ff:ff:ff:ff:ff:ff (broadcast, porque es ARP Request)
- Origen MAC: MAC_de_RtrA_eth0 (la MAC de la interfaz de Rtr-A en 172.16.9.0/29)
- EtherType: 0x0806 (ARP)

Payload ARP

- Hardware type (HTYPE): 1 (Ethernet)
- Protocol type (PTYPE): 0x0800 (IPv4)
- HLEN: 6
- PLEN: 4
- Opcode: 1 (ARP request)
- Sender hardware address (SHA): MAC_de_RtrA_eth0
- Sender protocol address (SPA): 172.16.9.2 (IP de Rtr-A en esa subred)
- Target hardware address (THA): 00:00:00:00:00:00 (desconocida)
- Target protocol address (TPA): 172.16.9.3 (IP de Rtr-C que se pregunta)

## Ejercicio 7

- Al realizar NATP no se modifican la IP Destino ni el puerto TCP destino. V
- En IPv4 la cabecera puede tener un tamaño variable por eso es necesario el campo Header Lenght. V
- Si un router detecta un paquete con el checksum erróneo entonces le solicitará una retransmisión al origen. F
- La funcionalidad del campo TTL es limitar el tiempo de vida de un paquete en una red. V

