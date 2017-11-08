import os
# from multiprocessing import Queue
from queue import Queue

# filho T1 é responsável por ler os pacotes da placa de rede, examinar quantos bytes
# tem o pacote e se o protocolo é TCP, UDP ou SMTP, e colocar as duas informações no buffer B12

# T2 é responsável por ler o buffer B12 e calcular o número, o tamanho médio e a variância dos
# pacotes UDP, TCP e SMTP a cada 30 s e colocar estas seis informações no buffer B23

# 3 é responsável por ler o buffer B23 e mostrar e atualizar a cada 30 s uma figura na tela
# com seis gráficos, mostrando a evolução de cada uma destas seis variáveis

def T1():
    package = os.popen("sudo tcpdump -i any -c 1 -v|grep proto").read()
    if package != "":
        pacote = package[package.index("proto"):].split(" ")[1] + " " + package[package.index("proto"):].split(" ")[4][:-2]
        print(pacote+"kb")
        b12 = Queue()
        b12.put(pacote)
        # print()

T1()
