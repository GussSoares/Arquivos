import os, time, math
from threading import Thread, Semaphore
from collections import deque
# Para instalar o matplotlib: sudo apt-get install python3-matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Para não precisar de senha com o uso do sudo
# No terminal digita sudo visudo, e altera #Allow membres of group sudo...
# Antes %sudo ALL=(ALL:ALL) ALL, depois %sudo ALL=(ALL:ALL)NOPASSWD:ALL
# Para salvar, ctrl+o e (não salve no arquivo .tmp. salvar em /etc/sudoers)
# Ctrl + x para sair

buffer12 = deque(maxlen=30)
buffer23 = deque(maxlen=9)

def thread1(buffer12, semaforo):
    while True:
        pacotes = os.popen("sudo tcpdump -i any -c 1 -v|grep proto").read()
        print(pacotes)
        if pacotes != "":
            dados = pacotes[pacotes.index("proto"):].split(" ")[1] + " " + pacotes[pacotes.index("proto"):].split(" ")[
                                                                               4][:-2]
            if ("TCP " in dados) or ("UDP" in dados) or ("SMTP" in dados):
                # print(dados)
                semaforo.acquire()
                buffer12.append(dados)
                semaforo.release()


# passa uma lista de pacotes como parametro e calcula a média
# sum() soma todos os numeros de uma lista
def medias(lista):
    if len(lista) > 0:
        return sum(lista) / len(lista)
    else:
        #   print("Nenhum pacote")
        return 0


# passa uma lista de pacotes e calcula a variância
# pow(num, expoente)
def variancias(lista):
    somatorio = 0
    media = medias(lista)
    if len(lista) > 0:
        for x in lista:
            somatorio += pow((x - media), 2)
        variancia = somatorio / float(len(lista))
        return variancia
    return 0


def thread2(buffer12, buffer23, semaforo, semaforo2):
    udp = []
    tcp = []  # vetor para guardar tam dos pacotes
    smtp = []

    print(buffer12)

    while True:
        time.sleep(5)

        while len(buffer23) != 0:
            semaforo2.acquire()
            buffer23.popleft()
            semaforo2.release()

        vetor_aux = []

        while len(buffer12) != 0:
            semaforo.acquire()
            vetor_aux.append(buffer12.popleft())
            semaforo.release()

        # Add apenas o tamanho do pacote em uma lista
        n = 0
        while n < len(vetor_aux):
            aux = vetor_aux[n]
            if "UDP" in aux:
                udp.append(sum([int(x) for x in aux.split(" ")[1:]]))
            elif "TCP" in aux:
                tcp.append(sum([int(x) for x in aux.split(" ")[1:]]))
            elif "SMTP" in aux:
                smtp.append(sum([int(x) for x in aux.split(" ")[1:]]))
            n += 1

        print("################################################")
        print("Pacotes UDP: ", udp)
        print("Pacotes TCP: ", tcp)
        print("Pacotes SMTP: ", smtp)
        print("Media UDP: ", medias(udp))
        print("Variancia UDP: ", variancias(udp))
        print("Media TCP: ", medias(tcp))
        print("Variancia TCP: ", variancias(tcp))
        print("Media SMTP: ", medias(smtp))
        print("Variancia SMTP: ", variancias(smtp))
        print("################################################")

        semaforo2.acquire()
        # Num. Media e variancia de UDP
        buffer23.append(int(len(udp)))
        buffer23.append(float(medias(udp)))
        buffer23.append(float(variancias(udp)))
        # Num. Media e variancia de TCP
        buffer23.append(int(len(tcp)))
        buffer23.append(float(medias(tcp)))
        buffer23.append(float(variancias(tcp)))
        # Num. Media e variancia de SMTP
        buffer23.append(int(len(smtp)))
        buffer23.append(float(medias(smtp)))
        buffer23.append(float(variancias(smtp)))

        semaforo2.release()
        print(buffer23)
        # Limpa vetor auxiliar
        vetor_aux.clear()


def thread3(buffer23, semaforo2):
    fig = plt.figure()

    ax1 = fig.add_subplot(221, axisbg='grey')
    ax2 = fig.add_subplot(222, axisbg='grey')
    ax3 = fig.add_subplot(223, axisbg='grey')

    time.sleep(5)

    y1 = [[0], [0], [0]]
    x1 = [[0], [0], [0]]
    y2 = [[0], [0], [0]]
    y3 = [[0], [0], [0]]

    def animate(i):

        teste = []

        print(buffer23)

        while len(buffer23) != 0:
            semaforo2.acquire()
            teste.append(str(buffer23.popleft()))  # Todo conteúdo de buffer está em teste
            semaforo2.release()

        num = [teste[0], teste[3], teste[6]]
        med = [teste[1], teste[4], teste[7]]
        var = [teste[2], teste[5], teste[8]]

        if len(teste) != 0:
            for i in range(3):
                x1[i].append(len(x1[i]))
                y1[i].append(num[i])
                y2[i].append(med[i])
                y3[i].append(var[i])

        ax1.clear()
        ax2.clear()
        ax3.clear()

        for j in range(3):
            ax1.plot(x1[j], y1[j], marker="^")
            ax2.plot(x1[j], y2[j], marker="o")
            ax3.plot(x1[j], y3[j], marker="p")

        ax1.legend(["num tcp", "num udp", "num smtp"], loc="upper left")
        ax1.set_xlabel("tempo")
        ax1.set_ylabel("Quantidade")

        ax2.legend(["media tcp", "media udp", "media smtp"], loc="upper left")
        ax2.set_xlabel("tempo")
        ax2.set_ylabel("Quantidade")

        ax3.legend(["var tcp", "var udp", "var smtp"], loc="upper left")
        ax3.set_xlabel("tempo")
        ax3.set_ylabel("Quantidade")

    anim = animation.FuncAnimation(fig, animate, interval=5000)
    plt.show()


if __name__ == "__main__":
    # Buffers (TESTE USANDO ARRAY)
    # buffer12 = Queue()
    # buffer23 = Queue()



    # semaforos
    smf = Semaphore()
    smf2 = Semaphore()

    print("==============================Antes de iniciar o thread 1==========================================")
    t1 = Thread(target=thread1, args=(buffer12, smf,))
    t1.start()

    time.sleep(20)
    print("===============================Antes de iniciar o thread 2=========================================")
    t2 = Thread(target=thread2, args=(buffer12, buffer23, smf, smf2,))
    t2.start()

    time.sleep(3)
    print("================================Antes de iiciar o thread 3==========================================")
    t3 = Thread(target=thread3, args=(buffer23, smf2,))
    t3.start()