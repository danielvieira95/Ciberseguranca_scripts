import hashlib # biblioteca responsável por implementar a função hash dos diferentes tipos

def calcular_hash(texto):
    # Criar um objeto de hash MD5
    #hash_md5 = hashlib.md5() # realiza a implementação da função hash md5
    #has_sha256 =hashlib.sha256()
    has_sha512 =hashlib.sha512()
    # Atualizar o objeto de hash com o texto fornecido
   # hash_md5.update(texto.encode())
    has_sha512.update(texto.encode()) # criptografa o texto

    # Obter o valor de hash em hexadecimal
    return has_sha512.hexdigest() # retorna o conteúdo após a criptografia 

# Exemplo de uso
texto = "Olá, mundo!"
hash_resultado = calcular_hash(texto)
print("Hash do texto '{}':".format(texto))
print(hash_resultado)

