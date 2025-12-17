Aquí tienes los ejercicios _multiple choice_ del Coloquio Integrador del 19/12/2013 en formato Markdown.

# Redes de Datos II - Coloquio Integrador – 19/12/2013

## Ejercicio 1

Una de las diferencias entre el formato de los paquetes de IPv4 y de IPv6 es que:

### A. IPv6 utiliza dos palabras de 32 bits para cada una de las direcciones IP origen y destino mientras que IPv4 sólo utiliza una para cada dirección

F

### B. IPv4 permite añadir opciones a la cabecera mientras que IPv6 no

F

### C. En IPv6 desaparece el campo del checksum que aparecía en la cabecera de IPv4

V

### D. Todas las respuestas anteriores son correctas

F

## Ejercicio 2

Dada la siguiente tabla ARP de un host perteneciente a la red 170.1.4.0/22, indicar cuáles de las entradas son incorrectas.

`C:\>arp -a`

|        | Dirección IP  | Dirección física  | Tipo     | Respuesta  |
| :----- | :------------ | :---------------- | :------- | :--------- |
| **a)** | 170.1.4.3     | 00-11-25-e9-73-85 | dinámico | Correcta   |
| **b)** | 170.1.5.255   | 00-11-25-ed-b5-95 | dinámico | correcta   |
| **c)** | 172.1.6.33    | 00-11-25-ea-b3-11 | dinámico | incorrecta   |
| **d)** | 170.1.7.255   | 00-11-25-58-4c-38 | dinámico | incorrecta |
| **e)** | 170.1.255.255 | 00-11-25-f9-d1-49 | dinámico | incorrecta |
| **f)** | 170.1.4.0     | 00-11-25-aa-9a-a2 | dinámico | incorrecta |
| **g)** | 170.1.4.1     | 00-11-25-1f-7c-d5 | dinámico | correcta   |
| **h)** | 228.1.2.3     | 00-11-25-cb-4a-f5 | dinámico | incorrecta |

## Ejercicio 4

Al encapsularse los mensajes de RIP en datagramas UDP:

### A. RIP no sufre de problemas de la fragmentación de datagramas IP

F

### B. RIP no sufre los problemas de descartado de paquetes por congestión en routers

F

### C. Los mensajes de RIP se desencapsulan por número de puerto del datagrama UDP

V

### D. Los mensajes de RIP se desencapsulan por número de protocolo en el datagrama IP

F

## Ejercicio 7

Estoy trabajando desde el ordenador de mi casa. Tengo contratado internet con un ISP cuyo DNS es dns.miisp.com. Intento conectarme desde mi casa al servidor de correo de la UNLP(post.unlp.edu.ar) cuya dirección está guardada en el servidor DNS de la universidad (oboe.info.unlp.edu.ar). ¿Quién le dará a mi ordenador la IP necesaria?

### A. oboe.info.unlp.edu.ar

F

### B. Dns.miisp.com

V

### C. post.unlp.edu.ar

F

### D. Uno de los dos servidores raíz: .ar ó .com

F

## Ejercicio 8

El servicio de DNS:

### A. Se encapsula directamente en IP dado su carácter auxiliar

F

### B. Se encapsula en UDP

F

### C. Se encapsula en TCP

F

### D. Se encapsula en TCP y/o UDP

V

