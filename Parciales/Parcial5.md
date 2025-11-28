# Parcial 5

## Ejercicio 1

Ruteo dinamico

## Ejercicio 2

- El servicio de DNS se encuentra almacenado en una base de datos centralizada. F
- Un servidor autoritativo es donde se almacena y modifica toda la información de DNS de un dominio.F
- Al hacer uso de una caché nos aseguramos que siempre vamos a recibir la respuesta correcta.F
- Utiliza UDP para realizar consultas y TCP para la transferencia de zonas.F (Puede ser V porque normalmente usa UDP)
- Una deficiencia de DNS es que solo se puede tener un solo servidor de nombre por dominio.F

## Ejercicio 3

Ruteo Dinamico

## Ejercicio 4

Ruteo Dinamico

## Ejercicio 5

### A

Esta utilizando el protocolo HTTPS, cuyo puerto default es el 443 de TCP

### B

<www.redes.unlp.edu.ar>

Se solicita el recurso /test

### C

304 Not Modified, no le devuelve nada

### D

Al ser http version 1.1, la conexion se mantiene activa hasta que se cierre la pagina. Por ende, no podemos garantizar que la conexion se haya cerrado, Deberia haber una cabezera que diga connection:close

## Ejercicio 6

- El cliente utiliza POP a IMAP para enviar y recibir mails. F
- MIME es una extension que permite el envío de distintos tipos de adjuntos en un mail. V
- El cliente de mail del usuario consultará por los registros MX de su dominio para enviar los mails a su servidor de mail. F
- SMTP funciona sobre TCP, en cambio POP lo hace sobre UDP. F
- Todas las opciones son verdaderas. F

## Ejercicio 7

Esto ocurre porque la PC A esta ejecutando FTP en modo pasivo, en el cual el canal de datos se pasa por un canal efimero de ambos extremos, mientras que en la PC B esta en modo activo, por lo que el canal de datos esta en el puerto 20, por lo que no puede llegar a la PC B

