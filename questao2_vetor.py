# -*- coding: utf-8 -*-

from threading import Thread
from collections import deque
import time, copy, os
import matplotlib.pyplot as plt
import matplotlib.animation as animation


import numpy as np

# filho T1 é responsável por ler os pacotes da placa de rede, examinar quantos bytes
# tem o pacote e se o protocolo é TCP, UDP ou SMTP, e colocar as duas informações no buffer B12
#
# T2 é responsável por ler o buffer B12 e calcular o número, o tamanho médio e a variância dos
# pacotes UDP, TCP e SMTP a cada 30 s e colocar estas seis informações no buffer B23
#
# 3 é responsável por ler o buffer B23 e mostrar e atualizar a cada 30 s uma figura na tela
# com seis gráficos, mostrando a evolução de cada uma destas seis variáveis

b12 = []                  # vetor de string de 20 posicoes
b23 = []                  # vetor de inteiros de 9 posicoes



def T1(buffer):
    i=0
    while True:

        package = os.popen("sudo tcpdump -i any -c 1 -v|grep proto").read()
        print(package)
        if package != "":
            pacote = package[package.index("proto"):].split(" ")[1] + " " + package[package.index("proto"):].split(" ")[4][:-2]
            print(pacote)
            if ("TCP" in pacote) or ("UDP" in pacote) or ("IGMP" in pacote):
                buffer.append(pacote)
                i+=1

        print(i)



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
        return 0

    while True:

        time.sleep(5)

        while not (len(buffer2_3) == 0):
            buffer2_3.pop()


        print("tamanho b12: ",len(buffer1_2))
        teste=copy.copy(buffer1_2)

        while not (len(buffer1_2) == 0):
            buffer1_2.pop()
        print(teste)

        for i in teste:

            print(i)

            if "TCP" in i:
                print("Package Received: TCP")
                tcp.append(sum([int(x) for x in i.split(" ")[1:]]))

            if "UDP" in i:
                print("Package Received: UDP")
                udp.append(sum([int(x) for x in i.split(" ")[1:]]))

            if "IGMP" in i:
                print("Package Received: IGMP")
                igmp.append(sum([int(x) for x in i.split(" ")[1:]]))


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

        buffer2_3.append(int(len(tcp)))
        buffer2_3.append(float(media(tcp, "TCP")))
        buffer2_3.append(float(variancia(tcp, "TCP")))

        buffer2_3.append(int(len(udp)))
        buffer2_3.append(float(media(udp, "UDP")))
        buffer2_3.append(float(variancia(udp, "UDP")))

        buffer2_3.append(int(len(igmp)))
        buffer2_3.append(float(media(igmp, "IGMP")))
        buffer2_3.append(float(variancia(igmp, "IGMP")))

        print(buffer2_3)


def T3(buffer2_3):

    fig = plt.figure()                  # tela onde joga o grafico
    ax = fig.add_subplot(1,1,1)         #
    legends= ["num. pacote TCP", "media pacote TCP", "variancia pacote TCP",
              "num. pacote UDP", "media pacote UDP", "variancia pacote UDP",
              "num. pacote IGMP", "media pacote IGMP", "variancia pacote IGMP"]

    time.sleep(5)

    y = [[0], [0], [0], [0], [0], [0], [0], [0], [0]]
    x = [[0], [0], [0], [0], [0], [0], [0], [0], [0]]

    def animate(i):                   # i é padrao

        if len(buffer2_3) != 0:

            for i in range(9):
                print("Tamanho x: ", len(x[i]))
                print("Tamanho y: ", len(y[i]))
                print("Tamanho buffer: ", len(buffer2_3))
                y[i].append(buffer2_3[i])
                x[i].append(len(x[i]))
                print(y[i])
                print(x[i])

        ax.clear()
        for j in range(9):
            ax.plot(x[j], y[j], marker="s")

        plt.title("Grafico")
        plt.legend(legends)
    anim = animation.FuncAnimation(fig, animate, interval=5000)
    plt.show()

def main():
    t1 = Thread(target=T1, args=(b12,))
    t2 = Thread(target=T2, args=(b12, b23,))
    t3 = Thread(target=T3, args=(b23,))

    t1.start()
    t2.start()
    t3.start()


if __name__ == '__main__':
    main()