# Practica 5

## Ejercicio 1

¿Cuáles son las funciones de la capa de aplicación? Compare funcionalidades entre modelo OSI y TCP/IP

La capa de aplicación provee servicios directos a los procesos del usuario: identificación de participantes, establecimiento/terminación de sesiones lógicas, negociación de parámetros, representación de datos y servicios comunes como correo, transferencia de archivos o web. En el modelo OSI la capa de aplicación está separada de las capas de presentación y sesión (que gestionan formato/codificación y control de diálogo); en el modelo TCP/IP esas tres funcionalidades se agrupan en una sola capa de aplicación, de modo que los protocolos de usuario (HTTP, SMTP, FTP, etc.) implementan tanto la representación de datos como la gestión de sesión según lo requieran.

## Ejercicio 2

¿Qué es un User-Agent? Nombre algunos que conozca e indique qué protocolo de aplicación soportan?

Un User-Agent es una cadena de texto que un cliente envía en una solicitud para identificarse ante el servidor. Esta cadena generalmente informa sobre el tipo de aplicación, el sistema operativo, el proveedor del software y la versión del cliente.

Algunos ejemplos son:

- **Navegadores web:** Como Google Chrome o Mozilla Firefox. Utilizan principalmente el protocolo **HTTP/HTTPS**.
- **Clientes de correo:** Como Microsoft Outlook o Mozilla Thunderbird. Soportan los protocolos **SMTP**, **POP3** e **IMAP**.
- **Rastreadores web (crawlers):** Como Googlebot, que indexa páginas para el motor de búsqueda de Google. Usa **HTTP/HTTPS**.
- **Herramientas de línea de comandos:** Como `cURL` o `Wget`, que pueden realizar solicitudes a servidores y soportan múltiples protocolos como **HTTP, HTTPS y FTP**.

## Ejercicio 3

Cuál es el objetivo del protocolo DNS? ¿Cómo funciona? ¿Es posible que Internet funcione sin este servicio?

El objetivo principal del **Protocolo de Sistema de Nombres de Dominio (DNS)** es traducir nombres de dominio legibles por humanos (ej: `www.google.com`) a direcciones IP numéricas (ej: `142.250.78.196`) que las computadoras utilizan para identificarse entre sí en la red. Esencialmente, funciona como la "guía telefónica" de Internet.

**Funcionamiento:**
El proceso es jerárquico:

1. Un usuario introduce un nombre de dominio en su navegador.
2. El sistema operativo del usuario consulta a un servidor DNS recursivo (generalmente proporcionado por el ISP).
3. Si el servidor recursivo no tiene la dirección en su caché, consulta a un servidor DNS raíz.
4. El servidor raíz lo dirige al servidor de dominio de nivel superior (TLD) apropiado (ej: para `.com`, `.org`, `.ar`).
5. El servidor TLD lo dirige al servidor de nombres autorizado para ese dominio específico.
6. Este servidor de nombres autorizado devuelve la dirección IP correcta al servidor recursivo.
7. El servidor recursivo envía la IP al cliente, que finalmente puede establecer la conexión con el servidor de destino.

**¿Es posible que Internet funcione sin DNS?**
Técnicamente, sí. La comunicación en Internet se basa en direcciones IP. Si un usuario conociera la dirección IP de cada sitio web que quiere visitar, podría ingresarla directamente en el navegador. Sin embargo, en la práctica, sería inviable para los humanos memorizar millones de direcciones IP numéricas. Por lo tanto, aunque Internet podría funcionar a un nivel fundamental sin DNS, sería completamente inmanejable y no se podría utilizar de la forma en que lo conocemos hoy. DNS es un servicio crítico para la usabilidad de Internet.

## Ejercicio 4

¿Qué protocolo de la capa de transporte utiliza? ¿Qué puertos?

El protocolo DNS utiliza principalmente **UDP (User Datagram Protocol)** para las consultas estándar debido a su rapidez y baja sobrecarga. Sin embargo, cuando el tamaño de la respuesta excede los 512 bytes o para operaciones críticas como las transferencias de zona (AXFR/IXFR) entre servidores, utiliza **TCP (Transmission Control Protocol)** para garantizar la entrega fiable de los datos.

Tanto para UDP como para TCP, DNS utiliza el puerto **53**.

## Ejercicio 5

¿Qué es un root-server? ¿Qué son los TLD? Diferencias entre gTLD y ccTLD? Indique 3 ejemplos de c/u. Cómo se acceden y que tipo de consultas se les hacen.

- **Root-server (Servidor Raíz):** Es uno de los 13 servidores (lógicos, distribuidos globalmente en cientos de servidores físicos) que operan en la raíz de la jerarquía del DNS. Su función principal es responder a las consultas de los servidores DNS recursivos indicándoles cuáles son los servidores de nombres autorizados para el Dominio de Nivel Superior (TLD) correspondiente a la consulta.

- **TLD (Top-Level Domain - Dominio de Nivel Superior):** Es el segmento final de un nombre de dominio, lo que sigue al último punto (ej: `.com`, `.org`, `.ar`).

- **Diferencias y ejemplos:**

  - **gTLD (generic Top-Level Domain):** Son dominios de nivel superior genéricos, no asociados a un país.
    - **Ejemplos:** `.com` (comercial), `.org` (organización), `.net` (red).
  - **ccTLD (country code Top-Level Domain):** Son dominios de nivel superior de código de país, asignados a un país o territorio específico.
    - **Ejemplos:** `.ar` (Argentina), `.es` (España), `.br` (Brasil).

- **Acceso y tipo de consultas:**
  - No se acceden directamente por los usuarios finales. Son los servidores DNS recursivos (como los de un ISP) los que les consultan cuando no tienen una respuesta en su caché.
  - Se les hacen **consultas iterativas**. Por ejemplo, un recursor le pregunta a un servidor raíz por `www.google.com`, y el servidor raíz no sabe la IP, pero responde con la dirección de los servidores TLD para `.com`. Luego, el recursor le pregunta a uno de esos servidores TLD, que a su vez le responderá con la dirección del servidor de nombres autorizado para `google.com`.

## Ejercicio 6

¿Qué es el resolver? ¿Cómo se configura en Linux y en Windows? ¿Qué tipos de resolvers hay?

- **Resolver:** Es el componente del lado del cliente en el sistema DNS. Su función es iniciar y gestionar el proceso de consulta para traducir un nombre de dominio a una dirección IP. Es la parte del sistema operativo que una aplicación (como un navegador) utiliza para buscar una dirección IP.

- **Configuración:**

  - **Linux:** La configuración principal se encuentra en el archivo `/etc/resolv.conf`. Este archivo contiene las direcciones IP de los servidores DNS a los que el resolver debe consultar, utilizando la directiva `nameserver`. Por ejemplo:

    ```
    nameserver 8.8.8.8
    nameserver 8.8.4.4
    ```

    En sistemas modernos, la gestión de este archivo a menudo es manejada por servicios como `systemd-resolved` o `NetworkManager`.

  - **Windows:** Generalmente se configura a través de la interfaz gráfica: `Panel de control > Redes e Internet > Centro de redes y recursos compartidos > Cambiar configuración del adaptador`. Se hace clic derecho en la conexión de red, se va a `Propiedades`, se selecciona `Protocolo de Internet versión 4 (TCP/IPv4)`, se hace clic en `Propiedades` y se introducen las direcciones de los servidores DNS preferido y alternativo. También se puede hacer por línea de comandos con `netsh`.

- **Tipos de Resolvers:**
  - **Stub Resolver:** Es el tipo más básico y se encuentra en la mayoría de los dispositivos cliente (PCs, smartphones). No realiza la resolución completa por sí mismo. Simplemente reenvía la solicitud a un servidor DNS recursivo y espera la respuesta final. El resolver del sistema operativo es un stub resolver.
  - **Recursive Resolver (o Full Resolver):** Es un servidor DNS que realiza el proceso completo de resolución en nombre del stub resolver. Si no tiene la respuesta en su caché, consulta a los servidores raíz, luego a los servidores TLD y finalmente a los servidores de nombres autorizados hasta obtener la dirección IP, que luego devuelve al cliente. Los DNS de los ISP o los públicos como Google (8.8.8.8) son resolvers recursivos.

## Ejercicio 7

¿Cuándo una respuesta es autoritativa?

Una respuesta de DNS es **autoritativa** cuando es proporcionada directamente por el servidor de nombres que tiene la responsabilidad oficial sobre el dominio consultado. Este servidor, conocido como **servidor de nombres autorizado**, es la fuente original y definitiva de los registros DNS (como los registros A, MX, CNAME, etc.) para ese dominio.

En otras palabras:

- **Respuesta Autoritativa:** Proviene del servidor que gestiona los registros del dominio. Es la "verdad absoluta" en ese momento. En la cabecera del paquete de respuesta DNS, el flag `AA` (Authoritative Answer) está activado.
- **Respuesta No Autoritativa:** Proviene de la caché de un servidor DNS recursivo (como el de un ISP o Google DNS). Este servidor ya había resuelto la consulta previamente y guardó el resultado para responder más rápido en futuras peticiones. Aunque suele ser correcta, podría estar desactualizada si los registros originales han cambiado recientemente y la entrada en caché aún no ha expirado (según su TTL).

## Ejercicio 8

Explique las diferencias entre una consulta iterativa y una recursiva

La diferencia fundamental entre una consulta DNS recursiva y una iterativa radica en quién asume la responsabilidad de completar la resolución del nombre de dominio.

- **Consulta Recursiva:**

  - El cliente (generalmente un stub resolver en un PC) le pide a un servidor DNS (un resolver recursivo, como el del ISP) que le proporcione la respuesta final.
  - La responsabilidad recae completamente en el servidor DNS contactado. Este servidor debe hacer todo el trabajo necesario (contactar a los servidores raíz, TLD y autorizados) para encontrar la dirección IP y devolverla al cliente.
  - El cliente solo hace una pregunta y espera una respuesta definitiva: la dirección IP o un mensaje de error.
  - **Ejemplo:** Tu PC le pregunta al DNS de tu proveedor de internet por `www.google.com`. El DNS del proveedor hace todas las consultas necesarias por su cuenta y te devuelve la IP final.

- **Consulta Iterativa:**
  - El cliente le pregunta a un servidor DNS y, si este no tiene la respuesta final, le devuelve una referencia (un "puntero") al siguiente servidor DNS en la jerarquía que podría saber la respuesta.
  - La responsabilidad recae en el cliente, que debe "iterar" y realizar consultas sucesivas a los servidores referidos hasta encontrar el que tiene la respuesta autoritativa.
  - El servidor contactado solo da la mejor información que tiene, que a menudo es "No lo sé, pero pregúntale a este otro servidor".
  - **Ejemplo:** Un resolver recursivo le pregunta a un servidor raíz por `www.google.com`. El servidor raíz responde: "No tengo la IP, pero aquí tienes la dirección de los servidores TLD de `.com`". Luego, el resolver recursivo le pregunta a un servidor TLD, y así sucesivamente. Esta comunicación entre servidores DNS es iterativa.

## Ejercicio 9

Indique un posible orden de los nombres de servidores consultados desde la raı́z para resolver el nombre <www.info.unlp.edu.ar>

Asumiendo que la consulta es iniciada por un resolver recursivo que no tiene ninguna información en su caché, el orden de las consultas iterativas sería el siguiente:

1. El resolver recursivo consulta a uno de los **servidores raíz (`.`)** para encontrar `www.info.unlp.edu.ar`.
2. El servidor raíz no conoce la dirección, pero sabe quién gestiona el TLD `.ar`. Responde con una referencia a los **servidores de nombres de `.ar`**.
3. El resolver recursivo consulta a un servidor de nombres de **`.ar`**.
4. Este servidor no conoce la dirección final, pero sabe quién gestiona el dominio de segundo nivel `.edu.ar`. Responde con una referencia a los **servidores de nombres de `.edu.ar`**.
5. El resolver recursivo consulta a un servidor de nombres de **`.edu.ar`**.
6. Este servidor tampoco conoce la dirección, pero sabe quién gestiona el dominio `.unlp.edu.ar`. Responde con una referencia a los **servidores de nombres autorizados de `unlp.edu.ar`**.
7. El resolver recursivo consulta al servidor de nombres autorizado de **`unlp.edu.ar`**.
8. Finalmente, este servidor es la autoridad para el dominio y tiene el registro `A` o `AAAA` para `www.info.unlp.edu.ar`. Responde con la dirección IP correspondiente, marcando la respuesta como **autoritativa**.

## Ejercicio 10

Describa la relación de los servidores primario/secundario, determine cuales son los servidores de DNS autoritativos de los dominios .com , .ar , .yahoo.com , edu.ar e indique cuál es el primario.

### Relación de Servidores Primario y Secundario

Para garantizar la redundancia y la distribución de la carga, una zona DNS (es decir, un dominio) es gestionada por varios servidores de nombres autorizados. La relación entre ellos es la siguiente:

- **Servidor Primario (Maestro):** Es el servidor que contiene la copia original y editable de los registros de la zona DNS. Todas las modificaciones de los registros del dominio (añadir un subdominio, cambiar una IP, etc.) se realizan en este servidor. Por cada zona, solo puede haber un servidor primario.
- **Servidor Secundario (Esclavo):** Contiene una copia de solo lectura de los registros de la zona. Se sincroniza periódicamente con el servidor primario para obtener las actualizaciones. El proceso de sincronización se llama **transferencia de zona**. Su función es responder a las consultas DNS en caso de que el servidor primario no esté disponible o para balancear la carga de peticiones. Puede haber múltiples servidores secundarios para una misma zona.

Esta configuración asegura que el servicio DNS para un dominio siga funcionando incluso si el servidor primario falla.

### Servidores Autoritativos y Primarios

Para determinar los servidores autoritativos se consulta el registro `NS` (Name Server) del dominio. Para identificar al primario, se consulta el registro `SOA` (Start of Authority), que en su campo MNAME (Master Name) especifica cuál es el servidor primario para esa zona.

_(Nota: Los resultados pueden variar con el tiempo, ya que la infraestructura de red cambia. Estos son los resultados a la fecha de la consulta.)_

**1. Dominio `.com`**

- **Servidores Autoritativos (NS):**
  - `a.gtld-servers.net.`
  - `b.gtld-servers.net.`
  - `c.gtld-servers.net.`
  - ... (hasta `m.gtld-servers.net.`)
- **Servidor Primario (del registro SOA):** `a.gtld-servers.net.`

**2. Dominio `.ar`**

- **Servidores Autoritativos (NS):**
  - `a.lactld.org.`
  - `b.lactld.org.`
  - `c.lactld.org.`
  - `d.lactld.org.`
  - `ns1.nic.ar.`
  - `ns2.nic.ar.`
- **Servidor Primario (del registro SOA):** `ns1.nic.ar.`

**3. Dominio `yahoo.com`**

- **Servidores Autoritativos (NS):**
  - `ns1.yahoo.com.`
  - `ns2.yahoo.com.`
  - `ns3.yahoo.com.`
  - `ns4.yahoo.com.`
  - `ns5.yahoo.com.`
- **Servidor Primario (del registro SOA):** `ns1.yahoo.com.`

**4. Dominio `edu.ar`**

- **Servidores Autoritativos (NS):**
  - `ns1.nic.ar.`
  - `ns2.nic.ar.`
  - `a.lactld.org.`
  - ... (y otros servidores de `lactld.org`)
- **Servidor Primario (del registro SOA):** `ns1.nic.ar.`

## Ejercicio 11

Explique para que se usan cada uno of los siguientes tipos de registros de DNS:

- **SOA (Start of Authority):** Proporciona información administrativa esencial sobre una zona (dominio). Incluye el nombre del servidor primario (maestro), el correo del administrador, el número de serie de la zona (que indica si ha habido cambios) y varios temporizadores que controlan la frecuencia con la que los servidores secundarios deben verificar si hay actualizaciones. Es el primer registro y el más importante de cualquier archivo de zona.

- **A (Address):** Es el registro más común. Mapea un nombre de host (como `www.google.com`) a una dirección **IPv4** (como `142.250.78.196`). Es el registro fundamental para la navegación web y la conexión a servicios en redes IPv4.

- **AAAA (IPv6 Address):** Es el equivalente del registro A, pero para **IPv6**. Mapea un nombre de host a una dirección IPv6 de 128 bits. Su nombre proviene de que IPv6 (128 bits) es 4 veces más grande que IPv4 (32 bits), de ahí "AAAA".

- **CNAME (Canonical Name):** Crea un alias o apodo para un nombre de host. Permite que un nombre de host apunte a otro nombre de host en lugar de a una IP. Por ejemplo, `ftp.midominio.com` podría ser un CNAME que apunta a `servidor1.midominio.com`. Si la IP de `servidor1` cambia, solo hay que actualizar su registro A, y `ftp.midominio.com` apuntará automáticamente a la nueva IP.

- **PTR (Pointer):** Realiza la función inversa a un registro A o AAAA. Mapea una dirección IP a un nombre de host. Se utiliza principalmente en **búsquedas de DNS inverso** (reverse DNS lookup), que son comunes para verificar la identidad de un remitente de correo electrónico y combatir el spam.

- **NS (Name Server):** Delega la autoridad de un dominio o subdominio a un conjunto específico de servidores de nombres. Este registro le dice a Internet qué servidores son los autorizados para responder a las consultas sobre los registros DNS de ese dominio.

- **MX (Mail Exchanger):** Especifica cuáles son los servidores de correo responsables de recibir los correos electrónicos enviados a un dominio. Cada registro MX tiene un valor de prioridad (un número más bajo indica mayor prioridad) para definir el orden en que se deben intentar contactar los servidores.

## Ejercicio 12

¿Qué problemas conllevarı́a cambiar la dirección IP de, por ejemplo, el nombre de servidor de mail con la información de la misma que se encuentra almacenada en un caché DNS? ¿Cómo podría ser minimizado?

### Problemas al Cambiar la Dirección IP

Cuando se cambia la dirección IP de un servidor de correo (cuyo nombre está en un registro MX), el principal problema es la **propagación de DNS** y el **almacenamiento en caché**.

1. **Inaccesibilidad Temporal y Pérdida de Correo:** Los servidores DNS recursivos y los clientes de todo el mundo tienen almacenada en su caché la antigua dirección IP asociada al nombre del servidor de correo. Esta entrada en caché tiene un período de validez llamado **TTL (Time to Live)**. Mientras la entrada en caché no expire (es decir, durante el tiempo que indica el TTL), cualquier servidor de correo que intente enviar un email a ese dominio resolverá el nombre a la **antigua y ahora incorrecta dirección IP**. Esto causará un fallo en la entrega del correo. Los servidores de correo que envían los mensajes reintentarán la entrega durante un tiempo, pero si la caché no se actualiza antes de que se agoten los reintentos, el correo será devuelto al remitente como no entregado (bounce).

2. **Período de Inconsistencia:** Durante el período de propagación, algunos servidores de correo en Internet ya tendrán la nueva IP (porque su caché expiró), mientras que otros seguirán usando la antigua. Esto crea un estado inconsistente donde algunos correos llegan correctamente y otros fallan.

### Cómo Minimizar el Problema

La estrategia para minimizar este problema se basa en la gestión proactiva del **TTL** del registro DNS (específicamente, el registro `A` o `AAAA` del hostname al que apunta el registro `MX`).

El procedimiento recomendado es:

1. **Bajar el TTL (con antelación):** Varios días o al menos un período de tiempo superior al TTL original antes del cambio programado, el administrador debe editar el registro DNS del servidor de correo y reducir su valor de TTL a un número muy bajo (por ejemplo, 300 segundos o 5 minutos).

2. **Esperar a que el TTL antiguo expire:** Se debe esperar a que el TTL original más largo expire de todas las cachés de Internet. Por ejemplo, si el TTL original era de 24 horas (86400 segundos), se debe esperar al menos 24 horas después de haberlo bajado para asegurarse de que todos los servidores recursivos ahora cachearán el registro por solo 5 minutos (el nuevo y corto TTL).

3. **Realizar el Cambio de IP:** Una vez que el TTL corto se ha propagado, se realiza el cambio de la dirección IP en el registro `A`/`AAAA` en el servidor DNS autoritativo.

4. **Minimización del Impacto:** Ahora, cuando los servidores DNS consulten el nombre del servidor de correo, obtendrán la nueva IP. Aquellos que todavía tengan la IP antigua en caché la mantendrán por un máximo de 5 minutos (el nuevo y corto TTL) antes de volver a consultar y obtener la dirección correcta. Esto reduce el período de posible pérdida de correos de horas o días a solo unos pocos minutos.

5. **Restaurar el TTL (opcional pero recomendado):** Una vez que se ha verificado que la migración ha sido exitosa y el nuevo servidor de correo funciona correctamente, se puede volver a subir el TTL a un valor más alto y estándar (ej: 3600 segundos o más) para reducir la carga sobre los servidores DNS autoritativos.

## Ejercicio 13

Mediante algunos of los comandos de DNS (dig, nslookup o host), contestar las siguientes preguntas:

**a) ¿Cuántos servidores raíces (ROOT-Servers) hay? Indique las direcciones IP del servidor “B” y “J”.**

Hay **13 servidores raíz lógicos**, nombrados de la letra "A" a la "M".

- **Comando:** `dig NS .`

Para obtener las direcciones IP:

- **Comando para B:** `dig A b.root-servers.net. && dig AAAA b.root-servers.net.`
- **Comando para J:** `dig A j.root-servers.net. && dig AAAA j.root-servers.net.`

- **Direcciones del servidor "B":**
  - IPv4: `199.9.14.201`
  - IPv6: `2001:500:200::b`
- **Direcciones del servidor "J":**
  - IPv4: `192.58.128.30`
  - IPv6: `2001:503:c27::2:30`

**b) ¿Cuántos servidores de correo aceptan mails en gmail.com? ¿Qué tipo de consulta es enviada para obtener la respuesta?**

- **Comando:** `dig MX gmail.com`
- **Respuesta:** Hay **5 servidores de correo** que aceptan mails para `gmail.com`.
  - `gmail-smtp-in.l.google.com`
  - `alt1.gmail-smtp-in.l.google.com`
  - `alt2.gmail-smtp-in.l.google.com`
  - `alt3.gmail-smtp-in.l.google.com`
  - `alt4.gmail-smtp-in.l.google.com`
- **Tipo de consulta:** Se envía una consulta por registros de tipo **MX (Mail Exchanger)**.

**c) ¿Cuál es el servidor SMTP principal de gmail.com? ¿En base a qué información se puede determinar esto? ¿Utiliza IPv6 Gmail ?**

- **Servidor SMTP principal:** `gmail-smtp-in.l.google.com`
- **Información para determinarlo:** Se determina por el **valor de prioridad** que acompaña a cada registro MX. El servidor con el número de prioridad más bajo es el principal. En este caso, `gmail-smtp-in.l.google.com` tiene una prioridad de `5`, mientras que los otros (`alt1`, `alt2`, etc.) tienen prioridades más altas (`10`, `20`, etc.).
- **Uso de IPv6:** Sí, Gmail utiliza IPv6. Si se consulta por el registro `AAAA` del servidor de correo principal, se obtiene una dirección IPv6.
  - **Comando:** `dig AAAA gmail-smtp-in.l.google.com`

**d) Realice esta misma consulta contra hotmail.com. Nota alguna diferencia en las respuestas**

- **Comando:** `dig MX hotmail.com`
- **Respuesta:** hotmail.com tiene **1 servidor de correo**: `hotmail-com.olc.protection.outlook.com` con prioridad `0`.
- **Diferencias:** La principal diferencia es la infraestructura. Gmail utiliza múltiples servidores de correo con diferentes prioridades para redundancia y balanceo de carga, mientras que hotmail.com (Outlook) en esta respuesta apunta a un único nombre de host de alta disponibilidad (`olc.protection.outlook.com`), que a su vez puede resolver a múltiples IPs. Los nombres de los servidores y las prioridades son completamente diferentes, ya que pertenecen a distintas compañías (Google vs. Microsoft).

**e) ¿Cuántos servidores de nombre existen para google.com? ¿Siempre se obtiene la misma respuesta?**

- **Comando:** `dig NS google.com`
- **Respuesta:** Existen **4 servidores de nombres** para `google.com`:
  - `ns1.google.com`
  - `ns2.google.com`
  - `ns3.google.com`
  - `ns4.google.com`
- **¿Siempre se obtiene la misma respuesta?:** Sí, la lista de **servidores de nombres autorizados** (registros NS) para un dominio es estable y la respuesta debería ser siempre la misma. Lo que puede cambiar con cada consulta son las direcciones IP asociadas al dominio `google.com` (registro A o AAAA) debido a técnicas de balanceo de carga y GeoDNS.

**f ) ¿Cuál es el nombre asociado a la dirección IP 163.10.0.145? ¿Qué tipo de consulta DNS es enviada para obtener la respuesta?**

- **Comando:** `dig -x 163.10.0.145`
- **Nombre asociado:** `presidencia.unlp.edu.ar`
- **Tipo de consulta:** Es una **búsqueda de DNS inversa (reverse lookup)**. Se envía una consulta por un registro de tipo **PTR (Pointer)** al dominio especial `145.0.10.163.in-addr.arpa`.

## Ejercicio 17

¿Qué protocolo de la capa de transporte utiliza HTTP? ¿Qué puertos?

- **Protocolo de Transporte:** HTTP (Hypertext Transfer Protocol) utiliza **TCP (Transmission Control Protocol)**. TCP es un protocolo orientado a la conexión que garantiza la entrega fiable y ordenada de los datos, lo cual es esencial para que los recursos web como páginas, imágenes, y scripts se carguen de manera íntegra y correcta.

- **Puertos:**
  - **HTTP** utiliza el puerto estándar **80**.
  - **HTTPS** (HTTP Secure), su versión cifrada, utiliza el puerto estándar **443**.

## Ejercicio 18

¿Cuáles son las principales diferencias entre HTTP 1.0 y HTTP 1.1?

HTTP 1.1 introdujo mejoras significativas sobre HTTP 1.0, enfocadas principalmente en el rendimiento y la eficiencia. Las principales diferencias son:

1. **Conexiones Persistentes (Keep-Alive):**

   - **HTTP 1.0:** Por cada solicitud de un recurso (ej: un HTML, una imagen, un CSS), se abría una nueva conexión TCP. Si una página necesitaba 10 recursos, se establecían y cerraban 10 conexiones TCP, lo cual es muy ineficiente y lento por el overhead del handshake de TCP.
   - **HTTP 1.1:** Introduce las **conexiones persistentes por defecto**. La conexión TCP se mantiene abierta después de una solicitud, permitiendo que múltiples solicitudes y respuestas se envíen a través de la misma conexión. Esto reduce drásticamente la latencia y el consumo de recursos.

2. **Cabecera `Host`:**

   - **HTTP 1.0:** La cabecera `Host` era opcional. Esto hacía muy difícil para un servidor con una unica dirección IP alojar múltiples sitios web (hosting virtual).
   - **HTTP 1.1:** La cabecera `Host` es **obligatoria**. Esto permite al servidor identificar a qué sitio web se dirige la solicitud, haciendo posible el hosting virtual basado en nombres, una característica fundamental de la web moderna.

3. **Pipelining:**

   - **HTTP 1.0:** El cliente debía esperar la respuesta a una solicitud antes de poder enviar la siguiente.
   - **HTTP 1.1:** Permite el **pipelining**, donde un cliente puede enviar múltiples solicitudes a través de una misma conexión persistente sin esperar las respuestas. Aunque las respuestas deben llegar en el mismo orden que las solicitudes, esto mejora el tiempo de carga de la página. (Nota: esta característica fue superada por el multiplexado en HTTP/2).

4. **Mejoras en el Caching:**

   - **HTTP 1.1:** Introduce cabeceras de control de caché más avanzadas y robustas, como `ETag`, `If-Unmodified-Since`, `If-Match`, y `Cache-Control`, que permiten a los navegadores y proxies gestionar la caché de manera más eficiente que la simple cabecera `Expires` de HTTP 1.0.

5. **Transferencia Codificada en Trozos (Chunked Transfer Encoding):**
   - **HTTP 1.1:** Permite al servidor enviar contenido en una serie de trozos (chunks) sin necesidad de conocer el tamaño total del contenido de antemano. Esto es muy útil para contenido generado dinámicamente, donde el tamaño final no se sabe hasta que se termina de generar.

## Ejercicio 19

¿Qué cambios hace HTTP 2?

HTTP/2 es una revisión mayor del protocolo HTTP y fue diseñado para solucionar las limitaciones de rendimiento de HTTP/1.1. Mantiene la misma semántica (métodos, códigos de estado, cabeceras), pero cambia cómo se empaquetan y transportan los datos. Sus cambios clave son:

1. **Protocolo Binario:**

   - A diferencia de HTTP/1.1 que es un protocolo de texto plano, HTTP/2 es **binario**. Esto lo hace más compacto, eficiente y menos propenso a errores de parseo. Las tramas (frames) binarias son más fáciles de procesar para las máquinas.

2. **Multiplexación Completa (Multiplexing):**

   - Es la característica más importante. Permite enviar múltiples solicitudes y respuestas de forma concurrente sobre una **única conexión TCP**. Soluciona el problema de "bloqueo por cabecera de línea" (Head-of-Line blocking) que existía en HTTP/1.1, donde una solicitud lenta podía bloquear a todas las que venían detrás en la misma conexión. Con la multiplexación, los recursos se dividen en tramas que se intercalan y se reensamblan al llegar, por lo que ninguna solicitud bloquea a otra.

3. **Compresión de Cabeceras (HPACK):**

   - HTTP/2 utiliza un algoritmo de compresión llamado **HPACK** para reducir el tamaño de las cabeceras. Muchas cabeceras son repetitivas entre solicitudes (User-Agent, Accept, etc.). HPACK mantiene una tabla de cabeceras comunes en ambos lados de la conexión, reduciendo drásticamente la cantidad de datos redundantes enviados y mejorando la latencia.

4. **Server Push:**

   - Permite al servidor enviar recursos al cliente de forma proactiva, antes de que el cliente los solicite explícitamente. Por ejemplo, si un cliente pide una página HTML, el servidor puede "empujar" (push) los archivos CSS y JavaScript asociados inmediatamente, ya que sabe que el navegador los necesitará para renderizar la página. Esto reduce el número de viajes de ida y vuelta (round trips).

5. **Priorización de Flujos (Stream Prioritization):**
   - El cliente puede asignar una prioridad a diferentes flujos (streams) de datos, indicando al servidor qué recursos son más importantes. Por ejemplo, el navegador puede solicitar que se envíe el CSS crítico para el renderizado de la página antes que las imágenes de menor importancia.

## Ejercicio 20

¿Por qué HTTP es un protocolo sin estados (stateless)?

HTTP es un protocolo **sin estado (stateless)** porque el servidor web no guarda ninguna información o contexto sobre las solicitudes previas de un cliente. Cada solicitud que un cliente hace al servidor es tratada como una transacción completamente independiente y aislada.

Las características principales de este diseño son:

1. **Independencia de las Solicitudes:** El servidor no tiene memoria de las peticiones anteriores. Si haces una solicitud y un segundo después haces otra, el servidor no sabe que ambas provienen del mismo cliente o qué relación guardan entre sí.

2. **Solicitudes Autocontenidas:** Debido a que el servidor no recuerda nada, cada solicitud del cliente debe incluir toda la información necesaria para que el servidor pueda entenderla y procesarla por completo.

**¿Por qué fue diseñado así?**
La principal ventaja de ser un protocolo sin estado es la **simplicidad y la escalabilidad**.

- **Simplicidad:** Los servidores no necesitan destinar recursos (memoria, CPU) para mantener un seguimiento de las sesiones de cada cliente, lo que simplifica su diseño y operación.
- **Escalabilidad:** Facilita enormemente el balanceo de carga. Cualquier solicitud de un cliente puede ser dirigida a cualquier servidor en un clúster, ya que ningún servidor depende de un historial de interacciones previas. Si un servidor se cae, el cliente puede ser redirigido a otro sin perder el "estado de la sesión", porque tal estado no existe a nivel de protocolo.

**¿Cómo se gestiona el estado en las aplicaciones web?**
Aunque el protocolo HTTP es sin estado, las aplicaciones web modernas (como tiendas online, redes sociales, etc.) necesitan mantener un estado (por ejemplo, saber si un usuario ha iniciado sesión o qué tiene en su carrito de compras). Este problema se soluciona implementando mecanismos de gestión de estado **por encima de HTTP**, no dentro del protocolo en sí. Los más comunes son:

- **Cookies:** El servidor envía un pequeño archivo de texto (la cookie) al cliente. El navegador del cliente almacena esta cookie y la envía de vuelta al servidor con cada solicitud posterior. La cookie contiene un identificador único que permite al servidor reconocer al cliente y recuperar su información de sesión (que sí se guarda en el servidor, en una base de datos o en memoria).
- **Sesiones:** Es el mecanismo del lado del servidor que, usando el identificador de la cookie, asocia las solicitudes de un cliente a un conjunto de datos almacenados temporalmente.

## Ejercicio 21

Si una página web contiene un archivo base HTML y 4 imágenes. ¿Cuántas conexiones TCP son necesarias en HTTP 1.0 para obtener toda la página? ¿Y en HTTP 1.1?

La respuesta depende de las características de gestión de conexiones de cada versión del protocolo. En total, se deben descargar 5 recursos (1 HTML + 4 imágenes).

- **HTTP 1.0:**

  - Por diseño, HTTP 1.0 abre una nueva conexión TCP por cada recurso que necesita descargar. Después de que el recurso es transferido, la conexión se cierra.
  - Por lo tanto, se necesitarían **5 conexiones TCP** separadas: una para el archivo HTML y una para cada una de las 4 imágenes.

- **HTTP 1.1:**
  - HTTP 1.1 introduce las **conexiones persistentes (Keep-Alive)** por defecto. Esto permite reutilizar una única conexión TCP para múltiples solicitudes y respuestas.
  - El navegador abriría una conexión TCP para solicitar el archivo HTML. Una vez recibido, usaría esa misma conexión para solicitar las 4 imágenes.
  - Por lo tanto, en teoría, solo sería necesaria **1 conexión TCP** para obtener todos los recursos. (Nota: para mejorar el rendimiento, los navegadores modernos a menudo abren varias conexiones paralelas, típicamente hasta 6 por dominio, pero el protocolo en sí solo requiere una).

## Ejercicio 22

Explique las diferencias between los métodos GET, POST y PUT.

GET, POST y PUT son métodos de solicitud HTTP que indican la acción deseada a realizar sobre un recurso. Aunque todos transfieren datos, tienen propósitos semánticos distintos y se comportan de manera diferente.

### GET

- **Propósito:** Se utiliza para **solicitar y recuperar** datos de un recurso específico. Es una operación de solo lectura.
- **Envío de Datos:** Los datos se envían como parte de la URL, en la cadena de consulta (query string). Ejemplo: `http://example.com/users?id=123`.
- **Idempotente:** Sí. Realizar la misma solicitud GET múltiples veces debe producir el mismo resultado (el estado del servidor no cambia).
- **Seguridad (Safe):** Se considera un método seguro, ya que no debe tener efectos secundarios en el servidor.
- **Visibilidad y Límites:** Los datos son visibles en la URL, lo que los hace inseguros para información sensible. Además, la longitud de la URL es limitada.
- **Caché:** Las respuestas a las solicitudes GET pueden ser cacheadas por el navegador.
- **Uso Común:** Cargar una página web, buscar información, obtener datos de una API.

### POST

- **Propósito:** Se utiliza para **enviar datos para ser procesados** por un recurso específico. Generalmente resulta en la **creación de un nuevo recurso** subordinado al recurso de la URI.
- **Envío de Datos:** Los datos se envían en el **cuerpo (body)** de la solicitud HTTP, ocultos al usuario.
- **Idempotente:** No. Realizar la misma solicitud POST múltiples veces puede resultar en la creación de múltiples recursos nuevos.
- **Seguridad (Safe):** No es un método seguro, ya que modifica el estado del servidor (crea datos).
- **Visibilidad y Límites:** Los datos no son visibles en la URL. No hay límite en la cantidad de datos que se pueden enviar.
- **Caché:** Las respuestas a las solicitudes POST no se cachean.
- **Uso Común:** Enviar un formulario de registro, subir un archivo, publicar un comentario.

### PUT

- **Propósito:** Se utiliza para **actualizar un recurso existente o crear uno nuevo en una URI específica**. El cliente especifica la URI completa del recurso.
- **Envío de Datos:** Al igual que POST, los datos se envían en el **cuerpo (body)** de la solicitud.
- **Idempotente:** Sí. Realizar la misma solicitud PUT al mismo recurso múltiples veces tendrá el mismo efecto que hacerlo una sola vez: el recurso terminará en el mismo estado final.
- **Seguridad (Safe):** No es un método seguro, ya que modifica el estado del servidor (crea o reemplaza datos).
- **Visibilidad y Límites:** Los datos no son visibles en la URL. No hay límite en la cantidad de datos que se pueden enviar.
- **Caché:** Las respuestas a las solicitudes PUT no se cachean.
- **Uso Común:** Actualizar el perfil de un usuario, reemplazar un documento completo.

### Diferencia Clave entre POST y PUT

La diferencia fundamental es la **idempotencia** y el **control de la URI**:

- Usa **POST** cuando no sabes cuál será la URI del recurso que vas a crear. El servidor la asignará y te la devolverá en la respuesta. Ejemplo: `POST /users` (crea un nuevo usuario).
- Usa **PUT** cuando quieres crear o reemplazar un recurso en una URI que tú (el cliente) ya conoces y especificas. Ejemplo: `PUT /users/123` (actualiza o crea el usuario con el ID 123).

## Ejercicio 32

Suponga un cliente HTTP 1.0 se conecta a un servidor HTTP 1.1 y realiza las siguientes peticiones: <http://www.http11.com.ar/>, <http://www.http11.com.ar/index.html>, <http://www.http11.com.ar/home.html> dentro de un una ventana de tiempo de 1 minuto.

a) ¿Cuántas conexiones TCP se utilizarían si ninguna de las páginas contiene referencias a otros objetos?
b) ¿Cuántas conexiones TCP se utilizarán si home.html tiene los TAGs HTML: `<IMG SRC="dd.jpg">` y `<A HREF="otro.html">`
c) ¿Qué sucedería si el cliente y el servidor soportaran ambos HTTP 1.1 ?
d) Responda la misma pregunta que la anterior suponiendo que entre la primera y la segunda petición la máquina donde ejecuta el cliente se reinicia. (Justifique todas sus respuestas).

---

**Justificación General:** La comunicación entre un cliente y un servidor se rige por la versión más baja del protocolo que ambos soporten. En los casos a) y b), como el cliente es HTTP 1.0, la comunicación se realizará bajo las reglas de HTTP 1.0 (conexiones no persistentes).

**a) Sin objetos referenciados**

- Se utilizarían **3 conexiones TCP**.
- **Justificación:** El cliente HTTP 1.0 no utiliza conexiones persistentes por defecto. Por lo tanto, establece una nueva conexión TCP para cada una de las tres solicitudes (`/`, `/index.html`, `/home.html`) y la cierra al recibir la respuesta.

**b) Con objetos referenciados en `home.html`**

- Se utilizarían **4 conexiones TCP**.
- **Justificación:** Se realizan las 3 conexiones iniciales para los archivos HTML. Al procesar `home.html`, el navegador encuentra la etiqueta `<IMG>` y reconoce que debe descargar el recurso `dd.jpg`. Como es un cliente HTTP 1.0, abre una cuarta conexión TCP exclusivamente para descargar la imagen. La etiqueta `<A HREF>` es un hipervínculo y no genera una solicitud automática, por lo que no consume una conexión hasta que el usuario haga clic en él.

**c) Cliente y Servidor soportan HTTP 1.1**

- Se utilizaría **1 sola conexión TCP** para el escenario del punto b).
- **Justificación:** HTTP 1.1 utiliza conexiones persistentes (Keep-Alive) por defecto. El cliente establecería una única conexión TCP con el servidor y la reutilizaría para enviar las 4 solicitudes de recursos (`/`, `/index.html`, `/home.html` y `dd.jpg`) de forma consecutiva.

**d) Ambos son HTTP 1.1 pero el cliente se reinicia**

- Se utilizarían **2 conexiones TCP**.
- **Justificación:**
  1. **Conexión 1:** El cliente abre una primera conexión TCP para la solicitud inicial (`http://www.http11.com.ar/`).
  2. **Reinicio:** Al reiniciarse el cliente, todo el estado de la red se pierde. La conexión TCP que se había establecido (y que podría haber quedado abierta por ser persistente) se termina abruptamente.
  3. **Conexión 2:** Después del reinicio, para realizar la segunda petición (`/index.html`), el cliente debe establecer una nueva conexión TCP desde cero. Esta segunda conexión se reutilizaría para las peticiones subsiguientes (`/home.html` y `dd.jpg`) gracias a que es HTTP 1.1.

## Ejercicio 35

¿Qué protocolos se utilizan para el envío y la recepción de mails? ¿Qué protocolos de la capa de transporte utilizan y qué puertos?

Para el manejo de correos electrónicos se utiliza una combinación de protocolos, uno para el envío y otros para la recepción/lectura. Todos ellos utilizan **TCP (Transmission Control Protocol)** como protocolo de capa de transporte debido a que se requiere una entrega fiable y ordenada de los mensajes.

### Protocolo de Envío

- **SMTP (Simple Mail Transfer Protocol):** Es el protocolo estándar para el envío de correos electrónicos. Se utiliza para la transferencia de correo desde un cliente de correo a un servidor (sumisión) y entre servidores de correo (retransmisión o relay).
  - **Puerto 25:** Puerto tradicional para la comunicación entre servidores de correo.
  - **Puerto 587:** Puerto moderno y recomendado para la sumisión de correos desde un cliente a un servidor, utiliza encriptación STARTTLS.
  - **Puerto 465:** Puerto antiguo para SMTPS (SMTP sobre SSL/TLS), hoy en desuso pero todavía en uso por sistemas heredados.

### Protocolos de Recepción

Son los protocolos que utiliza un cliente de correo para descargar los mensajes desde el servidor.

- **POP3 (Post Office Protocol 3):** Es un protocolo simple diseñado para descargar los correos del servidor al dispositivo local. Generalmente, una vez descargados, los correos son eliminados del servidor.

  - **Puerto 110:** Puerto estándar para POP3 (sin cifrar).
  - **Puerto 995:** Puerto para POP3S (POP3 sobre SSL/TLS, cifrado).

- **IMAP (Internet Message Access Protocol):** Es un protocolo más avanzado que permite gestionar los correos directamente en el servidor. Los correos permanecen en el servidor y se pueden organizar en carpetas. El cliente sincroniza su estado con el servidor, lo que permite acceder al mismo buzón desde múltiples dispositivos de manera consistente.
  - **Puerto 143:** Puerto estándar para IMAP (sin cifrar).
  - **Puerto 993:** Puerto para IMAPS (IMAP sobre SSL/TLS, cifrado).

## Ejercicio 36

Cuáles son las diferencias entre SMTP y ESMTP?

**ESMTP (Extended Simple Mail Transfer Protocol)** no es un protocolo separado, sino una **extensión** del SMTP original. Fue diseñado para añadir funcionalidades que no existían en el SMTP básico, manteniendo la retrocompatibilidad. Hoy en día, prácticamente todos los servidores de correo modernos utilizan ESMTP.

La diferencia fundamental radica en cómo se inicia la comunicación y la capacidad de anunciar y utilizar nuevas características:

1. **Comando de Saludo (Handshake):**

   - **SMTP:** El cliente inicia la sesión con el comando `HELO`. El servidor responde con un simple saludo.
   - **ESMTP:** El cliente inicia la sesión con el comando `EHLO` (Extended Hello). Si el servidor soporta ESMTP, responde con un código de éxito y una lista de todas las extensiones (comandos y capacidades adicionales) que soporta. Si el servidor solo soporta el SMTP antiguo, tratará `EHLO` como un error y el cliente puede reintentar con `HELO`.

2. **Extensibilidad:**
   - **SMTP:** Es un protocolo rígido con un conjunto de comandos fijo.
   - **ESMTP:** Es extensible por diseño. Permite añadir nuevas funcionalidades de forma estandarizada sin romper la compatibilidad.

Algunas de las extensiones más importantes introducidas por ESMTP incluyen:

- **SMTP-AUTH:** Permite la autenticación del cliente antes de enviar un correo, lo cual es crucial para prevenir que los servidores sean usados como "open relays" para enviar spam.
- **STARTTLS:** Permite cifrar la comunicación entre el cliente y el servidor utilizando TLS (Transport Layer Security) sobre una conexión que inicialmente no era segura.
- **PIPELINING:** Permite al cliente enviar una secuencia de comandos sin tener que esperar la respuesta a cada uno, mejorando significativamente el rendimiento.
- **SIZE:** Permite al cliente declarar el tamaño del mensaje al servidor. Si el mensaje es demasiado grande para el servidor, este puede rechazarlo de inmediato sin necesidad de transferir todos los datos.
- **8BITMIME:** Permite el uso de caracteres de 8 bits en el cuerpo del mensaje, facilitando el envío de correos en idiomas que no usan el set de caracteres ASCII de 7 bits.

## Ejercicio 37

¿Cuáles son las diferencias entre POP (ver3), IMAP (ver4), POPS e IMAPS? ¿Cuál supone que utilizan gmail o hotmail?

La diferencia fundamental se divide en dos ejes: el **funcionamiento del protocolo (POP vs. IMAP)** y la **seguridad de la conexión (versiones estándar vs. versiones seguras)**.

### Diferencia de Funcionamiento: POP3 vs. IMAP

| Característica                | POP3 (Post Office Protocol 3)                                                                   | IMAP (Internet Message Access Protocol)                                                                       |
| ----------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Modelo**                    | "Descargar y borrar". Actúa como una oficina de correos: vas, recoges tu correo y te lo llevas. | "Sincronización". Actúa como un acceso remoto al buzón; los correos viven en el servidor.                     |
| **Almacenamiento**            | Los correos se mueven del servidor al dispositivo local. El servidor queda vacío (por defecto). | Los correos permanecen siempre en el servidor. El cliente solo descarga una copia o la visualiza.             |
| **Estado del Mensaje**        | El estado (leído, no leído) se gestiona localmente en el dispositivo.                           | El estado (leído, no leído, respondido) se mantiene en el servidor y se sincroniza en todos los dispositivos. |
| **Carpetas**                  | No soporta la gestión de carpetas en el servidor. Todo se descarga a la bandeja de entrada.     | Permite crear, eliminar y gestionar una estructura de carpetas directamente en el servidor.                   |
| **Uso Multi-dispositivo**     | Muy ineficiente. Si descargas un correo en tu PC, no estará disponible en tu teléfono.          | Ideal para múltiples dispositivos. Las acciones realizadas en un dispositivo se reflejan en todos los demás.  |
| **Consumo de Ancho de Banda** | Mayor al inicio (descarga todo), pero luego permite trabajar offline sin conexión.              | Menor en general (solo descarga cabeceras o lo necesario), pero requiere conexión constante para operar.      |

### Diferencia de Seguridad: POPS e IMAPS

Esta diferencia no es de funcionamiento, sino de **cifrado**.

- **POP3 e IMAP:** Por defecto, operan en texto plano. Las credenciales (usuario/contraseña) y el contenido de los correos viajan sin cifrar por la red, lo cual es muy inseguro.
- **POPS (POP3 Secure) e IMAPS (IMAP Secure):** Son los mismos protocolos, pero la comunicación se encapsula desde el inicio dentro de una capa de seguridad **SSL/TLS**. Esto cifra toda la sesión, protegiendo tanto las credenciales como los correos de ser interceptados.

En resumen:

- **POPS** es POP3 sobre SSL/TLS.
- **IMAPS** es IMAP sobre SSL/TLS.

### ¿Cuál utilizan Gmail o Hotmail (Outlook)?

Los servicios de correo modernos como **Gmail** y **Hotmail/Outlook** utilizan **IMAP** como método principal y recomendado.

**Justificación:** Su modelo de negocio se basa en que los usuarios puedan acceder a su correo de forma consistente desde múltiples plataformas (navegador web, aplicación móvil, cliente de escritorio, etc.). El único protocolo que permite esta sincronización perfecta de carpetas y estados de mensajes es IMAP.

Aunque también ofrecen acceso **POP3** como una opción de compatibilidad para clientes de correo más antiguos, el método por defecto y el que usan en sus propias aplicaciones es IMAP.

Además, por motivos de seguridad, ambos servicios exigen el uso de las versiones seguras de los protocolos, es decir, **IMAPS (puerto 993)** y **POPS (puerto 995)**. La conexión a los puertos no seguros (143 y 110) generalmente no está permitida.

## Ejercicio 39

¿Para qué sirve la extensión MIME?

La extensión MIME (Multipurpose Internet Mail Extensions) sirve para identificar el tipo de contenido de un mensaje o un archivo y así indicar cómo debe interpretable o procesarse. Se utiliza en correo electrónico y en HTTP mediante la cabecera `Content-Type`.

- Formato: `tipo/subtipo` (ej.: `text/html`, `image/png`, `application/json`).
- Permite que clientes y servidores manejen correctamente datos binarios, texto, imágenes, audio, vídeo, etc.
- En email, indica cómo decodificar y mostrar adjuntos; en HTTP, informa al navegador qué renderizador usar.
- Asocia tipos con extensiones de archivo y establece la codificación (p. ej. `charset=utf-8`).

## Ejercicio 41

Por qué FTP utiliza dos puertos?

FTP utiliza dos puertos porque utiliza canales separados para control y datos. El puerto de control (TCP 21) se usa para enviar comandos y respuestas; el canal de datos se utiliza exclusivamente para transferir archivos o listar directorios. En modo activo el servidor inicia la conexión de datos desde su puerto 20 hacia un puerto efímero del cliente. En modo pasivo el servidor escucha en un puerto efímero y el cliente se conecta a ese puerto. Esta separación facilita la gestión de la sesión y las transferencias, pero requiere consideraciones especiales con firewalls y NAT (por eso el modo pasivo se usa frecuentemente).

## Ejercicio 42

¿Cuáles son las diferencias entre FTP Activo y FTP Pasivo?

- Canal de control y datos: FTP usa dos conexiones TCP: control (puerto 21) para comandos y respuestas, y un canal de datos separado para transferir archivos o listas.
- FTP Activo:
  - El cliente abre conexión al puerto 21 del servidor y envía el comando PORT indicando un puerto efímero propio.
  - El servidor inicia la conexión de datos desde su puerto 20 hacia el puerto efímero del cliente.
  - Problema con NAT/firewalls: el servidor debe poder conectarse al cliente, lo que suele fallar si el cliente está detrás de NAT o un firewall restrictivo.
- FTP Pasivo:
  - El cliente abre la conexión al puerto 21 del servidor y solicita PASV.
  - El servidor responde con un puerto efímero en el que queda a la escucha para la conexión de datos.
  - El cliente inicia la conexión de datos hacia ese puerto del servidor.
  - Más compatible con NAT/firewalls porque el cliente siempre inicia ambas conexiones.
- Puertos: control siempre TCP 21; canal de datos en Activo suele usar fuente TCP 20 del servidor; en Pasivo usa puertos efímeros del servidor (>=1024).
- Seguridad y práctica: FTP transmite credenciales y datos en texto plano; para seguridad usar FTPS o SFTP. En la práctica, el modo pasivo es el más usado por compatibilidad con firewalls/NAT.

## Ejercicio 43

FTP cifra las sesiones? ¿Qué se podría utilizar para lograr esta funcionalidad?

No — FTP estándar transmite control (comandos/credenciales) y datos en texto plano, por lo que no cifra la sesión.

Opciones para cifrar/asegurar transferencias de archivos:

- FTPS (FTP sobre TLS/SSL)
  - Modo explícito: cliente envía `AUTH TLS` sobre puerto 21; recomendable.
  - Modo implícito: conexión TLS desde el inicio, puerto 990.
  - Nota: FTPS mantiene canales de control y datos separados; hay que configurar rangos de puertos de datos y ajustar firewalls/NAT.
- SFTP (SSH File Transfer Protocol)
  - Protocolo distinto que opera sobre SSH (puerto 22). Recomendado por simplicidad y compatibilidad con NAT/firewall.
- Alternativas: tunelizar FTP sobre SSH/VPN o usar HTTPS (WebDAV/HTTPS) según el caso.

Recomendación práctica: usar SFTP o FTPS (AUTH TLS) con certificados TLS válidos y configurar el servidor en modo pasivo con un rango de puertos fijo para facilitar el paso por firewalls.

