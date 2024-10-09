from animal import Animal, Mamifero, Reptil

animal1 = Mamifero("Cachorro", 2)
animal2 = Mamifero("Leão", 4)
animal3 = Reptil("Cobra", 1)

animal1.exibirInfo()
animal1.som("Roar")
animal1.alimentarFilhotes()

animal2.exibirInfo()
animal2.som("Miau")
animal2.alimentarFilhotes()

animal3.exibirInfo()
animal3.som("Hiss")
animal3.mudarPele()

