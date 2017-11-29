# -*- coding: utf-8 -*-

from threading import Thread, Semaphore
from multiprocessing import Queue
import time, os
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

b12 = Queue()                  # vetor de string de 20 posicoes
b23 = Queue()                  # vetor de inteiros de 9 posicoes



def T1(buffer):
    i=0
    while True:
        # semaphore.acquire()
        package = os.popen("sudo tcpdump -i wlx8416f90dc4b1 -c 1 -v|grep proto").read()
        print(package)
        if package != "":
            pacote = package[package.index("proto"):].split(" ")[1] + " " + package[package.index("proto"):].split(" ")[4][:-2]
            print(pacote)
            if ("TCP" in pacote) or ("UDP" in pacote) or ("IGMP" in pacote):
                buffer.put(pacote)
                i+=1
        # semaphore.release()
        print(i)



def T2(buffer1_2, buffer2_3, semaphore):
    tcp=[]
    udp=[]
    igmp=[]
    i=0

    def media(lista, nome):
        if len(lista) > 0:
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
        semaphore.acquire()
        while not buffer2_3.empty():                            # esvazia o buffer
            buffer2_3.get()

        teste = []
        while not buffer1_2.empty():
            teste.append(buffer1_2.get())                       # passa os elementos do buffer para a lista
        semaphore.release()

        for i in teste:                                         # usa a lista para verificar os pacotes

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

        semaphore.acquire()
        buffer2_3.put(int(len(tcp)))
        buffer2_3.put(float(media(tcp, "TCP")))
        buffer2_3.put(float(variancia(tcp, "TCP")))

        buffer2_3.put(int(len(udp)))
        buffer2_3.put(float(media(udp, "UDP")))
        buffer2_3.put(float(variancia(udp, "UDP")))

        buffer2_3.put(int(len(igmp)))
        buffer2_3.put(float(media(igmp, "IGMP")))
        buffer2_3.put(float(variancia(igmp, "IGMP")))
        semaphore.release()

def T3(buffer2_3, semaphore):

    fig = plt.figure()                  # tela onde joga o grafico
    # ax = fig.add_subplot(1,1,1)
    ax1 = fig.add_subplot(111)


    legends= ["num. pacote TCP", "media pacote TCP", "variancia pacote TCP",
              "num. pacote UDP", "media pacote UDP", "variancia pacote UDP",
              "num. pacote IGMP", "media pacote IGMP", "variancia pacote IGMP"]

    time.sleep(5)

    y1 = [[0], [0], [0], [0], [0], [0], [0], [0], [0]]
    x1 = [[0], [0], [0], [0], [0], [0], [0], [0], [0]]


    def animate(i):                     # i é padrao
        semaphore.acquire()
        teste = []
        while not buffer2_3.empty():                # coloca os elementos do buffer num array
            teste.append(buffer2_3.get())

        if len(teste) != 0:                         # testa se o array n está vazio

            for i in range(9):
                print("Tamanho x: ", len(x1[i]))
                print("Tamanho y: ", len(y1[i]))
                print("Tamanho buffer: ", len(teste))
                y1[i].append(teste[i])
                x1[i].append(len(x1[i]))

        ax1.clear()

        for j in range(9):
            ax1.plot(x1[j], y1[j], marker="s")

        semaphore.release()

        plt.title("Grafico")
        plt.ylabel("Variáveis")
        plt.legend(legends, loc="upper right")
    anim = animation.FuncAnimation(fig, animate, interval=5000)
    plt.show()



def main():
    smf = Semaphore()

    t1 = Thread(target=T1, args=(b12,))
    t2 = Thread(target=T2, args=(b12, b23, smf,))
    t3 = Thread(target=T3, args=(b23, smf,))



    t1.start()
    t2.start()
    t3.start()


if __name__ == '__main__':
    main()