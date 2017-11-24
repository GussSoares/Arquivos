# -*- coding: utf-8 -*-

import os
# from multiprocessing import *
import time
from queue import Queue
from threading import Thread
import time, datetime
import matplotlib.pyplot as plt
import numpy as np

# filho T1 é responsável por ler os pacotes da placa de rede, examinar quantos bytes
# tem o pacote e se o protocolo é TCP, UDP ou SMTP, e colocar as duas informações no buffer B12
#
# T2 é responsável por ler o buffer B12 e calcular o número, o tamanho médio e a variância dos
# pacotes UDP, TCP e SMTP a cada 30 s e colocar estas seis informações no buffer B23
#
# 3 é responsável por ler o buffer B23 e mostrar e atualizar a cada 30 s uma figura na tela
# com seis gráficos, mostrando a evolução de cada uma destas seis variáveis

b12 = []
b23 = []

def T1(buffer):
    i=0
    while True:
    # while not buffer.full():
        package = os.popen("sudo tcpdump -i enp1s2 -c 1 -v|grep proto").read()
        print(package)
        if package != "":
            pacote = package[package.index("proto"):].split(" ")[1] + " " + package[package.index("proto"):].split(" ")[4][:-2]
            print(pacote)
            if ("TCP" in pacote) or ("UDP" in pacote) or ("IGMP" in pacote):
                buffer.append(pacote)
                i+=1

        print(i)
        # i = 0



def T2(buffer1_2, buffer2_3):
    tcp=[]
    udp=[]
    igmp=[]
    i=0

    def media(lista, nome):
        # print(lista, len(lista), "pacotes")
        if len(lista) > 0:
            # print("media do tamanho dos pacotes:", sum(lista)/len(lista))
            return sum(lista)/len(lista)
        else:
            # print("Nenhum Pacote {}".format(nome))
            return 0

    def variancia(lista, nome):
        med = media(lista, nome)
        soma = 0
        variancia = 0
        if len(lista) > 0:
            for valor in lista:
                soma += pow((valor-med), 2)
            variancia = soma/float(len(lista))
            return variancia
        # print("Nenhum Pacote {}".format(nome))
        return 0

    while i != len(buffer1_2):
        teste=str(buffer1_2[i])

        if "TCP" in teste:
            print("Package Received: TCP")
            tcp.append(sum([int(x) for x in teste.split(" ")[1:]]))

        if "UDP" in teste:
            print("Package Received: UDP")
            udp.append(sum([int(x) for x in teste.split(" ")[1:]]))

        if "IGMP" in teste:
            print("Package Received: IGMP")
            igmp.append(sum([int(x) for x in teste.split(" ")[1:]]))
        i+=1

    print("============================================")
    print("PACOTES TCP:",tcp)
    print("PACOTES UDP:",udp)
    print("PACOTE IGMP:",igmp)
    print("media TCP:", media(tcp, "TCP"))
    print("variancia TCP:", variancia(tcp, "TCP"))
    print("media UDP:", media(udp, "UDP"))
    print("variancia UDP:", variancia(udp, "UDP"))
    print("media IGMP:", media(igmp, "IGMP"))
    print("variancia IGMP:", variancia(igmp, "IGMP"))
    print("============================================")

    def cria_informacoes(lista, nome):
        informacoes = []
        informacoes.append(nome)
        informacoes.append(int(len(lista)))
        informacoes.append(float(media(lista, nome)))
        informacoes.append(float(variancia(lista, nome)))

        return informacoes

    # print(cria_informacoes(tcp, "TCP"))
    # print(cria_informacoes(udp, "UDP"))

    buffer2_3.append(cria_informacoes(tcp, "TCP"))
    buffer2_3.append(cria_informacoes(udp, "UDP"))
    buffer2_3.append(cria_informacoes(igmp, "IGMP"))
    print(len(buffer2_3))
    print(buffer2_3)
    # print(buffer2_3.qsize())

    while not (len(buffer1_2) == 0):
        buffer1_2.pop()
    # del tcp[:]
    # del udp[:]


def T3(buffer2_3):
    index=0
    time=5
    while True:
        # x_inicial_tcp_num = buffer2_3[index][1]
        # x_inicial_tcp_med = buffer2_3[index][2]
        # x_inicial_tcp_var = buffer2_3[index][3]

        # tcp_num = np.linspace(x_inicial_tcp_num, 2, 100)
        plt.scatter(time, buffer2_3[index][1])
        plt.scatter(time, buffer2_3[index+1][1])
        plt.scatter(time, buffer2_3[index+2][1])

        plt.plot(time, buffer2_3[index][1])
        plt.plot(time, buffer2_3[index + 1][1])
        plt.plot(time, buffer2_3[index + 2][1])
        # plt.plot(x, x, label='num')
        # plt.plot(x, x ** 2, label='media')
        # plt.plot(x, x ** 3, label='variancia')

        plt.xlabel('x label')
        plt.ylabel('y label')

        plt.title("Simple Plot")

        plt.legend()

        plt.show()
        plt.pause(0.0001)
        index += 3
        time+=5
        # time.sleep(5)


        # lista1 = str(buffer2_3.get())
        # print(lista1)

t1 = Thread(target=T1, args=(b12,))

t1.start()

y=0

while True:
    time.sleep(5-y)
    x = time.time()

    t2 = Thread(target=T2, args=(b12, b23,))
    t3 = Thread(target=T3, args=(b23,))

    if (not t2.is_alive()):
        t2.start()
        t2.join()

    t3.start()
    t3.join()

    y = time.time() - x
