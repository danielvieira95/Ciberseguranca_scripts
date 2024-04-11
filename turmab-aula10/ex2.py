import requests

host = "http://globo.com"
metodos = ['OPTIONS', 'GET', 'POST', 'PUT', 'DELETE', 'TRACE', 'CONNECT'] # metodos para consumir uma api
# Get pega informações da api
#post posta informações no servidor
#put altera uma informaçao no servidor
# delete deleta uma informaçao no servidor

for metodo in metodos:
    try:
        # Utilize o método request() para fazer a solicitação HTTP
        resposta = requests.request(metodo, host)
        # Imprime o método e o código de status da resposta
        print(metodo, "->", resposta.status_code)
    except requests.exceptions.RequestException as e:
        # Em caso de erro na solicitação, imprime o método e a mensagem de erro
        print(metodo, "-> Erro:", e)
