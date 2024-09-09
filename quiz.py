#inicio
resposta_certa = 0
print ("Bem vindo ao meu quiz!")
tema = int ( input ("Qual dos temas você gostaria de começar\n1) Brasil\n2) IFRN\n3) Volei\nreposta: "))
print ("_____________________________________________________________________________________")
if tema == 1:
    #tema brasil
    questoes = input ("Qual é a capital do Brasil?\na) Cidade das Rosas\nb) Rio de Janeiro\nc) Brasília\nd) Salvador\nreposta: ")
    if questoes == "c":
        resposta_certa += 1
        print ("vc acertou! Mas pra mim é meu Cidade das Rosas!")
    elif questoes == "a":
        print ("Seguindo as juridições, sua resposta estaria errada, mas pelo o autor desse quiz, sua resposta está TOTALMENTE CERTA, CDR É O MAIOR!!!!")
    elif questoes not in 'abcd':
        print('invalido')
    else:
        print ("vc errou!")

    print ("_____________________________________________________________________________________")

    questoes = input ("Em qual ano o Brasil se tornou independente de Portugal?\na) 1808\nb) 1822\nc) 1889\nd) 1900\nreposta: ")
    if questoes == "b":
        resposta_certa += 1
        print ("vc acertou!")
    elif questoes not in 'abcd':
        print('invalido')
    else:
        print ("vc errou!")

    print ("_____________________________________________________________________________________")

    questoes = input ("Qual é o maior bioma do Brasil em termos de área?\na) Caatinga\nb) Cerrado\nc) Pantanal\nd) Amazônia\nreposta: ")
    if questoes == "d":
        resposta_certa += 1
        print ("vc acertou!")
    elif questoes not in 'abcd':
        print('invalido')
    else:
        print ("vc errou!")
    
    questoes = input ("Qual é o nome do famoso carnaval realizado no Rio de Janeiro?\na) Carnaval das Flores\nb) Carnaval das Estações\nc) Carnaval do Samba\nd) Carnaval do Sol\nreposta: ")
    if questoes == "c":
        resposta_certa += 1
        print ("vc acertou!")
    elif questoes not in 'abcd':
        print('invalido')
    else:
        print ("vc errou!")

    print ("_____________________________________________________________________________________")

elif tema == 2:
    #tema ifrn

    questoes = input ("Qual é a principal função do IFRN?\na) Oferecer cursos de graduação e pós-graduação apenas\nb) Promover a educação básica, técnica, superior e tecnológica    \nc) Organizar eventos culturais e esportivos\nd) Oferecer apenas cursos de capacitação para empresas\nreposta: ")
    if questoes == "b":
        resposta_certa += 1
        print ("vc acertou!")
    elif questoes not in 'abcd':
        print('invalido')
    else:
        print ("vc errou!")

    questoes = input ("Em que ano foi fundado o IFRN?\na) 1909\nb) 1955\nc) 2008\nd) 1948\nreposta: ")
    if questoes == "c":
        resposta_certa += 1
        print ("vc acertou!")
    elif questoes not in 'abcd':
        print('invalido')
    else:
        print ("vc errou!")

    print ("_____________________________________________________________________________________")

    questoes = input ("Qual é a formação básica que os alunos do IFRN podem obter?\na) Apenas técnico\nb) Graduação em Engenharia e Medicina\nc) Técnico, graduação e pós-graduação\nd) Apenas pós-graduação em Tecnologia\nreposta: ")
    if questoes == "c":
        resposta_certa += 1
        print ("vc acertou!")
    elif questoes not in 'abcd':
        print('invalido')
    else:
        print ("vc errou!")

    print ("_____________________________________________________________________________________")

    questoes = input ("Qual é o principal objetivo da equipe de vôlei do IFRN?\na) Participar de campeonatos internacionais\nb) Promover a integração e prática esportiva\nc) Focar apenas em treinamentos individuais\nd) Realizar competições regionais\nreposta: ")
    if questoes == "b":
        resposta_certa += 1
        print ("vc acertou!")
    elif questoes not in 'abcd':
        print('invalido')
    else:
        print ("vc errou!")
    
    print ("_____________________________________________________________________________________")
    
elif tema == 3:
    #tema volei
        
    questoes = input ("Qual posição organiza as jogadas e distribui a bola no vôlei?\na) Levantador\nb) Central\nc) Oposto\nd) Líbero\nreposta: ")
    if questoes == "a":
        resposta_certa += 1
        print ("vc acertou!")
    elif questoes not in 'abcd':
        print('invalido')
    else:
        print ("vc errou!")

    print ("_____________________________________________________________________________________")

    questoes = input ("O que é a rotação no vôlei?\na) Técnica de passar a bola entre os jogadores\nb) Mudança de posição dos jogadores após o saque\nc) Movimento de girar o corpo para bloquear um ataque\nd) Distribuição das funções durante o jogo\nreposta: ")
    if questoes == "b":
        resposta_certa += 1
        print ("vc acertou!")
    elif questoes not in 'abcd':
        print('invalido')
    else:
        print ("vc errou!")

    print ("_____________________________________________________________________________________")

    questoes = input ("Qual é a principal característica de um levantamento no vôlei?\na) Feito com a mão aberta para precisão\nb) Ação defensiva para evitar que a bola toque no chão\nc) Técnica de ataque direto ao adversário\nd) Executado com uma única mão\nreposta: ")
    if questoes == "a":
        resposta_certa += 1
        print ("vc acertou!")
    elif questoes not in 'abcd':
        print('invalido')
    else:
        print ("vc errou!")
    
    print ("_____________________________________________________________________________________")

    questoes = input ("Quando um ace é obtido no vôlei?\na) No bloqueio\nb) No saque direto que não é tocado pelo adversário\nc) No levantamento\nd) No ataque\nreposta: ")
    if questoes == "b":
        resposta_certa += 1
        print ("vc acertou!")
    elif questoes not in 'abcd':
        print('invalido')
    else:
        print ("vc errou!")

else:
    print ("sua resposta está invalida")

resultado = (resposta_certa/4) * 100
print (f'A porcentagem dos seus acertos foi de: {resultado}%')