from ninja import Ninja
from Jinchuuriki import Jinchuuriki
from cenario import Cenario
from madara import Madara
from kaguya import Kaguya
import random
import time

def do_damage(ninja_atual, ninjas_list):
    for ninja in ninjas_list:
        if ninja_atual != ninja:
            dano = ninja_atual.get_dano_base()  # Usando o getter
            ninja.do_damage(dano)
            print(f"{ninja_atual.nome} causou dano em: {ninja.nome}")

def steal_chakra(ninja_atual, ninjas_list):
    for ninja in ninjas_list:
        if ninja_atual != ninja:
            dano = ninja_atual.get_dano_base()  # Usando o getter
            ninja.steal_chakra(dano)
            print(f"{ninja_atual.nome} causou dano em: {ninja.nome}")

def configure_game(ninjas_list):
    print("Você inicializou o jogo: 'Mate o Madara (é serio essa guerra tem mais episódio do que deveria)'")
    print("Primeiro vamos escolher seu ninja!")
    print("Seu ninja é um jinchuuriki? \n1.Sim \n2.Não")

    jin_bool = int(input())
    if jin_bool == 1:
        print(f"Nome: ")
        nome = input("")
        print(f"Aldeia: ")
        aldeia = input("")
        print(f"Nível Shinobi: ")
        nivel_shinobi = input("")
        print(f"Número Inicial de Shurikens: ")
        num_shuriken = int(input())
        print(f"Número de Caudas (Escreva em numeral, ex: 1,2,3): ")
        num_caudas = int(input())
        ninja_player = Jinchuuriki(nome, aldeia, nivel_shinobi, num_shuriken, num_caudas, do_damage, steal_chakra)
    else:
        print(f"Nome: ")
        nome = input("")
        print(f"Aldeia: ")
        aldeia = input("")
        print(f"Nível Shinobi: ")
        nivel_shinobi = input("")
        print(f"Número Inicial de Shurikens: ")
        num_shuriken = int(input())
        ninja_player = Ninja(nome, aldeia, nivel_shinobi, num_shuriken, do_damage, steal_chakra)

    ninjas_list.append(ninja_player)
    print(f"agora vamos aprender 3 jutsus!!")
    for i in range(3):
        print(f"Aprenda o jutsu {i + 1}: ")
        jutsu_aprendendo = input("")
        ninja_player.aprender_jutsu(jutsu_aprendendo)

ninjas_list = []
configure_game(ninjas_list)
Madara = Madara("Madara Uchiha", "Aldeia da Folha", "Deus Shinobi", 10, do_damage, steal_chakra)
ninjas_list.append(Madara)
Cenario = Cenario(ninjas_list)
Kaguya_existis = [0]

def play_game(kishimoto_use, Kaguya_existis):
    turno = 1
    while ninjas_list[0].vida > 0 and ninjas_list[1].vida > 0:
        jogador = "Player" if turno % 2 != 0 else "Madara Uchiha"
        if kishimoto_use == 0:
            if jogador == "Player":
                time.sleep(1)
                print("-----------------TURNO DO PLAYER-------------------")
                print(f"Sua vida atual é: {Cenario.ninja_list[0].vida}")
                print(f"Escolha sabiamente os seus movimentos!!!")
                print(f"1.Jogar Shuriken \n2.Socar \n3.Utilizar Jutsu \n4.Reforço \n5.Fugir")
                opcao = int(input())
                match opcao:
                    case 1:
                        time.sleep(0.5)
                        Cenario.ninja_list[0].jogar_shuriken()
                        Cenario.do_damage(Cenario.ninja_list[0], Cenario.ninja_list[0].get_dano_base() - 100)  # Chamando a função do_damage
                        print(f"{Cenario.ninja_list[0].nome} causou {Cenario.ninja_list[0].get_dano_base() - 100} de dano!!")
                    case 2:
                        time.sleep(0.5)
                        Cenario.ninja_list[0].soco()
                        Cenario.do_damage(Cenario.ninja_list[0], Cenario.ninja_list[0].get_dano_base())
                        print(f"{Cenario.ninja_list[0].nome} causou {Cenario.ninja_list[0].get_dano_base()}")
                    case 3:
                        print(f"Qual jutsu voce vai utilizar? \n1.{Cenario.ninja_list[0].jutsu[0]} \n2.{Cenario.ninja_list[0].jutsu[1]} \n3.{Cenario.ninja_list[0].jutsu[2]}")
                        opcao_jutsu = int(input())
                        opcao_jutsu -= 1
                        
                        time.sleep(0.5)
                        Cenario.ninja_list[0].usar_jutsu(Cenario.ninja_list[0].jutsu[opcao_jutsu])
                        time.sleep(0.5)
                        Cenario.do_damage(Cenario.ninja_list[0], Cenario.ninja_list[0].get_dano_base() + 300)  # Chamando a função do_damage
                        time.sleep(0.5)
                        print(f"{Cenario.ninja_list[0].nome} causou {Cenario.ninja_list[0].get_dano_base() + 300} de dano!!\n")
                    case 4:
                        time.sleep(0.5)
                        print(f"KISHIMOTO!! ME AJUDA!!")              
                        acoes_kishimoto = ['Poder Misterioso', 'Poder da Amizade', 'Kaguya']
                        acao_kishimoto = random.choice(acoes_kishimoto)
                        kishimoto_use = 1
                        match acao_kishimoto:
                            case 'Poder Misterioso':
                                time.sleep(0.5)
                                print(f"Você causou sorte! Kishimoto quer acabar logo o anime e lhe causou um poder misterioso!!")  
                                print(f"Dano base aumentado em 500")
                                Cenario.ninja_list[0].set_dano_base(Cenario.ninja_list[0].get_dano_base() + 500)  # Usando o setter
                            case 'Poder da Amizade':
                                time.sleep(0.5)
                                print(f"Kishimoto te ofereceu um filler sobre poder da amizade!!")
                                print(f"+1000 de vida")
                                Cenario.ninja_list[0].vida += 1000
                            case 'Kaguya':
                                time.sleep(0.5)
                                print(f"Sujou! Kishimoto quer mais 100 episodios e liberou um boss novo!!")
                                print(f"Madara morreu! Agora é Kaguya!!")
                                Madara.vida = 0
                                Kaguya_existis[0] += 1
                            case _:
                                print("invalido")
                    case 5:
                        time.sleep(0.5)
                        print(f"{Cenario.ninja_list[0].nome} fugiu")
                        break
                    case _:
                        print("Opção inválida! Escolha um número entre 1 e 5.")
            else:
                time.sleep(1)
                print(f"-----------------TURNO DE {Cenario.ninja_list[1].nome}---------------------")
                time.sleep(0.5)
                print(f"A vida atual de {Cenario.ninja_list[1].nome} é: {Cenario.ninja_list[1].vida}")
                acao_disponivel = ["Shuriken", "Socar", "Jutsu Aleatorio"]
                acao_boss = random.choice(acao_disponivel)
                if acao_boss == "Shuriken":
                    time.sleep(0.5)
                    Cenario.ninja_list[1].jogar_shuriken()
                    time.sleep(0.5)
                    Cenario.do_damage(Cenario.ninja_list[1], Cenario.ninja_list[1].get_dano_base() - 100)  # Chamando a função do_damage
                    time.sleep(0.5)
                    print(f"{Cenario.ninja_list[1].nome} causou {Cenario.ninja_list[1].get_dano_base() - 100} de dano!!!!")
                elif acao_boss == "Socar":
                    time.sleep(0.5)
                    Cenario.ninja_list[1].soco()
                    time.sleep(0.5)
                    Cenario.do_damage(Cenario.ninja_list[1], Cenario.ninja_list[1].get_dano_base())  # Chamando a função do_damage
                    time.sleep(0.5)
                    print(f"{Cenario.ninja_list[1].nome} causou {Cenario.ninja_list[1].get_dano_base()} de dano!!!!")
                    
                else:
                    jutsu_escolhido = random.choice(Cenario.ninja_list[1].jutsu)
                    time.sleep(0.5)
                    Cenario.ninja_list[1].usar_jutsu(jutsu_escolhido)
                    if jutsu_escolhido == Cenario.ninja_list[1].jutsu[0]:
                        time.sleep(0.5)
                        Cenario.do_damage(Cenario.ninja_list[1], Cenario.ninja_list[1].get_dano_base() + 400)  # Chamando a função do_damage
                        print(f"{Cenario.ninja_list[1].nome} causou {Cenario.ninja_list[1].get_dano_base() + 400} de dano!!!")
                    elif jutsu_escolhido == Cenario.ninja_list[1].jutsu[1]:
                        if Cenario.ninja_list[1].nome == 'Madara Uchiha':
                            clone_susanoo = random.choice([0, 1])
                            time.sleep(0.5)
                            if clone_susanoo == 1:
                                time.sleep(0.5)
                                print(f"{Cenario.ninja_list[1].nome} utilizou Susanoo com clones! Acerto Crítico!")
                                time.sleep(0.5)
                                Cenario.do_damage(Cenario.ninja_list[1], Cenario.ninja_list[1].get_dano_base()*4)  # Chamando a função do_damage
                            else:
                                time.sleep(0.5)
                                Cenario.do_damage(Cenario.ninja_list[1], Cenario.ninja_list[1].get_dano_base()*2)  # Chamando a função do_damage
                        time.sleep(0.5)
                        Cenario.do_damage(Cenario.ninja_list[1], Cenario.ninja_list[1].get_dano_base() + 400)  # Chamando a função do_damage
                        print(f"{Cenario.ninja_list[1].nome} causou {Cenario.ninja_list[1].get_dano_base() + 400} de dano!!!")
                    elif jutsu_escolhido == Cenario.ninja_list[1].jutsu[2]:
                        if Cenario.ninja_list[1].nome == "Kaguya Otsutsuki":
                            time.sleep(0.5)
                            print(f"Kaguya roubou seu chakra: -{Cenario.ninja_list[1].get_dano_base()} pra você!!!")
                            Cenario.steal_chakra(Cenario.ninja_list[1], Cenario.ninja_list[1].get_dano_base())  # Chamando a função do_damage
                        else:
                            time.sleep(0.5)
                            Cenario.do_damage(Cenario.ninja_list[1], Cenario.ninja_list[1].get_dano_base() + 800)  # Chamando a função do_damage
                            print(f"{Cenario.ninja_list[1].nome} causou {Cenario.ninja_list[1].get_dano_base() + 800} de dano!!!")
                    else:
                        time.sleep(0.5)
                        Cenario.do_damage(Cenario.ninja_list[1], Cenario.ninja_list[1].get_dano_base() + 300)
                        print(f"{Cenario.ninja_list[1].nome} causou {Cenario.ninja_list[1].get_dano_base() + 300} de dano!!!")
        else:
            if jogador == "Player":
                time.sleep(1)
                print("-----------------TURNO DO PLAYER-------------------")
                print(f"Sua vida atual é: {Cenario.ninja_list[0].vida}")
                print(f"Escolha sabiamente os seus movimentos!!!")
                print(f"1.Jogar Shuriken \n2.Socar \n3.Utilizar Jutsu \n4.Fugir")
                opcao = int(input())
                match opcao:
                    case 1:
                        time.sleep(0.5)
                        Cenario.ninja_list[0].jogar_shuriken()
                        Cenario.do_damage(Cenario.ninja_list[0], Cenario.ninja_list[0].get_dano_base() - 100)  # Chamando a função do_damage
                        print(f"{Cenario.ninja_list[0].nome} causou {Cenario.ninja_list[0].get_dano_base() - 100} de dano!!")
                    case 2:
                        time.sleep(0.5)
                        Cenario.ninja_list[0].soco()
                        Cenario.do_damage(Cenario.ninja_list[0], Cenario.ninja_list[0].get_dano_base())
                        print(f"{Cenario.ninja_list[0].nome} causou {Cenario.ninja_list[0].get_dano_base()} de dano!!")
                    case 3:
                        print(f"Qual jutsu voce vai utilizar? \n1.{Cenario.ninja_list[0].jutsu[0]} \n2.{Cenario.ninja_list[0].jutsu[1]} \n3.{Cenario.ninja_list[0].jutsu[2]}")
                        opcao_jutsu = int(input())
                        opcao_jutsu -= 1
                        
                        time.sleep(0.5)
                        Cenario.ninja_list[0].usar_jutsu(Cenario.ninja_list[0].jutsu[opcao_jutsu])
                        time.sleep(0.5)
                        Cenario.do_damage(Cenario.ninja_list[0], Cenario.ninja_list[0].get_dano_base() + 300)  # Chamando a função do_damage
                        time.sleep(0.5)
                        print(f"{Cenario.ninja_list[0].nome} causou {Cenario.ninja_list[0].get_dano_base() + 300} de dano!!\n")
                    case 4:
                        time.sleep(0.5)
                        print(f"{Cenario.ninja_list[0].nome} fugiu")
                        break
                    case _:
                        print("Opção inválida! Escolha um número entre 1 e 5.")
            else:
                time.sleep(1)
                print(f"-----------------TURNO DE {Cenario.ninja_list[1].nome}---------------------")
                time.sleep(0.5)
                print(f"A vida atual de {Cenario.ninja_list[1].nome} é: {Cenario.ninja_list[1].vida}")
                acao_disponivel = ["Shuriken", "Socar", "Jutsu Aleatorio"]
                acao_boss = random.choice(acao_disponivel)
                if acao_boss == "Shuriken":
                    time.sleep(0.5)
                    Cenario.ninja_list[1].jogar_shuriken()
                    time.sleep(0.5)
                    Cenario.do_damage(Cenario.ninja_list[1], Cenario.ninja_list[1].get_dano_base())  # Chamando a função do_damage
                    time.sleep(0.5)
                    print(f"{Cenario.ninja_list[1].nome} causou {Cenario.ninja_list[1].get_dano_base() - 100} de dano!!!!")
                elif acao_boss == "Socar":
                    time.sleep(0.5)
                    Cenario.ninja_list[1].soco()
                    time.sleep(0.5)
                    Cenario.do_damage(Cenario.ninja_list[1], Cenario.ninja_list[1].get_dano_base())  # Chamando a função do_damage
                    time.sleep(0.5)
                    print(f"{Cenario.ninja_list[1].nome} causou {Cenario.ninja_list[1].get_dano_base()} de dano!!!!")
                else:
                    jutsu_escolhido = random.choice(Cenario.ninja_list[1].jutsu)
                    time.sleep(0.5)
                    Cenario.ninja_list[1].usar_jutsu(jutsu_escolhido)
                    if jutsu_escolhido == Cenario.ninja_list[1].jutsu[0]:
                        time.sleep(0.5)
                        Cenario.do_damage(Cenario.ninja_list[1], Cenario.ninja_list[1].get_dano_base() + 400)  # Chamando a função do_damage
                        print(f"{Cenario.ninja_list[1].nome} causou {Cenario.ninja_list[1].get_dano_base() + 400} de dano!!!")
                    elif jutsu_escolhido == Cenario.ninja_list[1].jutsu[1]:
                        if Cenario.ninja_list[1].nome == 'Madara Uchiha':
                            clone_susanoo = random.choice([0, 1])
                            time.sleep(0.5)
                            if clone_susanoo == 1:
                                time.sleep(0.5)
                                print(f"{Cenario.ninja_list[1].nome} utilizou Susanoo com clones! Acerto Crítico!")
                                time.sleep(0.5)
                                Cenario.do_damage(Cenario.ninja_list[1], Cenario.ninja_list[1].get_dano_base()*3)  # Chamando a função do_damage
                                print(f"{Cenario.ninja_list[1].nome} causou {Cenario.ninja_list[1].get_dano_base()*3} de dano!!!")
                            else:
                                time.sleep(0.5)
                                Cenario.do_damage(Cenario.ninja_list[1], Cenario.ninja_list[1].get_dano_base() + 600)  # Chamando a função do_damage
                                print(f"{Cenario.ninja_list[1].nome} causou {Cenario.ninja_list[1].get_dano_base() + 600} de dano!!!")
                        time.sleep(0.5)
                        Cenario.do_damage(Cenario.ninja_list[1], Cenario.ninja_list[1].get_dano_base() + 400)  # Chamando a função do_damage
                    elif jutsu_escolhido == Cenario.ninja_list[1].jutsu[2]:
                        if Cenario.ninja_list[1].nome == "Kaguya Otsutsuki":
                            time.sleep(0.5)
                            print(f"Kaguya roubou seu chakra: -{Cenario.ninja_list[1].get_dano_base()} pra você!!!")
                            Cenario.steal_chakra(Cenario.ninja_list[1], Cenario.ninja_list[1].get_dano_base())  # Chamando a função do_damage
                        else:
                            time.sleep(0.5)
                            Cenario.do_damage(Cenario.ninja_list[1], Cenario.ninja_list[1].get_dano_base() + 800)  # Chamando a função do_damage
                            print(f"{Cenario.ninja_list[1].nome} causou {Cenario.ninja_list[1].get_dano_base() + 800} de dano!!!")
        turno += 1
        
play_game(0, Kaguya_existis)
     
if ninjas_list[0].vida <= 0:
    print(f"Game Over! {ninjas_list[0].nome} foi de vasco!!!")
elif Madara.vida <= 0 and Kaguya_existis[0] == 1:
    ninjas_list.pop()
    Kaguya = Kaguya("Kaguya Otsutsuki", "Outro Mundo","Deusa Coelho", 1000, do_damage,steal_chakra)
    ninjas_list.append(Kaguya)
    play_game(1,Kaguya_existis)
    
    if ninjas_list[0].vida <= 0:
        print(f"Gamer Over! {ninjas_list[0].nome} foi de vasco!!!")
    else:
        print(f"Grande Herói do mundo ninja! Derrotou Kaguya com {ninjas_list[0].vida} pontos de vida!!")
    
else:
    print(f"Grande Herói do mundo ninja! Venceu com {ninjas_list[0].vida} pontos de vida")