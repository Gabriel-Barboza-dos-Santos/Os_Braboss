

def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

comprimento_senha = 15
senha_gerada = gerar_senha(comprimento_senha)
print("Sua senha gerada:", senha_gerada)

