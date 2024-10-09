from jogo import Personagem, Jogador, Monstro

personagem1 = Personagem("Kili, o Destemido")
jogador1 = Jogador("Kili", "Elfo", "Poção de invisibilidade, Poção de Cura, Escudo de Madeira, Grimoire de Magia")
monstro1 = Monstro("Morgul, o Enigma Desvanecido", "Orc", 60)

personagem1.atacar()

jogador1.detalhes()
jogador1.usarHabilidade("Flecha Veloz")
jogador1.coletarItem("Poção de Cura")

monstro1.atacar()
monstro1.exibirInformacoes()
monstro1.invocarAliado("Graxius,Espectro da Morte", "Demônio")
monstro1.defender()


