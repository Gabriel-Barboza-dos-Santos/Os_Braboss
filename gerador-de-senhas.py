from funcoes import *
from interface import *

cabecalho("GERADOR DE SENHAS")

quant = quant_senhas()
tam = tam_senhas()

senhas = gerador_senhas(quant, tam)

cabecalho("SAINDO...")
