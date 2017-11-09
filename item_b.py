import os
# from multiprocessing import *
import time
from queue import Queue
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
    i=0
    while i<5:
        package = os.popen("sudo tcpdump -i any -c 1 -v|grep proto").read()

        if package != "":
            pacote = package[package.index("proto"):].split(" ")[1] + " " + package[package.index("proto"):].split(" ")[4][:-2]
            print(pacote)
            buffer.put(pacote)
            # print(buffer.get())
        i+=1

        print(i)
        # print(package)
def T2(buffer):
    tcp=[]
    udp=[]
    while not buffer.empty() != False:
        # print(len(buffer))
        # print("entrou")
        teste=buffer.get()
        # buffer.put(teste)
        if "TCP" in str(teste):
            print("Package Received: TCP")
            tcp.append(teste)


        if "UDP" in str(teste):
            print("Package Received: UDP")
            udp.append(teste)

    print(tcp)
    print(udp)

# p1=Process(target=T1, args=(b12,))
# p2=Process(target=T2, args=(b12,))
# #
# p1.start()
# p1.join()
# p2.start()
# p2.join()
T1(b12)
T2(b12)
