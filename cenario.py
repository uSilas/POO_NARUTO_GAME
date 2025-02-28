class Cenario:
    def __init__(self, ninja_list):
        self.ninja_list = ninja_list

    def do_damage(self, ninja_atual, dano):
        for ninja in self.ninja_list:
            if ninja_atual != ninja:
                ninja.do_damage(dano)
                print(f"{ninja_atual.nome} deu dano em: {ninja.nome}")

    def steal_chakra(self, ninja_atual, dano):
        for ninja in self.ninja_list:
            if ninja_atual != ninja:
                novo_dano = ninja.get_dano_base() - dano  # Obtém o dano atual e reduz
                ninja.set_dano_base(novo_dano) 
                print(f"{ninja_atual.nome} roubou chakra de {ninja.nome}")
