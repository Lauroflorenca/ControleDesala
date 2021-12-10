def defineCinema(ln, cl):

    cinema = []
    linhatt = []

    for x in range(0, ln):
        linhatt = []
        for y in range(0, cl):
            linhatt.append( "vazio" )
        cinema.append( linhatt )

    return cinema


def exibeMenu():
    menu = "\n1 - Nova reserva. \n4 - Finalizar."
    
    return menu


def exibeLugares():

    lugares = ""
    for x in range(0, linha):
        lugares += "\n"
        for y in range(0, coluna):
            lugares += "["+str((x+1))+" "+str((y+1))+"]->"+str(cinemaArray[x][y])+" | "
    return lugares

#verifica se o lugar existe
def verifcaLugar(flU, clU):
    if flU > -1 and flU < linha and clU > -1 and clU < coluna:
        return True
    else:
        return False



linha = 20
coluna = 15

# atribui o retorno da funcao (array solicitado) na variavel 
cinemaArray = defineCinema(linha, coluna)


print(exibeMenu())
opcaoMenu = 0

while opcaoMenu != 4 :
    opcaoMenu = int(input("\nEscolha uma opcao: "))
    if opcaoMenu == 1:
        
        print("Escolha um lugar: ") 
        print(exibeLugares())
        print("\n")

        flUser = int(input("Informe o numero da Fileira (fl): "))
        clUser = int(input("Informe o numero da poltrona (cl): "))
        flUser = flUser - 1
        clUser = clUser - 1
        nome = str(input("Informe seu nome: "))
        print("\n")

        rtVf = verifcaLugar(flUser, clUser)
        print(rtVf)
        if  rtVf :

            if cinemaArray[flUser][clUser] == "vazio":

                cinemaArray[flUser][clUser] = nome
                print("\n -------------------------------------------------------- \n")
                print("Seu lugar foi reservado com sucesso!!\n")
                print("\n -------------------------------------------------------- \n")
                print(exibeLugares())
            else:
                print("\n -------------------------------------------------------- \n")
                print("Esse lugar ja foi reservado!!\n")
                print("\n -------------------------------------------------------- \n")
        else:
            print("\n -------------------------------------------------------- \n")
            print("Posicao invalida!!!")
            print("\n -------------------------------------------------------- \n")



    print(exibeMenu())
     
       
print("\n")
print("Até + ^-^ Obrigado !!")