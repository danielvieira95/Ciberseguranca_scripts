import requests # biblioteca que permite a aquisição de dados via url

resposta = requests.head("https://www.globo.com/") #1 # armazena na variavel resposta o resultado
for cabecalho, conteudo in resposta.headers.items(): #2
    print(cabecalho, ":", conteudo)

