import psutil
import cpuinfo
import socket
nomeCPU = cpuinfo.get_cpu_info()['brand']  # Não sei porque roda o programa 2 vezes...
saiu = False

def processador():

    print("\n========================= CPU =========================")
    print("Processador: ", nomeCPU)
    print("Porcentagem de uso: ", psutil.cpu_percent(interval=1),"%")
    print("Frequência Máxima: ", round(psutil.cpu_freq().max/1000, 1), "GHz")
    print("Núcleos(Lógicos): ",psutil.cpu_count(logical=False),"(",psutil.cpu_count(),")")
    print("=======================================================")

def memoria():
    mem = psutil.virtual_memory()
    capacidade = round(mem.total/(1024*1024*1024), 2)
    print("\n========= MEMÓRIA RAM: =========")
    print("Capacidade total de ", capacidade, "GB")
    print("Memória Usada: ", round(mem.used / (1024 * 1024 * 1024), 2), "GB")
    print("Memória Livre: ", round(mem.free/(1024*1024*1024), 2), "GB")
    print("Uso de memória: ", mem.percent, "%")
    print("================================")

def hd():
    disco = psutil.disk_usage('.')
    print("\n=========== HD =============")
    print("Total:", round(disco.total / (1024 * 1024 * 1024), 2), "GB")
    print("Em uso:", round(disco.used / (1024 * 1024 * 1024), 2), "GB")
    print("Livre:", round(disco.free / (1024 * 1024 * 1024), 2), "GB")
    print("Total de uso:", disco.percent, "%")
    print("============================")

def rede():
    network = psutil.net_io_counters()
    hostname = socket.gethostname()
    # ip = psutil.net_connections()
    print("\n====================== REDE ======================")
    print("Endereço Interno: ", socket.gethostbyaddr(hostname)[0])
    print("IP: ", socket.gethostbyname(hostname))
    print("Pacotes enviados: ", network.packets_sent)
    print("Pacotes recebidos: ", network.packets_recv)
    print("Bytes enviados: ", round(network.bytes_sent / (1024 * 1024 * 1024), 2), "GB")
    print("Bytes rcebidos: ", round(network.bytes_recv / (1024 * 1024 * 1024), 2), "GB")
    print("==================================================")

while True:

    print("============= MENU =============")
    print("1. Informações do Processador")
    print("2. Informações da Memória RAM")
    print("3. Informações do Disco")
    print("4. Informações da Rede")
    print("5. Resumo de Todos")
    print("6. SAIR")
    print("================================")
    escolha = int(input("Opção: "))
    print("================================")

    if escolha == 1:
        processador()
        print("\n")
    elif escolha == 2:
        memoria()
        print("\n")
    elif escolha == 3:
        hd()
        print("\n")
    elif escolha == 4:
        rede()
        print("\n")
    elif escolha == 5:
        processador()
        memoria()
        hd()
        rede()
        print("\n")
    elif escolha == 6:
        saiu = True
        break
    else:
        print("Opção inválida!")
        print("FIM DO PROGRAMA")

if saiu == True:
    print("FIM DO PROGRAMAAAAAAAAAAAAAAAAAAAAAAAAAA")