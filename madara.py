from ninja import Ninja

class Madara(Ninja):
    def __init__(self, nome, regiao, nivel, shuriken, damage_callback, steal_callback):
        super().__init__(nome, regiao, nivel, shuriken, damage_callback, steal_callback)
        self.jutsu = [
            "Estilo Fogo: Grande Aniquilação por Fogo",
            "Susanoo",
            "Tengai Shinsei",
            "Mangekyou Sharingan"
        ]
        self.vida = 3000
        self.__dano_base = 300  # Variável privada

    # Getter para acessar dano_base
    def get_dano_base(self):
        return self.__dano_base

    # Setter para modificar dano_base
    def set_dano_base(self, novo_dano):
        if novo_dano >= 0:  # Evita valores negativos
            self.__dano_base = novo_dano
        else:
            print("O dano base não pode ser negativo!")
