import os

# Função para aplicar configurações SSH
def apply_ssh_settings(settings):
    try:
        # Abrir o arquivo de configuração SSH para escrita
        with open('/etc/ssh/sshd_config', 'a') as ssh_config_file:
            for setting in settings:
                ssh_config_file.write(setting + '\n')

        # Reiniciar o serviço SSH para aplicar as configurações
        os.system('sudo systemctl restart ssh')

        print('Configurações do SSH aplicadas com sucesso.')

    except Exception as e:
        print('Erro ao aplicar as configurações:', str(e))

# Função para visualizar o arquivo de configuração SSH
def view_ssh_config():
    try:
        with open('/etc/ssh/sshd_config', 'r') as ssh_config_file:
            return ssh_config_file.read()

    except Exception as e:
        return f'Erro ao visualizar as configurações: {str(e)}'

# Função para configurar a lista de IPs
def configure_ip_list(ip_type):
    ip_list = []
    while True:
        ip = input(f'Digite um endereço IP para a lista de {ip_type} (ou "q" para sair): ')
        if ip.lower() == 'q':
            break
        ip_list.append(ip)
    
    return ip_list

# Função para iniciar o serviço SSH
def start_ssh_service():
    os.system('sudo systemctl start ssh')
    print('Serviço SSH iniciado.')

# Função para reiniciar o serviço SSH
def restart_ssh_service():
    os.system('sudo systemctl restart ssh')
    print('Serviço SSH reiniciado.')

# Função para parar o serviço SSH
def stop_ssh_service():
    os.system('sudo systemctl stop ssh')
    print('Serviço SSH parado.')

# Menu principal
while True:
    print("\nMenu Principal:")
    print("1. Configurar IP Whitelist")
    print("2. Mostrar Lista de IPs permitidos")
    print("3. Configurar IP Blacklist")
    print("4. Mostrar Lista de IPs não permitidos")
    print("5. Configurar Portas")
    print("6. Configurar Alertas")
    print("7. Configurar Logs de Acesso")
    print("8. Visualizar configurações SSH")
    print("9. Iniciar serviço SSH")
    print("10. Reiniciar serviço SSH")
    print("11. Parar serviço SSH")
    print("0. Sair do programa")

    choice = input("Escolha uma opção: ")

    if choice == '1':
        ip_whitelist = configure_ip_list("Whitelist")
        settings = [f"AllowUsers {','.join(ip_whitelist)}"]
        apply_ssh_settings(settings)

    elif choice == '2':
        print("Lista de IPs permitidos:")
        ssh_config = view_ssh_config()
        print("\n".join(line for line in ssh_config.split("\n") if "AllowUsers" in line))

    elif choice == '3':
        ip_blacklist = configure_ip_list("Blacklist")
        settings = [f"DenyUsers {','.join(ip_blacklist)}"]
        apply_ssh_settings(settings)

    elif choice == '4':
        print("Lista de IPs não permitidos:")
        ssh_config = view_ssh_config()
        print("\n".join(line for line in ssh_config.split("\n") if "DenyUsers" in line))

    elif choice == '5':
        port = input("Digite a porta desejada (ou 'q' para sair): ")
        if port.lower() != 'q':
            settings = [f"Port {port}"]
            apply_ssh_settings(settings)

    elif choice == '6':
        alerts = input("Digite uma configuração de alerta: ")
        settings = [f"# Alert: {alerts}"]
        apply_ssh_settings(settings)

    elif choice == '7':
        settings = ["LogLevel VERBOSE", "PrintLastLog yes"]
        apply_ssh_settings(settings)

    elif choice == '8':
        print("Configurações SSH:")
        ssh_config = view_ssh_config()
        print(ssh_config)

    elif choice == '9':
        start_ssh_service()

    elif choice == '10':
        restart_ssh_service()

    elif choice == '11':
        stop_ssh_service()

    elif choice == '0':
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
