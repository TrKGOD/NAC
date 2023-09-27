import socket
import datetime

# Dicionário para armazenar a whitelist de IPs e MAC Addresses
whitelist = {}

# Dicionário para armazenar o registro de tentativas por IP
connection_attempts = {}

# Conjunto para armazenar IPs bloqueados
blocked_ips = set()

# Dicionário para armazenar o redirecionamento de portas
port_forwarding = {}

# Função para registrar tentativa de conexão
def log_connection_attempt(ip):
    if ip in connection_attempts:
        connection_attempts[ip] += 1
    else:
        connection_attempts[ip] = 1

# Função para verificar se um IP deve ser bloqueado
def should_block_ip(ip):
    if ip in connection_attempts and connection_attempts[ip] >= 5:
        return True
    return False

# Função para adicionar IPs e MAC Addresses à whitelist
def add_to_whitelist(ip, mac):
    whitelist[ip] = mac

# Função para visualizar os logs de tentativas de conexão
def view_connection_logs():
    for ip, attempts in connection_attempts.items():
        print(f"IP: {ip}, Tentativas: {attempts}")

# Função para visualizar IPs bloqueados
def view_blocked_ips():
    for ip in blocked_ips:
        print(f"IP Bloqueado: {ip}")

# Função para desbloquear um IP
def unblock_ip(ip):
    if ip in blocked_ips:
        blocked_ips.remove(ip)
        print(f"IP {ip} desbloqueado com sucesso.")

# Função para configurar o redirecionamento de portas
def configure_port_forwarding(ip, source_port, dest_port):
    port_forwarding[(ip, source_port)] = dest_port
    print(f"Porta {source_port} redirecionada para {ip}:{dest_port}.")

# Função para gerar um alerta de exemplo
def generate_example_alert():
    example_ip = "192.168.1.100"
    example_mac = "00:1A:2B:3C:4D:5E"
    
    current_time = datetime.datetime.now()
    
    print("Alerta de Exemplo:")
    print(f"Horário: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"IP: {example_ip}")
    print(f"MAC Address: {example_mac}")
    
    log_connection_attempt(example_ip)  # Registrar tentativa fictícia
    blocked_ips.add(example_ip)  # Bloquear o IP de exemplo
    print(f"Tentativa de Conexão: {connection_attempts[example_ip]}")
    print(f"IP Bloqueado: {example_ip}")

# Registrar uma tentativa de login falha com um IP bloqueado por padrão
default_ip = "192.168.1.200"
log_connection_attempt(default_ip)
blocked_ips.add(default_ip)

# Menu principal
while True:
    print("\nMenu Principal:")
    print("-" * 20)
    print("1. Adicionar IP/MAC à whitelist")
    print("2. Visualizar IPs na whitelist")
    print("3. Visualizar logs de tentativas de conexão")
    print("4. Visualizar IPs bloqueados")
    print("5. Desbloquear um IP")
    print("6. Configurar Port Forwarding")
    print("7. Alertas")
    print("8. Sair")
    print("-" * 20)

    choice = input("Escolha uma opção: ")

    if choice == '1':
        ip = input("Digite o IP: ")
        mac = input("Digite o MAC Address: ")
        add_to_whitelist(ip, mac)
        print(f"IP {ip} e MAC {mac} adicionados à whitelist.")

    elif choice == '2':
        print("\nIPs na Whitelist:")
        for ip, mac in whitelist.items():
            print(f"IP: {ip}, MAC: {mac}")

    elif choice == '3':
        view_connection_logs()

    elif choice == '4':
        view_blocked_ips()

    elif choice == '5':
        ip_to_unblock = input("Digite o IP a ser desbloqueado: ")
        unblock_ip(ip_to_unblock)

    elif choice == '6':
        ip = input("Digite o IP de destino: ")
        source_port = input("Digite a porta de origem: ")
        dest_port = input("Digite a porta de destino: ")
        configure_port_forwarding(ip, int(source_port), int(dest_port))

    elif choice == '7':
        generate_example_alert()

    elif choice == '8':
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
