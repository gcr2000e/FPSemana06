import json

class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, inimigo):
        inimigo.vida -= self.ataque
        print(f"{self.nome} Ataca {inimigo.nome} e Causa {self.ataque} de Dano!")

    def __str__(self):
        return f"{self.nome} {self.vida}"

class Guerreiro(Personagem):
    pass

class Mago(Personagem):
    pass

class Arqueiro(Personagem):
    pass

def importar_personagens(caminho):
    """
        Função que importa personagens a partir de um ficheiro JSON.
        O ficheiro contém uma lista de personagens com informações de nome, vida, ataque e classe.
        - caminho: Caminho para o ficheiro JSON que contém os dados dos personagens.
        Retorna:
        - lista de personagens.
        - quantidade total de personagens importados.
    """
    pass

def ordenar_personagens_por_vida(personagens):
    """
        Função que ordena a lista de personagens de acordo com os pontos de vida (do menor para o maior).
        - personagens: Lista de personagens.
        Retorna:
        - lista de personagens ordenada por vida.
    """
    pass

personagens, num_personagens = importar_personagens('personagens.json')
print(f"{num_personagens} Personagens Entram em Batalha!")

personagens = ordenar_personagens_por_vida(personagens)

print(personagens[0])
print(personagens[1])
print(personagens[2])

personagens[0].atacar(personagens[1])
print(personagens[1])

personagens[1].atacar(personagens[2])
print(personagens[2])

personagens[2].atacar(personagens[0])
print(personagens[0])

personagens[0].especial()
print(personagens[0])

personagens[1].especial([personagens[0], personagens[1]])
print(personagens[0])
print(personagens[1])

personagens[2].especial(personagens[1])
print(personagens[1])