from threading import Thread
import subprocess, os, time

# import io
# from pdfminer.convert import TextConvert
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.pdfpage import PDFPage
#
# def ler_pdf(path):
#     imgFontes = PDFResourceManager()
#     binario = io.StringIO()
#     codec = "utf-8"
#
#     device = TextConvert(imgFontes, binario, codec = codec)
#
#     fp = open(path, "rb")
#
#     interpreter = PDFPageInterpreter(imgFontes, device)
#
#     for page in PDFPage.get_pages(fp):
#         interpreter.process_page(page)
#
#     aux = [word.lower() for word in binario.getvalue().split()]
#     print(aux)
#     fp.close()
#     device.close()
#     binario.close()

def busca(path):

    command = ("find {} -maxdepth 8 -type f -iname \"*.pdf\"").format(path)  # the shell command

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    result = out.decode("UTF-8").replace("\n", "\n").split("\n")
    lista = []
    while "" in result:
        result.remove("")
    for caminho in result:

        a = caminho.replace(" ", "\ ")      # formata o caminho para espacamentos
        file = caminho.split("/")[-1]       # nome do arquivo pdf
        print(caminho)
        # ler_pdf(caminho)
        print(file)
        os.popen(("pdftotext {} {}").format(a, a.replace(".pdf", ".txt")))
        time.sleep(.5)

        with open(str(caminho.replace(".pdf", ".txt"))) as file_text:
            palavras = []
            print("entrou with")
            for line in file_text:
                line = line.split(" ")
                for word in line:
                    palavras.append(word.strip("\n"))
        palavras = sorted(set(palavras))
        print("ordenado: ", palavras)
        lista.append((caminho, palavras))

    print("LISTA: ", lista)
    return lista

def busca_na_lista(word, list):

    resultado = []
    for i in range(len(list)):

        if word in list[i][0].split("/")[-1]:
            print(list[i][1])
            resultado.append(lista[i][1])

    return resultado


lista = busca("/home/gustavo/Desktop")

busca_na_lista("deepin", lista)