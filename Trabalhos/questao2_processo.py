# -*- coding: utf-8 -*-

from threading import Semaphore
from multiprocessing import Queue
import time, os
import matplotlib.pyplot as plt
import matplotlib.animation as animation


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



def T1(buffer, semaphore1):
    i=0
    while True:

        package = os.popen("sudo tcpdump -i any -c 1 -v|grep proto").read()
        print(package)
        if package != "":
            pacote = package[package.index("proto"):].split(" ")[1] + " " + package[package.index("proto"):].split(" ")[4][:-2]
            print(pacote)
            if ("TCP" in pacote) or ("UDP" in pacote) or ("IGMP" in pacote):
                semaphore1.acquire()
                buffer.put(pacote)
                semaphore1.release()
                i+=1

        print(i)



def T2(buffer1_2, buffer2_3, semaphore1, semaphore2):
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

        semaphore2.acquire()
        while not buffer2_3.empty():                            # esvazia o buffer
            buffer2_3.get()
        semaphore2.release()

        teste = []

        semaphore1.acquire()
        while not buffer1_2.empty():
            teste.append(buffer1_2.get())                       # passa os elementos do buffer para a lista
        semaphore1.release()

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

        semaphore2.acquire()
        buffer2_3.put(int(len(tcp)))
        buffer2_3.put(float(media(tcp, "TCP")))
        buffer2_3.put(float(variancia(tcp, "TCP")))

        buffer2_3.put(int(len(udp)))
        buffer2_3.put(float(media(udp, "UDP")))
        buffer2_3.put(float(variancia(udp, "UDP")))

        buffer2_3.put(int(len(igmp)))
        buffer2_3.put(float(media(igmp, "IGMP")))
        buffer2_3.put(float(variancia(igmp, "IGMP")))
        semaphore2.release()

def T3(buffer2_3, semaphore2):

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

        teste = []

        semaphore2.acquire()
        while not buffer2_3.empty():                # coloca os elementos do buffer num array
            teste.append(buffer2_3.get())
        semaphore2.release()

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


        plt.title("Grafico")
        plt.ylabel("Variáveis")
        plt.xlabel("")
        plt.legend(legends, loc="upper right")

    plt.tight_layout()
    anim = animation.FuncAnimation(fig, animate, interval=5000)
    plt.show()



def main():

    smf = Semaphore()
    smf2 = Semaphore()


    p1 = os.fork()  # cria os forks
    if p1 == 0:  # se > 0, é filho
        T1(b12, smf)  # cria processo filho1


    p2 = os.fork()
    if p2 == 0:                                                 # se == 0, é filho
        T2(b12, b23, smf, smf2)                                       # cria processo filho 2


    p3 = os.fork()
    if p3 == 0:
        T3(b23, smf2)

    os.waitpid(os.P_ALL, 0)
    os.popen("kill " + str(p1)).close()                         # executa um kill no processo filho 1
    os.popen("kill " + str(p2)).close()                         # executa um kill no processo filho 2
    os.popen("kill " + str(p3)).close()                         # executa um kill no processo filho 3
    os.popen("kill " + str(os.getpid())).close()                # executa um kill no processo pai


if __name__ == '__main__':
    main()