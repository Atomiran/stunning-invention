



#contatos = [
   # "João Silva <joao.silva@email.com>",
    #"Maria Oliveira <maria.oliveira@email.com>",
    #"Carlos Souza <carlos.souza@email.com>",
    #"Ana Costa <ana.costa@email.com>"
#]


#for contato in contatos:
    #nome, email = contato.split(" <")
    #nome = nome.strip()         # Agora sim: nome existe e pode ser limpo
    #email = email.strip(">")
    #print(f"Nome: {nome} | Email: {email}")

  

contatos = [
    "João Silva <joao.silva@email.com>",
    "Maria Oliveira <maria.oliveira@email.com>",
    "Carlos Souza <carlos.souza@email.com>",
    "Ana Costa <ana.costa@email.com>"
]

lista_formatada = []

for contato in contatos:
    nome, email = contato.split(" <")
    nome = nome.strip()
    email = email.strip(">")
    
    # Criando o dicionário e adicionando à lista
    lista_formatada.append({
        "nome": nome,
        "email": email
    })

# Exibindo a lista de dicionários
for item in lista_formatada:
    print(item)

