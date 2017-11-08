import random, os
import threading, time
from multiprocessing import Queue, Semaphore, Lock
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def movimento_vetor(vetor):
	for i in range(len(vetor)-1):
		vetor[i] = vetor[i+1]

def principal(b12, tam, lock12, b23, lock23):

	def T1():

		i = 0

		while 1:

			lock12.acquire()

			aux = tam.get()
			tam.put(aux)


			if aux == 20:
				pass

			else:

				print("Aux: " + str(aux))

				if b12.empty() == True:
					i = 0

				pacote = os.popen("sudo tcpdump -i enp1s2 -c 1 -vv|grep proto").read()
				print(pacote)
				# p[1].split(" ")[2]
				# (p[0].split(" ")[2]
				print(len(pacote))
				if len(pacote) > 2:
					varS = pacote.split(",")[5:7][0].split(" ")[2] + " " + pacote.split(",")[5:7][1].split(" ")[2]
					if ")" in varS:
						varS = varS[:varS.index(")")]
					b12.put_nowait(varS)

				tam.put(tam.get() + 1)

				print("Entrou " + str(i))

				i += 1

			lock12.release()

	def T2():

		while 1:

			time.sleep(10)

			print("vai")

			lock12.acquire()

			i = 0

			print("Ok")

			# N pacotes, somatorio tamanho/ tamanho medio

			udp = [0,0]
			tcp = [0,0]
			smtp = [0,0]

			while b12.empty() != True:

				aux = b12.get_nowait()

				print(aux)

				i+=1

				if aux.split(" ")[0] == "TCP":
					tcp[0] += 1
					tcp[1] += int(aux.split(" ")[1])
				elif aux.split(" ")[0] == "UDP":
					udp[0] += 1
					udp[1] += int(aux.split(" ")[1])
				elif aux.split(" ")[0] == "SMTP":
					smtp[0] += 1
					smtp[1] += int(aux.split(" ")[1])

			# medias

			if tcp[0] != 0:					# caso nenhum pacote seja recebido
				tcp[1] = tcp[1]/tcp[0]
			if udp[0] != 0:
				udp[1] = udp[1]/udp[0]
			if smtp[0] != 0:
				smtp[1] = smtp[1]/smtp[0]

			# variancia

			media_pacotes = (tcp[0] + udp[0] + smtp[0])/3

			x_tcp = tcp[0] - media_pacotes
			x_udp = udp[0] - media_pacotes
			x_smtp = smtp[0] - media_pacotes

			x_tcp = x_tcp * x_tcp
			x_udp = x_udp * x_udp
			x_smtp = x_smtp * x_smtp

			total_quadrados = x_tcp + x_udp + x_smtp

			variancia = total_quadrados / (tcp[0] + udp[0] + smtp[0])

			print("Pacotes TCP: " + str(tcp[0]))
			print("Pacotes UDP: " + str(udp[0]))
			print("Pacotes SMTP: " + str(smtp[0]))
			print("Média do tamanho TCP: " + str(tcp[1]))
			print("Média do tamanho UDP: " + str(udp[1]))
			print("Média do tamanho SMTP: " + str(smtp[1]))
			print("Variancia: " + str(variancia))

			while tam.empty() != True:
				tam.get_nowait()
			tam.put(0)

			lock12.release()

			lock23.acquire()

			b23.put_nowait(tcp[0])
			b23.put_nowait(udp[0])
			b23.put_nowait(smtp[0])
			b23.put_nowait(tcp[1])
			b23.put_nowait(udp[1])
			b23.put_nowait(smtp[1])
			b23.put_nowait(variancia)

			lock23.release()

	def T3():

		def principal():

			def grafico():

				fig = plt.figure()
				ax1 = fig.add_subplot(1,1,1,axisbg='black')
				x = [[0],[0],[0],[0],[0],[0],[0]]
				y = [[0],[0],[0],[0],[0],[0],[0]]
				legendas = ["N.pac.TCP", "N.pac.UDP", "N.pac.SMTP", "T.pac.TCP", "T.pac.UDP", "T.pac.SMTP", "Variancia"]

				def animate(i):

					lock23.acquire()

					if b23.empty() != True:

						for i in range(7):
							y[i].append(b23.get_nowait())
							x[i].append(len(x[i]))


					ax1.clear()

					pontos = ['v','o','s','v','o','s','D']

					for j in range(7):
						ax1.plot(x[j],y[j], marker=pontos[j], linewidth = 2.0,  markersize = 17)

					plt.legend(legendas, loc='upper left', ncol=2, fontsize=13.0)
					plt.ylim(0, 250)
					plt.title("Então né")
					plt.ylabel("QTD")
					plt.xlabel("n - 30s")
					plt.grid(color='w', linestyle='--', linewidth=1)

					lock23.release()

				ani = animation.FuncAnimation(fig, animate, interval=1000)
				plt.show()

			th1 = threading.Thread(target=grafico)
			th1.start()

		principal()

	t1 = threading.Thread(target=T1)
	t2 = threading.Thread(target=T2)
	t3 = threading.Thread(target=T3)
	t1.start()
	t2.start()
	t3.start()

b12 = Queue()			# Fila -> buffer
tam = Queue()		# tamanho do buffer
tam.put(0)
lock12 = Semaphore()	# semaforo
b23 = Queue()
lock23 = Semaphore()
principal(b12, tam, lock12, b23, lock23)

# plt.scatter(XN_tcp , YN_tcp, linestyle='solid',  color='b', marker='o', linewidth=1.0, markersize=7)
# plt.scatter(XN_udp , YN_udp, linestyle='-',  color='g', marker='v', linewidth=1.0, markersize=7)
# plt.scatter(XN_smtp , YN_smtp, linestyle='--',  color='r', marker='+', linewidth=1.0, markersize=7)
# plt.scatter(XT_tcp , YT_tcp, linestyle='dashed',  color='c', marker='p', linewidth=1.0, markersize=7)
# plt.scatter(XT_udp , YT_udp, linestyle='dashdot',  color='m', marker='x', linewidth=1.0, markersize=7)
# plt.scatter(XT_smtp , YT_smtp, linestyle='dotted',  color='y', marker='*', linewidth=1.0, markersize=7)
# plt.scatter(XVarc , YVarc, linestyle='--',  color='k', marker='D', linewidth=1.0, markersize=7)
