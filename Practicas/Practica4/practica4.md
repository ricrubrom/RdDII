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

## Ejercicio 12

### a) Intercambio de mensajes para establecer la sesión (three-way handshake)

1. **A → B:** `SYN`, `Seq = 50430`, opciones: `MSS = 1400`, `Window = 64 KB`

   - A inicia la conexión anunciando su ISN (50430), su MSS (que indica el máximo que **A puede recibir**) y su ventana de recepción (64 KB).

2. **B → A:** `SYN, ACK`, `Seq = 68900`, `Ack = 50431` ( = 50430 + 1 ), opciones: `MSS = 1000`, `Window = 32 KB`

   - B responde con su ISN (68900), confirma el `SYN` de A con `Ack = ISN_A + 1` y anuncia su MSS (1000) y su ventana de recepción (32 KB).

3. **A → B:** `ACK`, `Seq = 50431`, `Ack = 68901` ( = 68900 + 1 )

   - A confirma el `SYN` de B. A partir de este ACK la sesión TCP queda establecida.

**Notas:**

- El MSS es una opción anunciada en el `SYN` y representa el tamaño máximo que _ese host puede recibir_. Por tanto, los tamaños máximos efectivos por sentido son:

  - Para datos **A → B**: usar como máximo `MSS_B = 1000 bytes`.
  - Para datos **B → A**: usar como máximo `MSS_A = 1400 bytes`.

- Las ventanas anunciadas (64 KB y 32 KB) son la cantidad de bytes que cada receptor está dispuesto a aceptar sin ACK.

---

### b) ¿Cuántos segmentos de tamaño máximo se pueden enviar sin esperar un ACK?

Primero convertimos ventanas a bytes exactos:

- `64 KB = 64 * 1024 = 65.536 bytes`
- `32 KB = 32 * 1024 = 32.768 bytes`

#### 1) **Sin aplicar control de congestión** (es decir, sólo limitados por la ventana de recepción)

- **A → B**

  - Ventana que A puede usar = ventana anunciada por B = 32.768 bytes.
  - Tamaño máximo por segmento (A → B) = `MSS_B = 1000 bytes`.
  - Número de segmentos máximos completos = `floor(32768 / 1000) = 32` segmentos completos.
  - Resto en bytes = `32768 − 32·1000 = 32768 − 32000 = 768 bytes` → se puede enviar además un segmento parcial de 768 bytes.
  - **Resultado:** 32 segmentos de 1000 B + 1 segmento parcial de 768 B (ó en términos de “segmentos de tamaño máximo”: 32).

- **B → A**

  - Ventana que B puede usar = ventana anunciada por A = 65.536 bytes.
  - Tamaño máximo por segmento (B → A) = `MSS_A = 1400 bytes`.
  - Número de segmentos máximos completos = `floor(65536 / 1400)`. Calculo: `1400·46 = 64.400` y `1400·47 = 65.800 (>65536)`, por tanto `floor = 46`.
  - Resto en bytes = `65536 − 46·1400 = 65536 − 64400 = 1.136 bytes` → un segmento parcial de 1.136 bytes posible.
  - **Resultado:** 46 segmentos de 1400 B + 1 segmento parcial de 1136 B (ó en términos de “segmentos de tamaño máximo”: 46).

#### 2) **Aplicando control de congestión tradicional** (modo clásico: _slow start_ con `cwnd` inicial = 1 MSS)

En el control de congestión tradicional (slow start) el emisor no puede enviar más que su `cwnd` además de estar limitado por la ventana del receptor. Si tomamos el valor _clásico_ y conservador `cwnd_initial = 1 MSS`:

- **A → B**

  - `cwnd = 1 · MSS_A_enviable = 1 · (MSS_B) = 1 · 1000 = 1000 bytes`.
  - Receptor permite hasta 32.768 bytes, pero `cwnd` limita a 1000 bytes antes de recibir ACK.
  - **Resultado:** **1 segmento** (de 1000 bytes) puede enviarse sin esperar ACK.

- **B → A**

  - `cwnd = 1 · MSS_B_enviable = 1 · (MSS_A) = 1 · 1400 = 1400 bytes`.
  - Receptor permite hasta 65.536 bytes, pero `cwnd` limita a 1400 bytes inicialmente.
  - **Resultado:** **1 segmento** (de 1400 bytes) puede enviarse sin esperar ACK.

**Comentario adicional sobre variantes modernas:** RFCs más recientes y prácticas actuales permiten `cwnd` inicial mayor (p. ej. 2–10 MSS, RFC 6928 propone 10 MSS en muchos casos). Si se aplicara un `cwnd_initial = N·MSS`, sustituya `1·MSS` por `N·MSS` en los cálculos y compare con la ventana del receptor (en cualquier caso el límite efectivo es `min(recv_window, cwnd)`).

## Ejercicio 13

B ya recibió **todos** los bytes hasta el byte **225**, por lo que el **próximo byte esperado** es el **226**. A se conecta desde el puerto **1986** hacia el puerto **22** de B.

### a) ¿Qué valor indicará B en el campo ACK para reconocer esta condición? ¿Qué ports utilizará?

- **ACK = 226** (indica el siguiente byte que espera recibir).
- **Puertos:** en los paquetes de B → A el **source port = 22** y el **destination port = 1986**.

### b) Números de secuencia de los dos segmentos (100 y 120 bytes) enviados por A

Asumiendo que A empieza a enviar en el siguiente byte esperado (226):

- Primer segmento (100 bytes): **Seq = 226** (cubre bytes `226 .. 325`).
- Segundo segmento (120 bytes): **Seq = 326** (cubre bytes `326 .. 445`).
  (El siguiente número de secuencia después de los dos sería **446**.)

### c) ACKs si B ACKea por cada segmento / si ACKea uno solo por ambos

- Si B envía un ACK por **cada** segmento recibido:

  - Tras el primer segmento (226–325) ACK = **326**.
  - Tras el segundo segmento (326–445) ACK = **446**.

- Si B envía **un solo ACK** para ambos (p. ej. delayed ACK): ACK = **446**.

### d) Si el segundo segmento (120 bytes) arriba **antes** que el primero, ¿qué ACK manda B al recibirlo?

Al recibir el segmento con **Seq = 326** (bytes 326–445) pero **sin** haber recibido aún los bytes 226–325, B sólo puede confirmar hasta el último byte contiguo recibido desde el inicio: eso sigue siendo 225, por lo que el ACK que envía será **226** (un _duplicate ACK_ indicando que aún espera el byte 226).

## Ejercicio 16

RTT = 10 ms
rwnd = 12 KB
MSS = 1 KB
cwnd inicial (IW) = 1 × MSS = 1 KB (slow start)
ssthresh inicial = 16 KB
Emisor envía continuamente. Queremos el tiempo hasta que `min(cwnd, rwnd)` alcance su máximo.

### Cálculo paso a paso (per-RTT, crecimiento en _slow start_ — cwnd se duplica cada RTT)

- Instante inicial (t = 0): `cwnd = 1 KB` → `min = 1 KB`
- Después de 1 RTT (t = 10 ms): `cwnd = 2 KB` → `min = 2 KB`
- Después de 2 RTT (t = 20 ms): `cwnd = 4 KB` → `min = 4 KB`
- Después de 3 RTT (t = 30 ms): `cwnd = 8 KB` → `min = 8 KB`
- Después de 4 RTT (t = 40 ms): `cwnd = 16 KB` → `min(cwnd, rwnd) = min(16 KB, 12 KB) = 12 KB`

Como la ventana de recepción (rwnd = 12 KB) limita el envío, el valor máximo alcanzable por `min(cwnd, rwnd)` es **12 KB**, y esto ocurre la primera vez que `cwnd ≥ 12 KB`, lo cual sucede al término del 4.º RTT.

**Tiempo total hasta alcanzar el máximo = 4 × RTT = 4 × 10 ms = 40 ms.**

### Tabla resumen

| Tiempo (ms) | cwnd (KB) | min(cwnd, rwnd) (KB)  |
| ----------: | :-------: | :-------------------: |
|           0 |     1     |           1           |
|          10 |     2     |           2           |
|          20 |     4     |           4           |
|          30 |     8     |           8           |
|          40 |    16     | 12 (máximo alcanzado) |

### Diagrama sencillo (eje vertical = KB, eje horizontal = tiempo / RTT)

Vertical: 0 — 2 — 4 — 6 — 8 — 10 — 12 — 14 — 16
RTT0: ▇ (1)
RTT1: ▇▇ (2)
RTT2: ▇▇▇▇ (4)
RTT3: ▇▇▇▇▇▇▇▇ (8)
RTT4: ▇▇▇▇▇▇▇▇▇▇▇▇ (12, limitado por rwnd) ← máximo efectivo

## Ejercicio 17

### Supuestos y comportamiento TCP tras RTO

Cuando vence el RTO habitualmente se aplica la reacción clásica (TCP Tahoe/Reno):

- `ssthresh = max(cwnd/2, 2·MSS)`.
- `cwnd` se reduce a `1·MSS` (inicio de _slow start_).

Dado `cwnd` inicial = 18 KB y `MSS = 1 KB`:

- `ssthresh = 18 KB / 2 = 9 KB` (9 MSS).
- `cwnd` queda en `1 KB` (1 MSS).

### Evolución de `cwnd` en las 4 ráfagas sucesivas (slow start, duplicación por RTT hasta `ssthresh`)

Contamos ráfagas como ciclos de éxito (p. ej. por RTT) que permiten completar el crecimiento de slow start:

1. Después de la 1.ª ráfaga: `cwnd = 2 KB`
2. Después de la 2.ª ráfaga: `cwnd = 4 KB`
3. Después de la 3.ª ráfaga: `cwnd = 8 KB`
4. Después de la 4.ª ráfaga: el siguiente paso en slow start sería `16 KB`, pero como `ssthresh = 9 KB` se deja de hacer _slow start_ al alcanzar/superar `ssthresh`. Por tanto `cwnd` queda limitado por `ssthresh` y pasa a congestión evitación.

**Resultado:** tras la 4.ª ráfaga `cwnd = 9 KB`.

