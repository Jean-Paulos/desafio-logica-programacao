import random

print("Olá, novo Herói! Bem-vindo à nossa guilda.")
escolha = input("Deseja se registrar? (sim/não): ")

if escolha == "sim" or escolha == "Sim":
    nome = input("Ótimo! Seu nome, por favor?: ")
    print("Bem-vindo,", nome + "!")
    print("Nossa guilda classifica os Heróis pelo XP. Quanto mais XP, maior o seu rank.\nUse está esfera de cristal para medir seu XP.")
    print("A esfera está brilhando! ela vai mostrar o seu XP agora!")
    xp = random.randint(1, 10001)
    if xp >= 1 and xp <= 1000:
        print(f"{nome}, o seu nível de XP é {xp} e seu rank é bronze.\nParece que você tem muito chão pela frente.")
    elif xp >=1001 and xp <= 2000:
        print(f"Hmm {nome}, seu nível de XP é {xp} e seu rank é ferro.\nContinue assim.")
    elif xp >= 2001 and xp <= 5000:
        print(f"Parabéns {nome}, seu nível de XP é {xp} e seu rank é prata!\nIsso é mpressionante para um novato!")
    elif xp >= 5001 and xp <= 6000:
        print(f"Uau! {nome}, seu nível de XP é {xp}! Você já é um rank Ouro! \nSerá que você é algum veterano disfarçado?")
    elif xp >= 6001 and xp <= 8000:
        print(f"Pelos Deuses! {nome}, o seu nível é {xp}!! Você é rank Platina Diamante!\nÉ a primeira vez que vejo um rank tão alto!")
    elif xp >= 8001 and xp <= 9000:
        print(f"O seu poder é de 7000... espera, agora é de 8000 e continua aumentando! ...O SEU XP É DE MAIS DE 8000 *QUEBRA O APARELHO*")
        print(f"*atendente está pálido e mudo, mas você consegue ver o número {xp} na esfera rachada, o que equivale ao rank Ascendente!")
    elif xp >= 9001 and xp <= 1000:
      print(f"{xp}?! R-rank I-i-mortal?! *desmaia* ")
    elif xp >= 10001:
        print(f"Hm? {xp}? ?  .... humanos podem chegar nesse número de XP? Isso é um nível além dos imortais das lendas!")
        print(f"Parabéns Herói! Você é Rank Radiante, infelizmente esse é o máximo. Você chegou ao topo!")
elif escolha == "não" or escolha == "Não":
    print("Claro, nos procure quando quiser.")
else:
    print("Desculpe, não entendi sua escolha.")