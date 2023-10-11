import re

def validar_cep(cep):
  # Formato de CEP: XXXXX-XXX ou XXXXXXXX (com ou sem hífen)
    padrao_cep = r'^\d{5}-?\d{3}$'
    
     # Verificar se o CEP corresponde ao padrão
    if re.match(padrao_cep, cep):
        return True
    else:
        return False

 # Exemplo de uso:
cep = '0100801033'
if validar_cep(cep):
    print("CEP válido!")
else:
     print("CEP inválido.")
