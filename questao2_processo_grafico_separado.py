# -*- coding: utf-8 -*-

from threading import Thread, Semaphore
from multiprocessing import Queue
import time, os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import MaxNLocator


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

        package = os.popen("sudo tcpdump -i wlx8416f90dc4b1 -c 1 -v|grep proto").read()
        print(package)
        if package != "":
            pacote = package[package.index("proto"):].split(" ")[1] + " " + package[package.index("proto"):].split(" ")[4][:-2]
            print(pacote)
            if ("TCP" in pacote) or ("UDP" in pacote) or ("IGMP" in pacote):
                buffer.put(pacote)
                i+=1

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

        time.sleep(30)
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
        buffer2_3.put(int(media(tcp, "TCP")))
        buffer2_3.put(int(variancia(tcp, "TCP")))

        buffer2_3.put(int(len(udp)))
        buffer2_3.put(int(media(udp, "UDP")))
        buffer2_3.put(int(variancia(udp, "UDP")))

        buffer2_3.put(int(len(igmp)))
        buffer2_3.put(int(media(igmp, "IGMP")))
        buffer2_3.put(int(variancia(igmp, "IGMP")))
        semaphore.release()

def T3(buffer2_3, semaphore):

    fig = plt.figure()                 # tela onde joga o grafico
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)

    # legends= ["num. pacote TCP", "media pacote TCP", "variancia pacote TCP",              so pra saber a ordem como estao dispostos os valoers de b23
    #           "num. pacote UDP", "media pacote UDP", "variancia pacote UDP",
    #           "num. pacote IGMP", "media pacote IGMP", "variancia pacote IGMP"]

    time.sleep(30)

    y1 = [[0], [0], [0]]                                                                    # valores do eixo y1
    x1 = [[0], [0], [0]]                                                                    # valores do eixo x1
    y2 = [[0], [0], [0]]
    y3 = [[0], [0], [0]]



    def animate(i):                                                                         # i é padrao

        semaphore.acquire()                                                                 # exclusao mutua
        teste = []                                                                          # vetor que sera uado para substiruir b23

        while not buffer2_3.empty():                                                        # coloca os elementos do buffer num array
            teste.append(str(buffer2_3.get()))

        num = [teste[0], teste[3], teste[6]]
        media = [teste[1], teste[4], teste[7]]
        variancia = [teste[2], teste[5], teste[8]]

        print(teste)
        print(num)
        print(media)
        print(variancia)

        if len(teste) != 0:                         # testa se o array n está vazio

            for i in range(3):

                print("Tamanho x: ", len(x1[i]))
                print("Tamanho y: ", len(y1[i]))
                print("Tamanho buffer: ", len(teste))
                x1[i].append(len(x1[i]))
                y1[i].append(num[i])
                y2[i].append(media[i])
                y3[i].append(variancia[i])




        ax1.clear()
        ax2.clear()
        ax3.clear()

        for j in range(3):
            ax1.plot(x1[j], y1[j], marker="s")
            ax2.plot(x1[j], y2[j], marker="s")
            ax3.plot(x1[j], y3[j], marker="s")

        semaphore.release()

        ax1.legend(["num tcp", "num udp", "num igmp"], loc="upper right")
        ax1.set_xlabel("tempo")
        ax1.set_ylabel("Quantidade")

        ax2.legend(["media tcp", "media udp", "media igmp"], loc="upper right")
        ax2.set_xlabel("tempo")
        ax2.set_ylabel("Quantidade")

        ax3.legend(["var tcp", "var udp", "var igmp"], loc="upper right")
        ax3.set_xlabel("tempo")
        ax3.set_ylabel("Quantidade")

    anim = animation.FuncAnimation(fig, animate, interval=30000)
    plt.show()



def main():
    smf = Semaphore()

    p1 = os.fork()  # cria os forks
    if p1 == 0:  # se > 0, é filho
        T1(b12)  # cria processo filho1

    p2 = os.fork()
    if p2 == 0:  # se == 0, é filho
        T2(b12, b23, smf)  # cria processo filho 2

    p3 = os.fork()
    if p3 == 0:
        T3(b23, smf)

    os.waitpid(os.P_ALL, 0)
    os.popen("kill " + str(p1)).close()  # executa um kill no processo filho 1
    os.popen("kill " + str(p2)).close()  # executa um kill no processo filho 2
    os.popen("kill " + str(p3)).close()  # executa um kill no processo filho 3
    os.popen("kill " + str(os.getpid())).close()  # executa um kill no processo pai


if __name__ == '__main__':
    main()
