
import random

def main():
#atributos avantureiro
    deff_aventureiro = random.randint(1,5)
    ataque_aventureiro= random.randint(10,20)
    vida_do_aventureiro = 100

#monstro
    vida_monstro = random.randint(60,80)
    ataque_monstro = random.randint(20,30)

    print ("Aventureiro: vida ",vida_do_aventureiro,"- att ",ataque_aventureiro,"- def ",deff_aventureiro)
    print("Mostro: vida ",vida_monstro,"-att", ataque_monstro)
    rodada = 0
    while True:
        rodada += 1 
        print("Rodada ",rodada)
        dano_aventureiro = random.randint(1,ataque_aventureiro)
        vida_monstro = vida_monstro - dano_aventureiro
        if vida_monstro <= 0 :
            print("MONSTRO MORREU")
            break
        dano_monstro = random.randint(1,ataque_monstro)
        if dano_monstro > deff_aventureiro:
            vida_do_aventureiro = vida_do_aventureiro - (dano_monstro - deff_aventureiro)
        if vida_do_aventureiro <= 0:
            ("AVENTUREIRO MORREU")
            break
        print ("Aventureiro: vida ",vida_do_aventureiro,"- att ",ataque_aventureiro,"- def ",deff_aventureiro)
        print("Mostro: vida ",vida_monstro,"-att", ataque_monstro)




main()







