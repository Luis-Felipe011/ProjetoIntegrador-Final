
import classificar 
import adicionar 
import deletar
import update 

def Menu():
    while True:

        #apresentação das opções
        print('\n')
        print("-="*40)
        print('Menu Principal'.center(75))
        print("-="*40)
        print('\n')
        print("Escolha o numero de acordo com a ação que deseja fazer!".center(65))
        print('\n')
        print("1- Incluir amostra")
        print("2- Alterar amostra")
        print("3- Excluir amostra")
        print("4- Classificar o ar")
        print("5- Sair do Sistema\n")
        
        #entrada da escolha
        pick=input("Escolha a opção que deseja: ")
        print("="*217)
        print("\n")
        
        #resultado da Escolha
        if pick == "1":
            adicionar.adicionar()
        #escolha de numero 2 - alterar
        elif pick =="2":
            update.update()           
        #Escolha de numero 3 - excluir
        elif pick =="3":
            deletar.deletar()           
        #escolha de numero 4 - classificar
        elif pick =="4":
            classificar.classificar()
        #escolha de numero 5 - fechar o programa
        elif pick =="5":
            print("Obrigado por usar este programa!")
            break
        else:
            print('Digite um valor válido!')

Menu() 