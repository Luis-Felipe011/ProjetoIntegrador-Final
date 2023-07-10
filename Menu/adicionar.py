
def adicionar():
    import mysql.connector  # Importa o módulo mysql.connector para se conectar ao banco de dados MySQL

    mydb = mysql.connector.connect(
        host="us-cdbr-east-06.cleardb.net",  # Host do banco de dados
        user="b5390412538351",  # Usuário do banco de dados
        password="e827f4fc",  # Senha do banco de dados
        database="heroku_a8dd37572b9035f"  # Nome do banco de dados
    )

    mycursor = mydb.cursor()  # Cria um objeto cursor para executar comandos SQL no banco de dados

    print('\n')
    print("-="*40)
    print('inserir'.center(60))
    print("-="*40)
    print('\n')

    while True:
        try:
            MP10 = int(input('Digite a quantidade de partículas inaláveis: '))  # Lê a quantidade de partículas inaláveis como um número inteiro
            MP25 = int(input('Digite a quantidade de partículas inaláveis finas: '))  # Lê a quantidade de partículas inaláveis finas como um número inteiro
            O3 = int(input('Digite a quantidade de ozônio: '))  # Lê a quantidade de ozônio como um número inteiro
            CO = int(input('Digite a quantidade de monóxido de carbono: '))  # Lê a quantidade de monóxido de carbono como um número inteiro
            NO2 = int(input('Digite a quantidade de dióxido de nitrogênio: '))  # Lê a quantidade de dióxido de nitrogênio como um número inteiro
            SO2 = int(input('Digite a quantidade de dióxido de enxofre: '))  # Lê a quantidade de dióxido de enxofre como um número inteiro
        except:
            print('Digite valores numéricos! Tente novamente')  # Exibe uma mensagem de erro se os valores inseridos não forem numéricos
        else:
            if MP10 < 0 or MP25 < 0 or O3 < 0 or CO < 0 or NO2 < 0 or SO2 < 0:
                print('São aceitos apenas valores positivos')  # Verifica se os valores inseridos são negativos e exibe uma mensagem de erro se forem
            else:
                ParInaS = str(MP10)  # Converte o valor de MP10 em uma string
                ParInaFS = str(MP25)  # Converte o valor de MP25 em uma string
                OzonioS = str(O3)  # Converte o valor de O3 em uma string
                MonoCarbS = str(CO)  # Converte o valor de CO em uma string
                DioNitroS = str(NO2)  # Converte o valor de NO2 em uma string
                DioEnxS = str(SO2)  # Converte o valor de SO2 em uma string

                dados = ParInaS + ',' + ParInaFS + ',' + OzonioS + ',' + MonoCarbS + ',' + DioNitroS + ',' + DioEnxS + ')'  # Concatena as strings dos valores das amostras separadas por vírgulas
                declaracao = """INSERT INTO heroku_a8dd37572b9035f.amostras
                (ID, MP10, MP25, O3, CO, NO2, SO2)
                VALUES (default,"""  # Cria uma declaração SQL para inserir os valores no banco de dados
                sql = declaracao + dados  # Concatena a declaração SQL com os dados das amostras

                print('\n')
                try:
                    mycursor.execute(sql)  # Executa o comando SQL para inserir os dados no banco de dados
                    mydb.commit()  # Confirma a transação
                    mycursor.close()
                except:
                    print('Erro ao inserir no banco de dados')  # Exibe uma mensagem de erro se ocorrer um erro ao inserir os dados no banco de dados
                else:
                    print('Inserido com sucesso')  # Exibe uma mensagem de sucesso se os dados forem inseridos com êxito
                return
