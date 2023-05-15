import mysql.connector
# Conectando ao banco de dados
config = {
  'user': 'admin',
  'password': 'aulanoiteFaculdade',
  'host': 'database.crhtgzzmysft.us-east-1.rds.amazonaws.com',
  'database': 'brasil'
}

# Estabelecer a conexão com o banco de dados
try:
    conn = mysql.connector.connect(**config)
    print("Conexão executada com sucesso.")
except mysql.connector.Error as err:
    print(f"Conexão falhou: {err}")

while True:
    # Menu de opções
    print("Selecione uma opção:")
    print("1 - Cadastrar tribo")
    print("2 - Editar tribo")
    print("3 - Consultar tribo")
    print("4 - Deletar tribo")
    print('0 - Sair')

    # Obter a escolha do usuário
    opcao = input("Opção: ")


    # Definir as funções
    def cadastrar_tribo():
        # Obter informações da tribo a ser cadastrada
        nome = input("Nome: ")
        num_habitantes = input("Número de habitantes: ")
        renda_media_mes = input("Renda média mensal: ")
        escolaridade = input("Escolaridade (fundamental/médio/superior): ")
        trabalho_assalariado = input("Possui trabalho assalariado (s/n): ")

        # Executar consulta SQL para cadastrar a tribo
        cursor = conn.cursor()
        query = "INSERT INTO tribos_nativas (nome, num_habitantes, renda_media_mes, escolaridade, trabalho_assalariado) VALUES (%s, %s, %s, %s, %s)"
        values = (nome, num_habitantes, renda_media_mes, escolaridade, trabalho_assalariado)
        cursor.execute(query, values)

        # Commit para salvar as alterações no banco de dados
        conn.commit()

        # Obter o ID da tribo recém-cadastrada
        id_tribo = cursor.lastrowid

        # Informar ao usuário que a tribo foi cadastrada com sucesso
        print(f"Tribp cadastrada com sucesso! ID da tribo: {id_tribo}")
    
    def editar_tribo():
        # Obter informações da tribo a ser editada
        id_tribo = input("ID da tribo a ser editada: ")
        nome = input("Nome: ")
        num_habitantes = input("Número de habitantes: ")
        renda_media_mes = input("Renda média mensal: ")
        escolaridade = input("Escolaridade (fundamental/médio/superior): ")
        trabalho_assalariado = input("Possui trabalho assalariado (s/n): ")

        # Executar consulta SQL para editar a tribo
        cursor = conn.cursor()
        query = "UPDATE tribos_nativas SET nome = %s, num_habitantes = %s, renda_media_mes = %s, escolaridade = %s, trabalho_assalariado = %s WHERE id_tribo = %s"
        values = (nome, num_habitantes, renda_media_mes, escolaridade, trabalho_assalariado, id_tribo)
        cursor.execute(query, values)

        # Commit para salvar as alterações no banco de dados
        conn.commit()

        # Informar ao usuário que a tribo foi editada com sucesso
        print("Tribo editada com sucesso!")
    def consultar_tribos():
        # Executar consulta SQL para obter todas as tribos cadastradas
        cursor = conn.cursor()
        query = "SELECT * FROM tribos_nativas"
        cursor.execute(query)

        # Exibir os resultados da consulta
        result = cursor.fetchall()
        for tribo in result:
            print(tribo)

    def deletar_tribo():
        # Obter o ID da tribo a ser deletada
        id_tribo = input("ID da tribo a ser deletada: ")

        # Executar consulta SQL para deletar a tribo
        cursor = conn.cursor()
        query = "DELETE FROM tribos WHERE id_tribo = %s"
        values = (id_tribo,)
        cursor.execute(query, values)

        # Commit para salvar as alterações no banco de dados
        conn.commit()

        # Verificar se a tribo foi deletada com sucesso
        if cursor.rowcount == 1:
            print("Tribo deletada com sucesso!")
        else:
            print("Tribo não encontrada.")

# Executar código correspondente à escolha do usuário
    if opcao == "1":
        cadastrar_tribo()
    elif opcao == "2":
        editar_tribo()
    elif opcao == "3":
        consultar_tribos()
    elif opcao == "4":
        deletar_tribo()
    elif opcao == '0':
        print("Programa encerrado.")
    break
else:
    print('Opção inválida!')

# Fechar a conexão com o banco de dados
conn.close()