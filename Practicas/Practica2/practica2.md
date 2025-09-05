# Ejercicio 1

## Función de la capa de red en el modelo OSI

La **capa de red** (capa 3) se encarga de:

- Encaminamiento de paquetes desde el origen hasta el destino, incluso a través de múltiples redes intermedias.
- Direccionamiento lógico (asignar direcciones únicas a cada nodo, ej. direcciones IP).
- Fragmentación y reensamblaje de paquetes cuando es necesario.
- Control de congestión y selección de rutas.

En resumen, asegura que los datos viajen de un host a otro sin importar la topología física ni el tipo de red intermedia.

### Implementaciones conocidas

- **IPv4**: la más usada históricamente, con direcciones de 32 bits (≈ 4.3 mil millones de direcciones).
- **IPv6**: sucesora de IPv4, con direcciones de 128 bits.
- Otros protocolos menos comunes: **IPX/SPX** (Novell), **AppleTalk** (antiguo de Apple), aunque hoy todo se estandariza en torno a IP.

### ¿Qué es IPv6 y por qué es necesaria?

- **IPv6** es la nueva versión del protocolo IP, con direcciones de 128 bits, lo que permite una cantidad prácticamente ilimitada de direcciones únicas.
- Es necesaria porque:

  - El espacio de direcciones IPv4 está agotado.
  - IPv6 mejora eficiencia de enrutamiento, autoconfiguración, seguridad (IPsec nativo), soporte para IoT, etc.

### Explicación de las gráficas (IETF)

Las dos imágenes son **relojes de arena** que representan la arquitectura de protocolos en Internet:

- **Parte superior (aplicaciones)**: protocolos de capa de aplicación (ej: email, WWW, VoIP, SMTP, HTTP, RTP).
- **Parte inferior (enlace y físico)**: distintas tecnologías de transmisión (Ethernet, PPP, CSMA, radio, fibra, cobre).
- **Centro (cuello del reloj)**: el **protocolo de red** que actúa como núcleo unificador.

**Gráficas específicas**:

- **Izquierda**: coexistencia de **IPv4 e IPv6** en la capa de red, representando la transición entre ambas versiones.
- **Derecha**: visión simplificada, donde **IP** (sin versión) es el núcleo que conecta todas las aplicaciones con cualquier tecnología de red física.

**Interpretación general**:

- El modelo en “reloj de arena” resalta que **IP es el punto central**:

  - Arriba: múltiples aplicaciones que usan transporte (TCP/UDP).
  - Abajo: múltiples tecnologías físicas de red.
  - Centro: un único protocolo universal que hace de pegamento (IP).

# Ejercicio 2

## Campos de un datagrama IPv4 e IPv6

**IPv4**:

- **Version**: indica la versión del protocolo (4).
- **IHL (Header Length)**: longitud del encabezado en palabras de 32 bits.
- **Type of Service (ToS)**: prioridad y manejo de la calidad de servicio.
- **Total Length**: longitud total del datagrama (header + datos).
- **Identification, Flags, Fragment Offset**: control de fragmentación.
- **TTL (Time To Live)**: limita la vida del paquete en la red.
- **Protocol**: indica el protocolo de capa superior (TCP, UDP, ICMP).
- **Header Checksum**: verificación de integridad del encabezado.
- **Source/Destination IP**: direcciones de origen y destino.
- **Options**: opciones adicionales (rara vez usadas).

**IPv6**:

- **Version**: indica la versión del protocolo (6).
- **Traffic Class**: equivalente al ToS de IPv4.
- **Flow Label**: identifica flujos de datos para QoS.
- **Payload Length**: longitud de los datos (excluye encabezado).
- **Next Header**: indica protocolo de capa superior o extensión siguiente.
- **Hop Limit**: equivalente a TTL en IPv4.
- **Source/Destination IP**: direcciones de 128 bits de origen y destino.

---

### TTL y Hop Limit

Si un paquete llega a un router con **TTL = 1**, el router **descarta el paquete** y envía un mensaje **ICMP Time Exceeded** al origen.

En IPv6, el campo equivalente se llama **Hop Limit**.

---

### Checksum

- En **IPv4**, existe un **checksum del encabezado**.
- En **IPv6**, **no hay checksum en el encabezado**, se asume que capas inferiores (como Ethernet) realizan verificación.
- Los checksums de **TCP y UDP** se mantienen en IPv6, se calculan sobre el pseudo-header actualizado.

Si un paquete tiene un error de checksum:

- **IPv4**: el paquete es descartado y se puede enviar un ICMP al origen si es TCP/UDP.
- **IPv6**: el paquete es descartado; el encabezado no tiene checksum, pero TCP/UDP sí, por lo que errores son detectados igual.

---

### Header Length

No es necesario el **campo Header Length** en IPv6 porque el encabezado tiene **longitud fija de 40 bytes**, y los datos adicionales se manejan con extensiones.

---

### Soporte de nuevas funcionalidades

- **IPv4**: se usarían **opciones en el encabezado**, lo que aumenta su complejidad y tamaño.
- **IPv6**: se usan **headers de extensión**, diseñados específicamente para agregar nuevas funcionalidades sin afectar el encabezado base.

# Ejercicio 3

## Redes IPv4 por clase

**Clase A**:

- Primer bit: 0
- Rango de direcciones: 0.0.0.0 a 127.255.255.255
- Número de redes: 128 (0–127, aunque algunas reservadas)
- Hosts por red: 16.777.214 (2²⁴ − 2)

**Clase B**:

- Primeros bits: 10
- Rango de direcciones: 128.0.0.0 a 191.255.255.255
- Número de redes: 16.384 (2¹⁴)
- Hosts por red: 65.534 (2¹⁶ − 2)

**Clase C**:

- Primeros bits: 110
- Rango de direcciones: 192.0.0.0 a 223.255.255.255
- Número de redes: 2.097.152 (2²¹)
- Hosts por red: 254 (2⁸ − 2)

---

### Clases en IPv6

No existen **clases A, B, C** en IPv6; se usa un esquema de direccionamiento **sin clases (classless)** basado en prefijos (CIDR) y subredes.

---

### Direccionamiento classless

Significa que **no se asignan redes fijas según clases A, B o C**, sino que se usan **prefijos de longitud variable** (CIDR) para dividir el espacio de direcciones según necesidad, optimizando el uso de IPs.

# Ejercicio 4

## Función de la máscara de red

La **máscara de red** determina qué parte de una dirección IP corresponde a la **red** y qué parte corresponde al **host**. Los **bits en 1** representan la **parte de red**, y los **bits en 0** representan la **parte de host**. Esto permite a los dispositivos saber si un destino está en la misma red local o si debe enviarse a un router.

---

### Notación alternativa

Se puede usar **notación CIDR** (Classless Inter-Domain Routing), indicando el número de bits de la red después de la barra:

_Ejemplo_: `192.168.1.0/24` indica que los primeros 24 bits son de la red.

---

### IPv6

En IPv6 se utiliza **CIDR**, por ejemplo `2001:0db8::/32`, porque no existen clases fijas y la longitud de la red puede variar para permitir subredes más flexibles y eficientes.

# Ejercicio 5

## Cálculo de máscara

Se tiene la red: `65.0.0.0/8` y se necesitan **934 subredes**.

1. Calcular cuántos bits se necesitan para las subredes:
   $2^n \ge 934$ → $n = 10$ (2¹⁰ = 1024 ≥ 934)

2. Máscara de red extendida:

   - Original /8 + 10 bits para subred → **/18**

---

## Subred número 817

1. Número de hosts por subred:

   - Hosts = $2^{32-18} - 2 = 2^{14} - 2 = 16.382$

2. Tamaño de bloque: $2^{32-18} = 16.384$ direcciones por subred.

3. Dirección de red de la subred 817:

   - Dirección de red = 65.0.0.0 + (817 × 16.384)

   Calculando:

   - 817 × 16.384 = 13.382.528
   - Convertir a formato IP:

     - 13.382.528 ÷ 256³ = 1, sobra 13.382.528 − 16.777.216×0 = 13.382.528
     - ÷ 256² = 13.382.528 ÷ 65.536 ≈ 204 → 204 × 65.536 = 13.361.664
     - Sobra: 13.382.528 − 13.361.664 = 20.864
     - ÷ 256 = 20.864 ÷ 256 ≈ 81 → 81 × 256 = 20.736
     - Último octeto: 20.864 − 20.736 = 128

   → Dirección de red: **65.204.81.128**

4. Dirección broadcast:

   - Broadcast = Dirección de red + 16.384 − 1 = 13.382.528 + 16.384 − 1 = 13.398.911
   - Convertir a IP: **65.204.97.255**

5. Rango de hosts asignables:

   - Desde 65.204.81.129 hasta 65.204.97.254

---

**Resumen**:

- **Máscara:** /18
- **Subred 817:**

  - Dirección de red: 65.204.81.128
  - Dirección broadcast: 65.204.97.255
  - Rango de hosts: 65.204.81.129 – 65.204.97.254

# Ejercicio 6

## Cálculo de máscara

Red: `195.200.45.0/24`
Se necesitan **9 subredes**.

1. Calcular cuántos bits para subredes:
   $2^n \ge 9$ → $n = 4$ (2⁴ = 16 ≥ 9)

2. Máscara extendida: /24 + 4 bits → **/28**

3. Hosts por subred:
   $2^{32-28} - 2 = 2^4 - 2 = 14$ hosts asignables por subred.

---

## Subredes

Incremento de subred: 16 direcciones por subred (2⁴ = 16)

| Subred | Dirección de red | Broadcast      |
| ------ | ---------------- | -------------- |
| 1      | 195.200.45.0     | 195.200.45.15  |
| 2      | 195.200.45.16    | 195.200.45.31  |
| 3      | 195.200.45.32    | 195.200.45.47  |
| 4      | 195.200.45.48    | 195.200.45.63  |
| 5      | 195.200.45.64    | 195.200.45.79  |
| 6      | 195.200.45.80    | 195.200.45.95  |
| 7      | 195.200.45.96    | 195.200.45.111 |
| 8      | 195.200.45.112   | 195.200.45.127 |
| 9      | 195.200.45.128   | 195.200.45.143 |

---

## Ejemplo: Subred 3

- Dirección de red: **195.200.45.32**
- Broadcast: **195.200.45.47**
- Rango de hosts asignables: **195.200.45.33 – 195.200.45.46**

---

**Resumen**:

- **Máscara:** /28
- **Subred 3:** Dirección de red 195.200.45.32, Broadcast 195.200.45.47, Hosts 195.200.45.33 – 195.200.45.46

# Ejercicio 7

| Dirección     | Clase | Privada/Publica |
| ------------- | ----- | --------------- |
| 172.16.7.12   | B     | Privada         |
| 200.5.123.221 | C     | Pública         |
| 224.0.0.9     | D     | Pública         |
| 10.10.1.10    | A     | Privada         |
| 172.15.7.98   | B     | Pública         |
| 192.168.10.5  | C     | Privada         |
| 240.32.34.2   | E     | Pública         |
| 1.1.1.1       | A     | Pública         |
| 8.8.8.8       | A     | Pública         |
| 239.12.34.3   | D     | Pública         |

# Ejercicio 8

## 1. 163.10.5.66/26

- Clase: B
- Pública/Privada/Reservada: Pública
- Subred: 163.10.5.64
- Broadcast: 163.10.5.127
- Posibles subredes con /26 en toda la red: 2⁸ = 256 (B tiene 16.384 redes, con /26 → 16.384 × 2^(26-16) = 16.384 × 1024 = 16.777.216 posibles, pero se toma por bloque de la misma máscara: 2^(26-16)=1024 subredes dentro de cada red B)
- Hosts por subred: 2⁶ = 64 → 64-2 = 62

---

## 2. 127.0.0.1/8

- Clase: A
- Pública/Privada/Reservada: Reservada (loopback)
- Subred: 127.0.0.0
- Broadcast: 127.255.255.255
- Posibles subredes con /8: 2⁰ = 1
- Hosts por subred: 2²⁴ − 2 = 16.777.214

---

## 3. 20.6.20.1/18

- Clase: A
- Pública/Privada/Reservada: Pública
- Subred: 20.6.0.0
- Broadcast: 20.6.63.255
- Posibles subredes con /18 en toda la red: 2¹⁰ = 1024 subredes dentro de la red A original
- Hosts por subred: 2¹⁴ − 2 = 16.382

---

## 4. 200.5.10.3/30

- Clase: C
- Pública/Privada/Reservada: Pública
- Subred: 200.5.10.0
- Broadcast: 200.5.10.3
- Posibles subredes con /30: 2⁶ = 64 subredes dentro de la red C original
- Hosts por subred: 2² − 2 = 2

---

## 5. 172.18.10.0/26

- Clase: B
- Pública/Privada/Reservada: Privada
- Subred: 172.18.10.0
- Broadcast: 172.18.10.63
- Posibles subredes con /26: 2⁶ = 64 subredes dentro de la red B original
- Hosts por subred: 2⁶ − 2 = 62

# Ejercicio 9

| Dirección                                      | Válida | Asignable a host | Motivo de invalidez (si corresponde)                  |
| ---------------------------------------------- | ------ | ---------------- | ----------------------------------------------------- |
| 2001:0:1019\:afde::1                           | Sí     | Sí               | —                                                     |
| 2001::1871::4                                  | No     | No               | Tiene **dos abreviaturas `::`** en la misma dirección |
| 3ffg:8712:0:1:0000\:aede\:aaaa:1211            | No     | No               | Contiene un **carácter no hexadecimal `g`**           |
| 3::1                                           | Sí     | Sí               | —                                                     |
| 3ffe:1080:1212:56ed:75da:43ff\:fe90\:affe      | Sí     | Sí               | —                                                     |
| ::                                             | Sí     | No               | Dirección todo ceros, no asignable a host             |
| 2001::                                         | Sí     | No               | Prefijo de red, no asignable a host                   |
| 3ffe:1080:1212:56ed:75da:43ff\:fe90\:affe:1001 | No     | No               | Tiene **9 bloques**, IPv6 solo permite 8 bloques      |

# Ejercicio 10

Las direcciones se pueden **agrupar en un bloque mayor** aplicando CIDR:

- Direcciones originales:
  200.10.0.0/24
  200.10.1.0/24
  200.10.2.0/24
  200.10.3.0/24

- Todas pertenecen al mismo rango de **200.10.0.0 – 200.10.3.255**.

- Bloque CIDR que las resume: **200.10.0.0/22**

Esto agrupa los 4 /24 consecutivos en una sola red más grande.

# Ejercicio 11

Redes originales:

200.10.0.0/24\
200.10.1.0/24\
200.10.2.0/24\
200.10.3.0/24\
200.10.4.0/24\
200.10.5.0/24\
200.10.6.0/24\
200.10.7.0/24

Rango total: 200.10.0.0 – 200.10.7.255

Bloque CIDR que las resume: **200.10.0.0/21**

Esto agrupa las 8 redes consecutivas en un solo bloque de mayor tamaño.

# Ejercicio 12

Redes originales:

195.80.0.0/24\
195.80.1.0/24\
195.80.2.0/24

Rango total: 195.80.0.0 – 195.80.2.255

Bloques CIDR que las resumen: **195.80.0.0/23** y **195.80.2.0/24**

_Explicación:_

- 195.80.0.0/23 cubre 195.80.0.0 y 195.80.1.0
- 195.80.2.0/24 queda como bloque independiente, porque no se puede combinar con /23 sin incluir 195.80.3.0/24.

# Ejercicio 13

## Cálculo de máscara

Red: `195.200.45.0/25`
Se necesitan **6 subredes** con **6 hosts cada una**.

1. Calcular cuántos bits para hosts:

   - 6 hosts → 3 bits (2³ − 2 = 6 hosts)

2. Máscara para subredes:

   - Total bits de host = 3 → máscara = 32 − 3 = **/29**

---

## Subredes

Incremento por subred: 2³ = 8 direcciones por subred (6 hosts + red + broadcast)

| Subred | Dirección de red | Broadcast     | Hosts asignables              |
| ------ | ---------------- | ------------- | ----------------------------- |
| 1      | 195.200.45.0     | 195.200.45.7  | 195.200.45.1 – 195.200.45.6   |
| 2      | 195.200.45.8     | 195.200.45.15 | 195.200.45.9 – 195.200.45.14  |
| 3      | 195.200.45.16    | 195.200.45.23 | 195.200.45.17 – 195.200.45.22 |
| 4      | 195.200.45.24    | 195.200.45.31 | 195.200.45.25 – 195.200.45.30 |
| 5      | 195.200.45.32    | 195.200.45.39 | 195.200.45.33 – 195.200.45.38 |
| 6      | 195.200.45.40    | 195.200.45.47 | 195.200.45.41 – 195.200.45.46 |

---

**Resumen:**

- **Máscara utilizada:** /29
- **Subred número 4:**

  - Dirección de red: 195.200.45.24
  - Broadcast: 195.200.45.31
  - Rango de hosts: 195.200.45.25 – 195.200.45.30

# Ejercicio 14

<!--



  Tengo que hacerlo


 -->

# Ejercicio 15

La dirección **127.0.0.1** es la **dirección de loopback** en IPv4.

**Significado y uso:**

- Permite que un host se **auto-comunique**, enviando paquetes a sí mismo sin salir a la red física.
- Se utiliza principalmente para **pruebas y diagnóstico** de la pila TCP/IP del propio equipo.
- Todas las direcciones del rango **127.0.0.0/8** están reservadas para loopback.

# Ejercicio 16

## ICMP

**ICMP (Internet Control Message Protocol)** es un protocolo de la capa de red que se utiliza para **enviar mensajes de control y diagnóstico** sobre el estado de la red, como errores en la entrega de paquetes o pruebas de conectividad.

---

## Comandos

- **ping**: envía paquetes ICMP **Echo Request** a un host y espera recibir **Echo Reply**, midiendo conectividad y tiempos de respuesta.
- **traceroute (Linux) / tracert (Windows)**: determina la ruta que siguen los paquetes hasta un destino, usando paquetes con **TTL incrementales** y detectando los mensajes ICMP **Time Exceeded** enviados por routers intermedios.

---

## Tipos y códigos ICMP

- **Ping (solicitud)**:

  - Tipo = 8 (Echo Request)
  - Código = 0

- **Ping (respuesta)**:

  - Tipo = 0 (Echo Reply)
  - Código = 0

- **Traceroute**:

  - Usa **ICMP Time Exceeded**
  - Tipo = 11
  - Código = 0

---

## Diferencias Linux vs Windows

- **Linux (traceroute)**: por defecto envía **paquetes UDP** a puertos altos y detecta ICMP Time Exceeded; puede usar ICMP con opción `-I`.
- **Windows (tracert)**: envía paquetes **ICMP Echo Request** directamente.
- Resultado final similar, pero el tipo de paquetes enviados inicialmente difiere.
- Con un capturador de tráfico (Wireshark/tshark/tcpdump) se puede observar esta diferencia.

# Ejercicio 17

**Diferencias principales entre ICMP (IPv4) e ICMPv6:**

- ICMPv6 **hereda las funciones de diagnóstico y control** de ICMP en IPv4 (errores y mensajes de información).
- ICMPv6 **integra funcionalidades adicionales obligatorias para IPv6**, incluyendo:

  - **Neighbor Discovery (ND)**: reemplaza ARP, para resolución de direcciones y detección de vecinos.
  - **Router Solicitation / Advertisement**: permite autoconfiguración de hosts y descubrimiento de routers.
  - **Mensaje de redirección optimizada**: indica rutas más eficientes dentro de la red.

- ICMPv6 también es **esencial para la autoconfiguración sin estado (SLAAC)** de IPv6, algo que ICMP en IPv4 no realiza.

En resumen, ICMPv6 combina funciones tradicionales de control con mecanismos de descubrimiento y autoconfiguración necesarios en IPv6.

# Ejercicio 18

Core

<!-- Lo hago despues -->

# Ejercicio 19

**ARP (Address Resolution Protocol)** sirve para **resolver direcciones IP a direcciones físicas (MAC)** en redes de capa de enlace, permitiendo que un host pueda enviar tramas a otro dentro de la misma red local.

---

**No es necesario ARP en:**

- Protocolos de enlace que **ya tienen mapeo directo de direcciones**, como **ATM, Frame Relay** o redes que usan direcciones de nivel 3 ya directamente sobre hardware lógico.

---

**IPv6 y ARP:**

- ARP **no se utiliza en IPv6**.
- En su lugar se emplea **Neighbor Discovery (ND)**, que usa ICMPv6 para resolver direcciones y detectar vecinos.

# Ejercicio 20

- **ARP Request:** se envía a **dirección MAC de broadcast** `FF:FF:FF:FF:FF:FF`, porque el emisor no conoce la dirección del destinatario.
- **ARP Reply:** se envía a la **dirección MAC específica del solicitante**, es decir, de manera **unicast** hacia quien pidió la información.

# Ejercicio 21

No, los mensajes **ARP no son reenviados por los routers**.

**Justificación:**

- ARP opera en la **capa de enlace (L2)** y su alcance es **solo la red local (broadcast local)**.
- Los routers solo manejan el **encaminamiento de paquetes IP** entre redes; no retransmiten tramas de broadcast de capa 2 como ARP hacia otras redes.

# Ejercicio 22

Core

<!-- Lo hago despues -->

# Ejercicio 23

**Direcciones link-local en IPv6:**

- Son direcciones que comienzan con **FE80::/10** y se **autoconfiguran automáticamente** en cada interfaz.
- Se utilizan para **comunicaciones dentro de un mismo enlace** (subred), como **neighbor discovery, router discovery y autoconfiguración**.
- No son enrutable a otras redes.

**Analogía con IPv4:**

- Equivalen aproximadamente a las direcciones **APIPA/169.254.0.0/16** en IPv4, que también se autoconfiguran y sirven para comunicación local en ausencia de DHCP.

# Ejercicio 24

Para generar un **IID (Interface Identifier) de 64 bits** a partir de una dirección MAC de 48 bits, se usa el **formato EUI-64**:

1. Dividir la MAC en dos partes de 24 bits.
2. Insertar `FFFE` en el medio.
3. Invertir el **bit universal/local** (el segundo bit más significativo del primer octeto).

---

## 1. MAC: 00:1b:77\:b1:49\:a1

1. Primer octeto: `00` → binario: `00000000`

   - Invertir bit universal/local (2° bit): `00000010` → hexadecimal: `02`

2. Insertar `FFFE` en el medio: 02:1b:77\:FF\:FE\:b1:49\:a1

**IID 64 bits:** `021b:77ff:feb1:49a1`

---

## 2. MAC: e8:1c:23\:a3:21\:f4

1. Primer octeto: `e8` → binario: `11101000`

   - Invertir bit universal/local: `11101010` → hexadecimal: `ea`

2. Insertar `FFFE` en el medio: ea:1c:23\:FF\:FE\:a3:21\:f4

**IID 64 bits:** `ea1c:23ff:fea3:21f4`

# Ejercicio 25

La **abreviatura correcta** de `3f80:0000:0000:0a00:0000:0000:0000:0845` es:

**3f80:0:0\:a00::845**

- Explicación:

  - Se eliminan los ceros a la izquierda de cada bloque.
  - Se reemplaza la **mayor secuencia continua de bloques cero** por `::` (solo una vez).

# Ejercicio 26

| Dirección                          | Tipo de dirección          |
| ---------------------------------- | -------------------------- |
| fe80::1/64                         | Link-local                 |
| 3ffe:4543:2:<!-- -->100:4398::1/64 | Global (unicast global)    |
| ::                                 | Unspecified (no asignable) |
| ::1                                | Loopback                   |
| ff02::2                            | Multicast (all routers)    |
| 2818\:edbc:43e1::8721:122          | Global (unicast global)    |
| ff02::9                            | Multicast (RIP routers)    |

# Ejercicio 27

<!-- Lo hago despues -->