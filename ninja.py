class Ninja:
    def __init__(self, nome, regiao, nivel, shuriken, damage_callback, steal_callback):
        self.nome = nome
        self.regiao = regiao
        self.nivel = nivel
        self.shuriken = shuriken
        self.jutsu = []
        self.vida = 1000
        self.__dano_base = 200  # Agora é uma variável privada
        self.damage_callback = damage_callback
        self.steal_callback = steal_callback

    def jogar_shuriken(self):
        if self.shuriken == 0:
            print(f"{self.nome} não tem mais shurikens")
        else:
            print(f"{self.nome} jogou uma shuriken!")
            self.shuriken -= 1

    def view_shuriken(self):
        print(f"{self.nome} tem: {self.shuriken} shurikens!")

    def soco(self):
        print(f"{self.nome} utilizou combo básico!!")

    def aprender_jutsu(self, nome_jutsu):
        print(f"{self.nome} aprendeu o jutsu: {nome_jutsu}")
        self.jutsu.append(nome_jutsu)

    def view_jutsu(self):
        for i in self.jutsu:
            print(f"Os jutsus disponíveis para {self.nome} são: {i} |")

    def do_damage(self, dano):
        self.vida -= dano

    def steal_chakra(self, dano):
        self.__dano_base -= dano

    def usar_jutsu(self, nome_jutsu):
        if nome_jutsu in self.jutsu:
            print(f"{self.nome} utilizou {nome_jutsu}")

    # Getter para acessar dano_base
    def get_dano_base(self):
        return self.__dano_base

    # Setter para modificar dano_base
    def set_dano_base(self, novo_dano):
        self.__dano_base = novo_dano

