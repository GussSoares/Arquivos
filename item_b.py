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
b23 = Queue()
def T1(buffer):
    i=0
    while i<5:
        package = os.popen("sudo tcpdump -i any -c 1 -v|grep proto").read()

        if package != "":
            pacote = package[package.index("proto"):].split(" ")[1] + " " + package[package.index("proto"):].split(" ")[4][:-2]
            print(pacote)
            buffer.put(pacote)
            i+=1

        print(i)

def T2(buffer1_2, buffer2_3):
    tcp=[]
    udp=[]

    def media(lista, nome):
        # print(lista, len(lista), "pacotes")
        if len(lista) > 0:
            # print("media do tamanho dos pacotes:", sum(lista)/len(lista))
            return sum(lista)/len(lista)
        else:
            print("Nenhum Pacote {}", nome)
            return -1

    def variancia(lista, nome):
        med = media(lista, nome)
        soma = 0
        variancia = 0
        if len(lista) > 0:

            for valor in lista:
                soma += pow((valor-med), 2)
            variancia = soma/float(len(lista))
            return variancia
        print("Nenhum Pacote {}", nome)
        return -1

    while not buffer1_2.empty() != False:
        teste=str(buffer1_2.get())

        if "TCP" in teste:
            print("Package Received: TCP")
            tcp.append(sum([int(x) for x in teste.split(" ")[1:]]))

        if "UDP" in teste:
            print("Package Received: UDP")
            udp.append(sum([int(x) for x in teste.split(" ")[1:]]))

    print("PACOTES TCP:",tcp)
    print("PACOTES UDP:",udp)
    print("media:", media(tcp, "TCP"))
    print("variancia:", variancia(tcp, "TCP"))
    print("media:", media(udp, "UDP"))
    print("variancia:", variancia(udp, "UDP"))

    def cria_informacoes(lista, nome):
        informacoes = []
        informacoes.append(int(len(lista)))
        informacoes.append(float(media(lista, nome)))
        informacoes.append(float(variancia(lista, nome)))

        return informacoes

    print(cria_informacoes(tcp, "TCP"))
    print(cria_informacoes(udp, "UDP"))


# p1=Process(target=T1, args=(b12,))
# p2=Process(target=T2, args=(b12,))
# #
# p1.start()
# p1.join()
# p2.start()
# p2.join()
T1(b12)
T2(b12, b23)
