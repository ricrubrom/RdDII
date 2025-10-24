# Practica 4

## Ejercicio 1

### Funciones de la capa de transporte (modelo OSI)

- **Entrega de datos de extremo a extremo:** Garantiza que los datos enviados por una aplicación en un host lleguen a la aplicación correspondiente en otro host.
- **Segmentación y reensamblaje:** Divide los datos grandes en segmentos y los reensambla en el destino.
- **Control de flujo:** Regula la velocidad de envío para evitar saturar al receptor.
- **Control de errores:** Detecta errores en los segmentos y solicita retransmisión si es necesario.
- **Multiplexación/demultiplexación:** Permite que varias aplicaciones compartan la misma conexión de red usando puertos.
- **Conexiones confiables:** Opcionalmente, establece una sesión confiable con confirmaciones y retransmisiones.

### Protocolos TCP, UDP

| Función                     | TCP | UDP           |
| --------------------------- | --- | ------------- |
| Entrega confiable           | Sí  | No            |
| Control de flujo            | Sí  | No            |
| Control de errores          | Sí  | Solo checksum |
| Segmentación y reensamblaje | Sí  | Sí            |
| Multiplexación por puertos  | Sí  | Sí            |
| Orientación a conexión      | Sí  | No            |
| Cifrado integrado           | No  | No            |

### Otros protocolos de transporte en TCP/IP

- **SCTP (Stream Control Transmission Protocol):** Orientado a mensajes, confiable, admite múltiples flujos dentro de una misma conexión.
- **DCCP (Datagram Congestion Control Protocol):** Proporciona control de congestión para datagramas, útil en multimedia.
- **QUIC (Quick UDP Internet Connections):** Protocolo de transporte sobre UDP que ofrece entrega confiable, multiplexación de streams, control de flujo y cifrado integrado.
- Los más utilizados siguen siendo **TCP**, **UDP** y, cada vez más, **QUIC** para aplicaciones web modernas (HTTP/3).

### Encapsulación y ubicación

- Se encapsulan **sobre IPv4 o IPv6**, aunque QUIC se implementa sobre UDP.
- Generalmente se implementan en **el kernel del sistema operativo**, porque necesitan acceso a las interfaces de red y manejo eficiente de sockets.
- Algunos protocolos o funciones modernas pueden implementarse en **espacio de usuario** o como **microservicios fuera del kernel**, especialmente QUIC, que suele implementarse en librerías de usuario.

## Ejercicio 2

### Supuestos de TCP y UDP sobre la capa de red

- **TCP** y **UDP** asumen que la capa de red (IP) proporciona:

  - **Entrega de datagramas sin error garantizado** (aunque IP no garantiza fiabilidad, TCP/UDP detectan errores).
  - **Entrega de datagramas a la dirección correcta**, usando direcciones IP.
  - **Servicios de datagramas independientes**, sin control de flujo ni retransmisión (esto lo maneja TCP).

- TCP añade **confiabilidad, control de flujo y secuenciación** sobre el servicio básico de IP.

- UDP ofrece **transporte no confiable**, solo verificación de integridad con checksum.

---

### Campo del datagrama IP para diferenciar protocolos de transporte

- El campo en IPv4 se llama **Protocol** y en IPv6 se llama **Next Header**.
- Este campo indica qué protocolo de transporte se está usando.

Ejemplos de valores (consultables en `/etc/protocols`):

| Protocolo | Campo IP               | Valor |
| --------- | ---------------------- | ----- |
| TCP       | Protocol / Next Header | 6     |
| UDP       | Protocol / Next Header | 17    |
| SCTP      | Protocol / Next Header | 132   |
| ICMP      | Protocol / Next Header | 1     |

- Este valor permite la **multiplexación**, es decir, entregar cada datagrama IP al protocolo de transporte correspondiente en el host de destino.

## Ejercicio 3

### Nombres de las PDUs en capa de transporte

| Protocolo | Nombre de la PDU | Descripción                                                       |
| --------- | ---------------- | ----------------------------------------------------------------- |
| TCP       | Segmento         | Contiene encabezado TCP + datos de la aplicación                  |
| UDP       | Datagram         | Contiene encabezado UDP + datos de la aplicación                  |
| SCTP      | Chunk            | Contiene encabezado SCTP + chunks de datos (pueden ser múltiples) |
| QUIC      | Packet / Frame   | Contiene encabezado QUIC + frames de datos multiplexados          |

### Estructura de las PDUs

**TCP Segmento:**

```text
+-------------------------------+
| Puerto origen (16 bits)       |
+-------------------------------+
| Puerto destino (16 bits)      |
+-------------------------------+
| Número de secuencia (32 bits) |
+-------------------------------+
| Número de acuse (32 bits)     |
+-------------------------------+
| Offset + Reservado + Flags    |
+-------------------------------+
| Ventana (16 bits)             |
+-------------------------------+
| Checksum (16 bits)            |
+-------------------------------+
| Urgent pointer (16 bits)      |
+-------------------------------+
| Opciones (variable)           |
+-------------------------------+
| Datos (variable)              |
+-------------------------------+
```

**UDP Datagram:**

```text
+---------------------+
| Puerto origen (16)  |
+---------------------+
| Puerto destino (16) |
+---------------------+
| Longitud (16)       |
+---------------------+
| Checksum (16)       |
+---------------------+
| Datos (variable)    |
+---------------------+
```

**SCTP Chunk:**

```text
+-------------------------+
| Puerto origen (16)      |
+-------------------------+
| Puerto destino (16)     |
+-------------------------+
| Verificación checksum   |
+-------------------------+
| Chunk 1 (tipo, longitud, datos) |
+-------------------------+
| Chunk 2 ...             |
+-------------------------+
```

**QUIC Packet / Frame:**

```text
+-------------------------------+
| Header QUIC (var. largo)      |
+-------------------------------+
| Frame 1 (tipo, longitud, datos) |
+-------------------------------+
| Frame 2 ...                    |
+-------------------------------+
```

Si querés, puedo hacer un **diagrama unificado con todas las PDUs comparadas** para verlo de manera visual y rápida. ¿Querés que haga eso?

## Ejercicio 4

### Comportamiento ante recepción de datagramas/segmentos

#### a) Datagrama IPv6 a un host sin soporte IPv6

- El datagrama **es descartado**.
- El host puede generar un **ICMP “Destination Unreachable – Protocol Unreachable”** o simplemente ignorarlo según la implementación.

#### b) Segmento TCP a un host sin soporte TCP

- El segmento **es descartado**.
- Generalmente se genera un **ICMP “Protocol Unreachable”** hacia el origen.

#### c) Segmento TCP o UDP a un puerto sin proceso escuchando

- **TCP:** El host responde con un **TCP RST (Reset)** indicando que no hay servicio disponible en ese puerto.
- **UDP:** El host envía un **ICMP “Port Unreachable”** al origen.

## Ejercicio 5

### Diferencias entre checksums de UDP, TCP, IPv4 e IPv6

| Protocolo | Campo de checksum           | Propósito                                                                 | Obligatorio                           | Datos cubiertos                                  |
| --------- | --------------------------- | ------------------------------------------------------------------------- | ------------------------------------- | ------------------------------------------------ |
| **IPv4**  | Header checksum             | Verifica la integridad del **encabezado IPv4**                            | Sí                                    | Solo header (no datos)                           |
| **IPv6**  | No tiene checksum en header | La integridad se asegura a nivel de transporte (TCP/UDP) o capa de enlace | No                                    | –                                                |
| **TCP**   | Checksum                    | Detecta errores en **encabezado + datos**                                 | Sí                                    | Pseudo-header IPv6/IPv4 + header TCP + datos TCP |
| **UDP**   | Checksum                    | Detecta errores en **encabezado + datos**                                 | Opcional en IPv4, obligatorio en IPv6 | Pseudo-header IPv6/IPv4 + header UDP + datos UDP |

## Ejercicio 6

### Escenario TCP y UDP con múltiples conexiones

- Hosts origen: `10.0.0.10` y `10.0.0.11`
- Servidor destino: `192.168.1.10`
- Servicio: Telnet (puerto 23)

---

#### a) Primera conexión TCP (desde 10.0.0.10)

```text
Dirección origen: 10.0.0.10
Puerto origen: 1025 (ejemplo, asignado dinámicamente por SO)
Dirección destino: 192.168.1.10
Puerto destino: 23 (Telnet)
```

#### b) Segunda conexión TCP (desde 10.0.0.10)

```text
Dirección origen: 10.0.0.10
Puerto origen: 1026 (SO asigna un puerto distinto)
Dirección destino: 192.168.1.10
Puerto destino: 23
```

#### c) Nueva conexión TCP desde 10.0.0.11

```text
Dirección origen: 10.0.0.11
Puerto origen: 1025 (asignado dinámicamente)
Dirección destino: 192.168.1.10
Puerto destino: 23
```

---

#### d) Cantidad de segmentos TCP transmitidos (solo handshake)

- Cada conexión TCP requiere 3 segmentos (SYN, SYN-ACK, ACK)
- Con 3 conexiones: 3 × 3 = 9 segmentos TCP

---

#### e) Flags visibles en los segmentos TCP

```text
Handshake inicial: SYN, SYN-ACK, ACK
Segmentos de datos: ACK (junto con datos)
Cierre de conexión: FIN, ACK (y RST si cierre abrupto)
```

---

#### f) Cantidad total de segmentos TCP si solo dos de los tres procesos envían 1 byte y luego cierran

- Cada conexión que envía datos:

  - Handshake: 3 segmentos
  - Envío de 1 byte: 1 segmento de datos + 1 ACK → 2 segmentos
  - Cierre: 2 segmentos por cada extremo → 4 segmentos

- Con 2 conexiones que envían datos: 3 + 2 + 4 = 9 segmentos por conexión

- Conexión que no envía datos: handshake 3 + cierre 2 = 5 segmentos

- Total segmentos TCP: 9 + 9 + 5 = 23 segmentos TCP

---

#### g) Cantidad de datagramas UDP si solo dos de los tres procesos envían datos

- Cada datagrama UDP corresponde a un envío de datos, no hay handshake ni cierre.
- Con 2 procesos enviando 1 byte cada uno: 2 datagramas enviados.
- Si consideramos respuesta del servidor (1 byte por proceso): 2 datagramas de vuelta.
- Total datagramas UDP: 2 + 2 = 4

---

#### h) Simulación de los escenarios con `nc` o `telnet`

```bash
# Conexión TCP desde 10.0.0.10 hacia servidor
telnet 192.168.1.10 23

# Otra conexión TCP desde el mismo host
telnet 192.168.1.10 23

# Conexión TCP desde 10.0.0.11 hacia servidor
telnet 192.168.1.10 23

# Para UDP (con nc)
# En el servidor
nc -u -l 5000

# En el cliente
nc -u 192.168.1.10 5000
```

- Se pueden abrir varias terminales para simular conexiones simultáneas.
- Usar **Wireshark o tcpdump** permite observar segmentos, flags, puertos y dirección de cada conexión.

