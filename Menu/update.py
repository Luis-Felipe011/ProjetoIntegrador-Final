def update():
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
    print('Alterar amostras'.center(60))
    print("-=" * 40)
    print('\n')

    consulta = 'SELECT ID, MP10, MP25, O3, CO, NO2, SO2 FROM AMOSTRAS'  # Consulta para obter as amostras do banco de dados
    mycursor.execute(consulta)  # Executa a consulta
    linhas = mycursor.fetchall()  # Obtém todas as linhas de resultado

    if len(linhas) == 0:
        print('Não há amostras disponíveis para alterar.')
        return

    print('Amostras disponíveis para alteração:')
    for linha in linhas:
        print('ID:', linha[0])  # Exibe o ID da amostra
        print('MP10:', linha[1])  # Exibe o valor de MP10 da amostra
        print('MP25:', linha[2])  # Exibe o valor de MP25 da amostra
        print('O3:', linha[3])  # Exibe o valor de O3 da amostra
        print('CO:', linha[4])  # Exibe o valor de CO da amostra
        print('NO2:', linha[5])  # Exibe o valor de NO2 da amostra
        print('SO2:', linha[6])  # Exibe o valor de SO2 da amostra
        print('-' * 40)

    tipo = input('Digite o ID da amostra que você deseja alterar: ')  # Lê o ID da amostra que será alterada

    if not tipo.isdigit():
        print('ID inválido. Digite um valor numérico válido.')  # Exibe uma mensagem de erro se o ID inserido não for numérico

    sql = f"SELECT * FROM AMOSTRAS WHERE ID = {tipo}"  # Consulta para obter os dados da amostra selecionada
    mycursor.execute(sql)  # Executa a consulta
    result = mycursor.fetchone()  # Obtém a primeira linha de resultado

    if result is None:
        print('ID não encontrado. Digite um ID válido.')  # Exibe uma mensagem de erro se o ID não for encontrado no banco de dados

    while True:
        muda = int(input('Qual desses campos deseja alterar?: '))  # Lê a opção de campo que será alterado
        if muda >= 1 and muda <= 6:
            break
        else:
            print('Digite valores entre 1 e 6')
            print('Tente novamente!!')

    campos = ['MP10', 'MP25', 'O3', 'CO', 'NO2', 'SO2']  # Lista dos nomes dos campos
    muda = campos[muda - 1]  # Obtém o nome do campo correspondente à opção selecionada

    consulta = f'SELECT {muda} FROM AMOSTRAS WHERE ID = {tipo}'  # Consulta para obter o valor atual do campo selecionado
    mycursor.execute(consulta)  # Executa a consulta
    linhas = mycursor.fetchall()  # Obtém todas as linhas de resultado
    muda2 = str(linhas[0][0])  # Obtém o valor atual do campo

    novo = input('Digite o novo valor: ')  # Lê o novo valor que será atribuído ao campo
    sql = f"UPDATE AMOSTRAS SET {muda} = '{novo}' WHERE ID = {tipo}"  # Cria a declaração SQL para atualizar o campo com o novo valor
    try:
        mycursor.execute(sql)  # Executa o comando SQL para atualizar o campo
        mydb.commit()  # Confirma a transação
        mycursor.close()
        print('\n')
        print('Amostra alterada!')  # Exibe uma mensagem de sucesso se a amostra for alterada com sucesso
    except:
        print('Não foi possível alterar a amostra')  # Exibe uma mensagem de erro se ocorrer um erro ao alterar a amostra

        return
    else:
        print('\n')
        print('Erro ao alterar amostra!')  # Exibe uma mensagem de erro se ocorrer um erro ao alterar a amostra

    return

update()  # Chama a função `update` para iniciar o processo de alteração da amostra
