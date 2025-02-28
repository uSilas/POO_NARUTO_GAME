from ninja import Ninja

class Kaguya(Ninja):
    def __init__(self, nome, regiao, nivel, shuriken, damage_callback, steal_callback):
        super().__init__(nome, regiao, nivel, shuriken, damage_callback, steal_callback)
        self.jutsu = [
            "Shinra Tensei",
            "Esfera do Caminho da Verdade",
            "Absorção de Chakra",
            "Agulha de Cabelo do Coelho"
        ]
        self.vida = 4000
        self.__dano_base = 500  # Variável privada

    # Getter para acessar dano_base
    def get_dano_base(self):
        return self.__dano_base

    # Setter para modificar dano_base
    def set_dano_base(self, novo_dano):
        if novo_dano >= 0:  # Evita valores negativos
            self.__dano_base = novo_dano
        else:
            print("O dano base não pode ser negativo!")
