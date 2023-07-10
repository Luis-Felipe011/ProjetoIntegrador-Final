def classificar():
    import mysql.connector  # Importa o módulo mysql.connector para se conectar ao banco de dados MySQL

    mydb = mysql.connector.connect(
        host="us-cdbr-east-06.cleardb.net",  # Host do banco de dados
        user="b5390412538351",  # Usuário do banco de dados
        password="e827f4fc",  # Senha do banco de dados
        database="heroku_a8dd37572b9035f"  # Nome do banco de dados
    )

    cursor = mydb.cursor()  # Cria um objeto cursor para executar comandos SQL no banco de dados

    print("Classifque a qualidade do ar: ")

    # Consultas para obter a média dos valores das amostras de cada poluente
    consulta = 'select avg(MP10) from AMOSTRAS'
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    for linha in linhas:
        MP10 = float(linha[0])

    consulta = 'select avg(MP25) from AMOSTRAS'
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    for linha in linhas:
        MP25 = float(linha[0])

    consulta = 'select avg(O3) from AMOSTRAS'
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    for linha in linhas:
        O3 = float(linha[0])

    consulta = 'select avg(CO) from AMOSTRAS'
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    for linha in linhas:
        CO = float(linha[0])

    consulta = 'select avg(NO2) from AMOSTRAS'
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    for linha in linhas:
        NO2 = float(linha[0])

    consulta = 'select avg(SO2) from AMOSTRAS'
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    for linha in linhas:
        SO2 = float(linha[0])

    # Verifica a qualidade do ar com base nos valores médios dos poluentes
    if MP10 < 51 and MP25 < 26 and O3 < 101 and CO < 10 and NO2 < 201 and SO2 < 21:
        qualidade = "BOA."
        print("A qualidade do ar é", qualidade, "não há efeito à saúde.\n")
    
    elif MP10 <= 100 and MP25 <= 50 and O3 <= 130 and CO <= 11 and NO2 <= 240 and SO2 <= 40:
        qualidade = "MODERADA."
        print("A qualidade do ar é", qualidade,"\n")
        print("Os efeitos na saúde são:\n")
        print("Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.\n")
        
    elif MP10 <= 150 and MP25 <= 75 and O3 <= 160 and CO <= 13 and NO2 <= 320 and SO2 <= 365:
        qualidade = "RUIM."
        print("A qualidade do ar é", qualidade,"\n") 
        print("Os efeitos na saúde são:\n")
        print("Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.\n")
        
    elif MP10 <= 250 and MP25 <= 125 and O3 <= 200 and CO <= 15 and NO2 <= 1130 and SO2 <= 800:
        qualidade = "MUITO RUIM."
        print("A qualidade do ar é", qualidade,"\n")
        print("Os efeitos na saúde são:")
        print("Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).\n")
    
    elif MP10 > 250 or MP25 > 125 or O3 > 200 or CO > 15 or NO2 > 1130 or SO2 > 800:
        qualidade = "PÉSSIMA."
        print("A qualidade do ar é", qualidade,"\n")
        print("Os efeitos na saúde são:")
        print("Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis.\n")
    
    # Loop para continuar a classificação da qualidade do ar
    while True:
        respostas = input("Deseja continuar classificando a qualidade do ar (S/N)? ").upper()
        if respostas not in ["S", "N"]:
            print("É preciso digitar S ou N!")
        elif respostas in ["s", "S"]:
            classificar()  # Chama a função classificar() novamente para continuar a classificação
        else:
            if respostas in ["n", "N"]:
                print("Obrigado por usar esse programa!")
            break  # Sai do loop

