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
    
    nome = ""
    vida = 0
    ataque = 0

    def __init__(self, nome, vida, ataque):
        
     self.nome = nome
     self.vida = vida
     self.ataque = ataque
    
    def especial(self, inimigo):
        inimigo.vida -=  self.ataque + 15
        print(f"{self.nome} usa Golpe Poderoso em {inimigo.nome} e Causa 30 de Dano!")

class Mago(Personagem):

    nome = ""
    vida = 0
    ataque = 0

    def __init__(self, nome, vida, ataque):
        
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
    
    def especial(self):
        self.vida += 25
        print(f"{self.nome} usa Cura e Ganha 25 Pontos de Vida!")


class Arqueiro(Personagem):
    
    nome = ""
    vida = 0
    ataque = 0

    def __init__(self, nome, vida, ataque):
       
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
    
    def especial(self, inimigos):
        for inimigo in inimigos:
            if inimigo != self:
                inimigo.vida -= 15
        print(f"{self.nome} usa Chuva de Flechas e Causa 15 de Dano a Todos os Inimigos!")

def importar_personagens(path):
   with open(path, 'r') as file:
        info = json.load(file)

   personagens = []

   for data in info:
        if data["classe"] == "Guerreiro":
            personagens.append(Guerreiro(data["nome"], data["vida"], data["ataque"]))

        elif data["classe"] == "Mago":
            personagens.append(Mago(data["nome"], data["vida"], data["ataque"]))

        else: 
            data["classe"] == "Arqueiro"
            personagens.append(Arqueiro(data["nome"], data["vida"], data["ataque"]))

   return personagens, len(personagens)
    

def ordenar_personagens_por_vida(personagens):
    return sorted(personagens, key=lambda p: p.vida)

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