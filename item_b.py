import os
from multiprocessing import *
from queue import Queue
import time
# filho T1 é responsável por ler os pacotes da placa de rede, examinar quantos bytes
# tem o pacote e se o protocolo é TCP, UDP ou SMTP, e colocar as duas informações no buffer B12
#
# T2 é responsável por ler o buffer B12 e calcular o número, o tamanho médio e a variância dos
# pacotes UDP, TCP e SMTP a cada 30 s e colocar estas seis informações no buffer B23
#
# 3 é responsável por ler o buffer B23 e mostrar e atualizar a cada 30 s uma figura na tela
# com seis gráficos, mostrando a evolução de cada uma destas seis variáveis



b12 = Queue()
def T1(buffer):
    package = os.popen("sudo tcpdump -i any -c 1 -v|grep proto").read()

    # if package != "":
    if package != "":
        pacote = package[package.index("proto"):].split(" ")[1] + " " + package[package.index("proto"):].split(" ")[4][:-2]
        print(pacote)
        buffer.put(pacote)
        # print(buffer.get())
    else:
        T1(buffer)

def T2(buffer):
    print("entrou")
    teste=buffer.get()

    if "TCP" in str(teste):
        print("tcp")
    buffer.put(teste)
    teste2=buffer.get()
    if "UDP" in str(teste2):
        print("udp")

# p1=Process(target=T1, args=(b12,))
# p2=Process(target=T2, args=(b12,))
# #
# p1.start()
# p1.join()
# p2.start()
# p2.join()
T1(b12)
T2(b12)
