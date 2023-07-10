def deletar():
    import mysql.connector  # Importa o módulo mysql.connector para se conectar ao banco de dados MySQL

    mydb = mysql.connector.connect(
        host="us-cdbr-east-06.cleardb.net",  # Host do banco de dados
        user="b5390412538351",  # Usuário do banco de dados
        password="e827f4fc",  # Senha do banco de dados
        database="heroku_a8dd37572b9035f"  # Nome do banco de dados
    )

    mycursor = mydb.cursor()  # Cria um objeto cursor para executar comandos SQL no banco de dados
    print('\n')
    print("-=" * 40)
    print('Deletar amostras'.center(75))  # Imprime um cabeçalho indicando que a função é para deletar amostras
    print("-=" * 40)
    print('\n')

    consulta = 'SELECT ID, MP10, MP25, O3, CO, NO2, SO2 FROM AMOSTRAS'  # Consulta SQL para selecionar os registros da tabela AMOSTRAS
    mycursor.execute(consulta)  # Executa a consulta SQL
    linhas = mycursor.fetchall()  # Recupera todas as linhas retornadas pela consulta

    if len(linhas) == 0:  # Verifica se não há amostras disponíveis para exclusão
        print('Não há amostras disponíveis para exclusão.')
        return

    for linha in linhas:  # Itera sobre as linhas retornadas e imprime os valores de cada campo para cada registro
        print('ID =', linha[0])
        print('MP10 =', linha[1])
        print('MP25 =', linha[2])
        print('O3 =', linha[3])
        print('CO =', linha[4])
        print('NO2 =', linha[5])
        print('SO2 =', linha[6])
        print('-' * 40)

    excluir = input('Qual o ID da amostra que deseja excluir: ')  # Solicita ao usuário o ID da amostra a ser excluída

    ids_disponiveis = [linha[0] for linha in linhas]  # Cria uma lista com os IDs disponíveis nas linhas retornadas

    if excluir not in ids_disponiveis:  # Verifica se o ID fornecido pelo usuário não está na lista de IDs disponíveis
        print("\n")
        print('ID incorreto. Por favor, digite um ID válido.')
        mycursor.close()  # Fecha o objeto cursor
        return

    sql = 'DELETE FROM AMOSTRAS WHERE ID = %s'  # Consulta SQL para excluir o registro com o ID fornecido
    try:
        mycursor.execute(sql, (excluir,))  # Executa a consulta de exclusão, passando o valor do ID como parâmetro
        mydb.commit()  # Confirma a exclusão no banco de dados
        print('\n')
        print('Sucesso!! Registro excluído.')
    except:
        print('Não foi possível excluir esse registro')

    mycursor.close()  # Fecha o objeto cursor
