# Ejercicio 1

Aplicando VLSM, resolver los siguientes ejercicios:

## A)

Dada la red IP 65.0.0.0/24 se necesitan definir:

- 1 red de 80 hosts
- 2 redes de 10 hosts
- 1 red de 40 hosts

Para la primera red se necesitan 7 bits para hosts (2⁷ − 2 = 126 hosts).
Por lo tanto, la subred es:

**65.0.0.0/25** → cubre de 65.0.0.0 a 65.0.0.127

Para la red de 40 hosts se necesitan 6 bits para hosts (2⁶ − 2 = 62 hosts).
La siguiente subred disponible es:

**65.0.0.128/26** → cubre de 65.0.0.128 a 65.0.0.191

Finalmente, para las dos redes de 10 hosts se necesitan 4 bits para hosts (2⁴ − 2 = 14 hosts).
Las siguientes subredes disponibles son:

**65.0.0.192/28** → cubre de 65.0.0.192 a 65.0.0.207\
**65.0.0.208/28** → cubre de 65.0.0.208 a 65.0.0.223

## B)

Dada la red IP **100.0.0.0/16** se necesitan definir:

- 2 redes de **2000** hosts
- 2 redes de **500** hosts
- 20 redes de **300** hosts
- 50 redes de **200** hosts
- 1 red backbone de **74** direcciones

### Cálculo de tamaños (VLSM — ordenar de mayor a menor)

Para cada necesidad calculamos los bits de host necesarios: `bits = ceil(log2(hosts + 2))` y el prefijo `32 - bits`.

- **2000 hosts** → `ceil(log2(2000+2)) = 11` bits de host → **/21** (2¹¹ = 2048 direcciones → 2046 usables).
- **500 hosts** → `ceil(log2(500+2)) = 9` bits de host → **/23** (512 direcciones → 510 usables).
- **300 hosts** → `ceil(log2(300+2)) = 9` bits de host → **/23** (512 direcciones → 510 usables).
- **200 hosts** → `ceil(log2(200+2)) = 8` bits de host → **/24** (256 direcciones → 254 usables).
- **74 direcciones (backbone)** → `ceil(log2(74+2)) = 7` bits de host → **/25** (128 direcciones → 126 usables).

### Asignación (sin solapamientos). Se asigna desde 100.0.0.0/16 de mayor a menor:

1. **Dos subredes para 2000 hosts — /21**

   - **100.0.0.0/21**

     - Rango: **100.0.0.0 – 100.0.7.255**
     - Usables: **100.0.0.1 – 100.0.7.254**
     - Broadcast: **100.0.7.255**
     - Máscara: **255.255.248.0**

   - **100.0.8.0/21**

     - Rango: **100.0.8.0 – 100.0.15.255**
     - Usables: **100.0.8.1 – 100.0.15.254**
     - Broadcast: **100.0.15.255**
     - Máscara: **255.255.248.0**

2. **Veintidós subredes para 500 y 300 hosts — /23**
   (2 redes de 500 + 20 redes de 300 = 22 redes `/23`; se colocan contiguas a continuación)

   - Empieza en **100.0.16.0/23** y cada bloque avanza en pasos de 2 en el tercer octeto:

     - **100.0.16.0/23** → 100.0.16.0 – 100.0.17.255
     - **100.0.18.0/23** → 100.0.18.0 – 100.0.19.255
     - **100.0.20.0/23** → 100.0.20.0 – 100.0.21.255
     - **...** (continuar de 2 en 2)
     - Última de las 22: **100.0.58.0/23** → 100.0.58.0 – 100.0.59.255

   - Cada `/23`: usables `x.x.N.1 – x.x.(N+1).254`, broadcast `x.x.(N+1).255`, máscara `255.255.254.0`.

3. **Cincuenta subredes para 200 hosts — /24**

   - Empiezan justo después de la última `/23` asignada: **100.0.60.0/24**.
   - Se asignan **50** bloques consecutivos `/24`:

     - **100.0.60.0/24** → 100.0.60.0 – 100.0.60.255
     - **100.0.61.0/24** → 100.0.61.0 – 100.0.61.255
     - …
     - **100.0.109.0/24** → 100.0.109.0 – 100.0.109.255 _(60 + 49 = 109)_

   - Cada `/24`: usables `.1 – .254`, broadcast `.255`, máscara `255.255.255.0`.

4. **Backbone (74 direcciones) — /25**

   - Siguiente bloque libre: **100.0.110.0/25**

     - Rango: **100.0.110.0 – 100.0.110.127**
     - Usables: **100.0.110.1 – 100.0.110.126** (126 usables, suficiente para 74)
     - Broadcast: **100.0.110.127**
     - Máscara: **255.255.255.128**

### Resumen de bloques asignados (tabla)

|     Necesidad | Cantidad | Prefijo | Primera subred asignada | Última subred asignada       |
| ------------: | :------: | :-----: | :---------------------- | :--------------------------- |
|    2000 hosts |    2     |   /21   | 100.0.0.0/21            | 100.0.8.0/21                 |
|     500 hosts |    2     |   /23   | 100.0.16.0/23           | 100.0.18.0/23 (una de ellas) |
|     300 hosts |    20    |   /23   | 100.0.16.0/23           | 100.0.58.0/23                |
|     200 hosts |    50    |   /24   | 100.0.60.0/24           | 100.0.109.0/24               |
| Backbone (74) |    1     |   /25   | 100.0.110.0/25          | 100.0.110.0/25               |

**Espacio total usado aproximado:**

- 2 × /21 = 4096 direcciones
- 22 × /23 = 11264 direcciones
- 50 × /24 = 12800 direcciones
- 1 × /25 = 128 direcciones
  → **Total ≈ 28 288 direcciones** (dentro del /16 disponible: 65 536 direcciones).

# Ejercicio 2

Resolver el ejercicio (1b) teniendo en cuenta una capacidad de crecimiento del 20 % para cada subred sin considerar el backbone

## B)

### Cálculo de tamaños (bits y prefijos)

Usamos `bits = ceil(log2(hosts + 2))` y `prefijo = 32 - bits`.

* **2400 hosts** → `/20` → bloque = **4096** direcciones (4094 usables).
* **600 hosts**  → `/22` → bloque = **1024** direcciones (1022 usables).
* **360 hosts**  → `/23` → bloque = **512** direcciones (510 usables).
* **240 hosts**  → `/24` → bloque = **256** direcciones (254 usables).

### Asignación (ordenada de mayor a menor, desde `100.0.0.0/16`, sin solapamientos)

1. **Dos subredes para 2400 hosts — /20**

   * **100.0.0.0/20** → `100.0.0.0 – 100.0.15.255` (usables `100.0.0.1 – 100.0.15.254`)
   * **100.0.16.0/20** → `100.0.16.0 – 100.0.31.255` (usables `100.0.16.1 – 100.0.31.254`)

2. **Dos subredes para 600 hosts — /22**

   * **100.0.32.0/22** → `100.0.32.0 – 100.0.35.255` (usables `100.0.32.1 – 100.0.35.254`)
   * **100.0.36.0/22** → `100.0.36.0 – 100.0.39.255` (usables `100.0.36.1 – 100.0.39.254`)

3. **Veinte subredes para 360 hosts — /23**

   * Asignadas contiguas empezando en **100.0.40.0/23** y acabando en **100.0.78.0/23**.
   * Cada `/23` cubre 2 tercetos (ej.: `100.0.40.0 – 100.0.41.255`), máscara `255.255.254.0`.

4. **Cincuenta subredes para 240 hosts — /24**

   * Asignadas contiguas empezando en **100.0.80.0/24** y acabando en **100.0.129.0/24**.
   * Cada `/24` cubre `x.x.N.0 – x.x.N.255`, máscara `255.255.255.0`.

### Resumen de bloques asignados (tabla compacta)

| Necesidad original | Cantidad | Crecimiento 20% → hosts req. | Prefijo usado | Tamaño (direcciones) | Usables aprox. |
| -----------------: | :------: | :--------------------------: | :-----------: | :------------------: | :------------: |
|         2000 hosts |     2    |             2400             |      /20      |         4096         |      4094      |
|          500 hosts |     2    |              600             |      /22      |         1024         |      1022      |
|          300 hosts |    20    |              360             |      /23      |          512         |       510      |
|          200 hosts |    50    |              240             |      /24      |          256         |       254      |


### Espacio total usado aproximado

* 2 × /20 = **8192** direcciones
* 2 × /22 = **2048** direcciones
* 20 × /23 = **10240** direcciones
* 50 × /24 = **12800** direcciones
  **Total ≈ 33 280 direcciones** (dentro del /16 disponible: 65 536 direcciones).

# Ejercicio 3

## 1a) — Usando **2001:db8:1111::/48**

**Regla práctica IPv6:** para LANs en IPv6 se **usa /64** por subred (recomendación de RFC — necesaria para SLAAC y prácticas habituales). Aunque desde un punto de vista puramente numérico podríamos usar prefijos mayores, **usar /64 es la práctica correcta**.

Dispones de `2^(64-48)=2^16 = 65536` subredes `/64` en `2001:db8:1111::/48`, así que hay más que suficiente.

Asignación (ordenada por necesidad, sin solapamientos):

* **80 hosts → /64**

  * **2001:db8:1111:0000::/64**
  * Rango usable (ejemplo): `2001:db8:1111:0000::1` … `2001:db8:1111:0000:ffff:ffff:ffff:fffe`
  * Comentario: un /64 proporciona 2^64 direcciones, sobrado para 80 hosts.

* **40 hosts → /64**

  * **2001:db8:1111:0001::/64**

* **10 hosts → /64** (primera)

  * **2001:db8:1111:0002::/64**

* **10 hosts → /64** (segunda)

  * **2001:db8:1111:0003::/64**

**Resumen (tabla compacta)**

| Necesidad | Prefijo asignado        |
| --------: | :---------------------- |
|  80 hosts | 2001:db8:1111:0000::/64 |
|  40 hosts | 2001:db8:1111:0001::/64 |
|  10 hosts | 2001:db8:1111:0002::/64 |
|  10 hosts | 2001:db8:1111:0003::/64 |

## 1b) — Usando **2001:db8:1111:2200::/56**

Con un `/56` tienes `2^(64-56)=2^8 = 256` subredes `/64`. En el enunciado original (sin crecimiento) necesitabas 75 subredes en total (2 + 2 + 20 + 50 + 1 backbone = 75). 75 ≤ 256, por lo tanto **hay suficiente espacio**. (Si necesitas crecimiento extra, se puede repartir más /64s pues hay muchas disponibles.)

Asignación (mayor → menor, contigua, usando /64 para cada LAN):

* **Dos subredes para 2000 hosts** → asignamos dos `/64` contiguos:

  * **2001:db8:1111:2200::/64**
  * **2001:db8:1111:2201::/64**

* **Dos subredes para 500 hosts** → asignamos dos `/64` siguientes:

  * **2001:db8:1111:2202::/64**
  * **2001:db8:1111:2203::/64**

* **Veinte subredes para 300 hosts** → asignamos 20 `/64` contiguos empezando en:

  * **2001:db8:1111:2204::/64** … **2001:db8:1111:2217::/64**  *(20 bloques)*

* **Cincuenta subredes para 200 hosts** → asignamos 50 `/64` contiguos empezando en:

  * **2001:db8:1111:2218::/64** … **2001:db8:1111:2249::/64**  *(50 bloques)*

* **Backbone (74 direcciones)** — para enlaces punto a punto o backbone en IPv6 lo habitual es usar también un `/64` o un `/127` para enlaces punto-a-punto. Si querés mantener uniformidad y simplicidad, asignamos:

  * **2001:db8:1111:224A::/64**  *(suficiente para 74 direcciones; si prefieres eficiencia, podrías usar /127 por enlace punto-a-punto, pero /64 es la práctica estándar)*

**Resumen (contiguo y compacto)**

|          Tipo | Cantidad | Prefijos ejemplo (inicio → fin)                   |
| ------------: | :------: | :------------------------------------------------ |
|    2000 hosts |     2    | 2001:db8:1111:2200::/64 → 2001:db8:1111:2201::/64 |
|     500 hosts |     2    | 2001:db8:1111:2202::/64 → 2001:db8:1111:2203::/64 |
|     300 hosts |    20    | 2001:db8:1111:2204::/64 → 2001:db8:1111:2217::/64 |
|     200 hosts |    50    | 2001:db8:1111:2218::/64 → 2001:db8:1111:2249::/64 |
| Backbone (74) |     1    | 2001:db8:1111:224a::/64                           |

# Ejercicio 4

CORE

# Ejercicio 5

WIRESHARK

# Ejercicio 6

Perfecto — vamos paso a paso y con números claros.

**Datos iniciales**

* Tamaño del datagrama IPv4: **1100 bytes** (incluye encabezado IP).
* Encabezado IPv4 sin opciones: **20 bytes**.
* Payload (datos) = 1100 − 20 = **1080 bytes**.
* MTU del link = **200 bytes** (esto limita el tamaño total del datagrama en la interfaz —encabezado IP incluido—).
* Restricción de offset: los payloads de los fragmentos (excepto el último) deben ser múltiplos de **8 bytes** (porque el campo Fragment Offset se mide en unidades de 8 bytes).

## Determinar tamaño de payload por fragmento

Máximo payload por fragmento = MTU − encabezado = 200 − 20 = **180 bytes**.
Pero debe ser múltiplo de 8 (excepto último). El mayor múltiplo de 8 ≤ 180 es **176 bytes** (22 × 8).

Por tanto:

* Payload de los fragmentos completos = **176 bytes**.
* Cada fragmento completo tendrá longitud total (IP) = 176 + 20 = **196 bytes**.

Número de fragmentos completos necesarios:
1080 ÷ 176 = 6 con resto.
176 × 6 = 1056 bytes usados; queda resto = 1080 − 1056 = **24 bytes** (último fragmento).

Entonces hay **7 fragmentos** en total: 6 fragmentos con 176 bytes de payload y 1 fragmento final con 24 bytes de payload.

## Offset y flags (MF) de cada fragmento

Recordá: el campo *Fragment Offset* se expresa en unidades de 8 bytes.

Listado (ordenado):

1. **Fragmento 1**

   * Offset = 0 (unidades = 0)
   * Payload = 176 bytes
   * Longitud total IP = 196 bytes
   * MF (More Fragments) = **1**

2. **Fragmento 2**

   * Offset = 176 bytes → en unidades = 176/8 = **22**
   * Payload = 176 bytes
   * Longitud total IP = 196 bytes
   * MF = **1**

3. **Fragmento 3**

   * Offset = 352 bytes → unidades = **44**
   * Payload = 176 bytes
   * Longitud total IP = 196 bytes
   * MF = **1**

4. **Fragmento 4**

   * Offset = 528 bytes → unidades = **66**
   * Payload = 176 bytes
   * Longitud total IP = 196 bytes
   * MF = **1**

5. **Fragmento 5**

   * Offset = 704 bytes → unidades = **88**
   * Payload = 176 bytes
   * Longitud total IP = 196 bytes
   * MF = **1**

6. **Fragmento 6**

   * Offset = 880 bytes → unidades = **110**
   * Payload = 176 bytes
   * Longitud total IP = 196 bytes
   * MF = **1**

7. **Fragmento 7 (último)**

   * Offset = 1056 bytes → unidades = 1056/8 = **132**
   * Payload = **24 bytes** (no necesita ser múltiplo de 8)
   * Longitud total IP = 24 + 20 = **44 bytes**
   * MF = **0** (último fragmento)

Verificación rápida: payload total = 6×176 + 24 = 1056 + 24 = **1080 bytes** (coincide con los datos originales).

Bytes transmitidos totales (IP incl.): 6×196 + 44 = 1176 + 44 = **1220 bytes**.


## Overhead (porcentaje de datos de cabecera) — comparar con solución MTU = 1500

Primero, calculamos bytes de cabecera IP:

* Con MTU = 200 (fragmentación): número de fragmentos = 7 → cabeceras totales = 7 × 20 = **140 bytes**.
  Total transmitido = payload (1080) + headers (140) = **1220 bytes**.

* Con MTU = 1500 (no hay fragmentación): todo cabe en un solo datagrama. Cabeceras = 1 × 20 = **20 bytes**.
  Total transmitido = 1100 bytes (ya incluye la cabecera).

Ahora porcentajes:

* **Escenario MTU 200:** porcentaje de cabecera sobre total transmitido = 140 / 1220 × 100 ≈ **11.48 %**.
* **Escenario MTU 1500:** porcentaje de cabecera sobre total transmitido = 20 / 1100 × 100 ≈ **1.82 %**.

También puedes ver el **sobrecoste absoluto** de fragmentar: cabeceras extras = 140 − 20 = **120 bytes** adicionales. En términos relativos contra el caso MTU=1500: (140/20)=7× más cabeceras; o ( (140−20)/20 )*100 = **600%** más cabeceras.

## ¿Es necesario hacer padding a nivel Ethernet en el último fragmento?

Sí. Ethernet tiene un **payload mínimo de 46 bytes** (trama mínima 64 bytes contando cabecera y FCS). El último fragmento IP tiene longitud total IP = **44 bytes** (20 bytes header + 24 bytes payload), por lo que el campo de payload de la trama Ethernet sería de 44 bytes < 46 bytes mínimo.

Por tanto, a nivel **Ethernet** se **deben añadir 2 bytes de padding** en la última trama para alcanzar el mínimo de 46 bytes de carga útil. (Este padding no forma parte del datagrama IP; es agregado por la capa enlace.)


# Ejercicio 7

### Cálculo de fragmentación

**Datos:**

* MTU enlace n2–n3 = 400 bytes
* Overhead IPv4 = 20 bytes
* Overhead link layer = 18 bytes
* Datos a enviar = 1000 bytes

**Bytes disponibles para datos por fragmento:**

$$
MTU_{enlace} − link layer overhead − IPv4 header = 400 − 18 − 20 = 362 bytes
$$

**Número de fragmentos:**

$$
Número de fragmentos = ceil(1000 / 362) = 3
$$

**Tamaño de cada fragmento (incluyendo headers):**

* Fragmento 1: 362 + 20 + 18 = 400 bytes
* Fragmento 2: 362 + 20 + 18 = 400 bytes
* Fragmento 3: 276 + 20 + 18 = 314 bytes

**Total transmitido entre n2–n3:**

$$
400 + 400 + 314 = 1114 bytes
$$

**Caso DF = 1:**

* Los datagramas no se pueden fragmentar.
* Cada datagrama original (1000 + 20 bytes = 1020 bytes) excede la MTU de 400.
* El router n2 descarta el datagrama y envía un ICMP “Fragmentation Needed” a n1.

# Ejercicio 9

**Cómo se resuelve la fragmentación en IPv6:**

* En IPv6, **los routers intermedios no fragmentan** los paquetes como en IPv4.
* La fragmentación se realiza **solo en el host de origen**, usando un **Fragment Header** adicional de 8 bytes.
* Si un paquete es más grande que la MTU del enlace de salida, el host origen debe dividirlo en fragmentos que quepan en la MTU más pequeña.
* Para determinar el tamaño máximo de fragmento que puede enviarse sin ser descartado, se utiliza **Path MTU Discovery (PMTUD)**, que permite al host origen conocer la MTU mínima a lo largo del camino hacia el destino.

**Qué se debería cambiar para que funcione:**

* Aumentar la **MTU del enlace n2–n3** a al menos 1280 bytes, que es el mínimo recomendado en IPv6, o
* Implementar **PMTUD** para que el host origen fragmente correctamente los paquetes antes de enviarlos, asegurando que ningún fragmento exceda la MTU de los enlaces intermedios.

# Ejercicio 10

### RFC 1918 y su relación con NAT/NAPT

* Define **rangos de direcciones IPv4 privadas** que no son enrutables en Internet:

```
10.0.0.0 – 10.255.255.255       (10/8)
172.16.0.0 – 172.31.255.255     (172.16/12)
192.168.0.0 – 192.168.255.255   (192.168/16)
```

* Estas direcciones son **solo para uso interno** dentro de redes privadas y no deben aparecer directamente en Internet.

**Relación con NAT/NAPT:**

* NAT (Network Address Translation) y NAPT (Network Address and Port Translation) permiten que **hosts con direcciones privadas** puedan comunicarse con Internet.
* El router realiza la traducción de las direcciones privadas definidas por RFC 1918 a **direcciones públicas** asignadas por el proveedor de Internet.
* NAPT además traduce los **puertos**, permitiendo que múltiples hosts privados compartan una única dirección pública.

En resumen, RFC 1918 define las direcciones privadas que NAT/NAPT convierte para poder acceder a Internet.

