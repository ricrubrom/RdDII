import math

def fragment_ipv4(total_data, ip_header, mtu, df):
    """
    total_data: tamaño total de los datos a enviar (bytes)
    ip_header: tamaño del header IPv4 (bytes)
    mtu: MTU del enlace de salida (bytes)
    df: Don’t Fragment bit (True o False)
    """
    link_overhead = 18  # overhead del link layer

    max_payload = mtu - ip_header - link_overhead

    if df and total_data + ip_header > mtu - link_overhead:
        print("El datagrama no puede fragmentarse. ICMP 'Fragmentation Needed' enviado.")
        return

    # Calcular número de fragmentos
    num_fragments = math.ceil(total_data / max_payload)

    print(f"Número de fragmentos: {num_fragments}\n")
    
    remaining_data = total_data
    for i in range(1, num_fragments + 1):
        if remaining_data >= max_payload:
            data_size = max_payload
        else:
            data_size = remaining_data
        total_size = data_size + ip_header + link_overhead
        print(f"Fragmento {i}:")
        print(f"  Datos: {data_size} bytes")
        print(f"  IPv4 header: {ip_header} bytes")
        print(f"  Link layer overhead: {link_overhead} bytes")
        print(f"  Tamaño total transmitido: {total_size} bytes\n")
        remaining_data -= data_size

# Ejemplo de uso
fragment_ipv4(total_data=1000, ip_header=20, mtu=400, df=False)

