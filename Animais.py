class Animais:
    def __init__(self, tipo, som):
        self.tipo = tipo
        self.som = som

    def Reproducao(self):
        if self.tipo == "Ave":
            print("O seu animal é: Ovíparo")
        elif self.tipo == "Mamífero":
            print("O seu animal é: Placentário")
        else:
            print("Tipo Inválido")

Gato = Animais("Mamífero", "Miau")
Passarinho = Animais("Ave", "Piu Piu")
Planta = Animais ("Briófita", "")
Gato.Reproducao(), Planta.Reproducao()
