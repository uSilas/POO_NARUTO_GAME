from ninja import Ninja

class Jinchuuriki(Ninja):
    def __init__(self, nome, regiao, nivel, shuriken, numero_caudas, damage_callback, steal_callback):
        super().__init__(nome, regiao, nivel, shuriken, damage_callback, steal_callback)
        self.numero_caudas = numero_caudas
        self.bijuus = ['Shukaku', 'Matatabi', 'Isobu', 'Son Goku', 'Kokuo', 'Saiken', 'Chomei', 'Gyuki', 'Kurama']
        self.vida = 3000
        self.__dano_base = 200  # Variável privada

    def view_bijuu(self):
        for index, valor in enumerate(self.bijuus):
            if index + 1 == self.numero_caudas:
                print(f"A bijuu do Jinchuuriki {self.nome} é {valor}")

    # Getter para acessar dano_base
    def get_dano_base(self):
        return self.__dano_base

    # Setter para modificar dano_base
    def set_dano_base(self, novo_dano):
        if novo_dano >= 0:  # Evita valores negativos
            self.__dano_base = novo_dano
        else:
            print("O dano base não pode ser negativo!")
