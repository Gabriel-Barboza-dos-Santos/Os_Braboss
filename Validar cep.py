Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
... 
... def validar_cep(cep):
...     # Formato de CEP: XXXXX-XXX ou XXXXXXXX (com ou sem hífen)
...     padrao_cep = r'^\d{5}-?\d{3}$'
...     
...     # Verificar se o CEP corresponde ao padrão
...     if re.match(padrao_cep, cep):
...         return True
...     else:
...         return False
... 
... # Exemplo de uso:
... cep = input("Digite um CEP: ")
... if validar_cep(cep):
...     print("CEP válido!")
... else:
...     print("CEP inválido.")
