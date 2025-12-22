class casa:
    def __init__(self, cor, janelas, portas, quartos):
        
        self.cor = cor
        self.janelas = janelas
        self.portas = portas
        self.quartos = quartos

    def quantidade(self):
        print(f'essa casa tem {self.janelas} janelas, {self.portas} portas, {self.quartos} quartos e a cor dela é {self.cor}')


casinha = casa('verde', 8, 7, 3)
casita = casa('preto', 3, 9, 2)
casarao = casa('branco', 10, 14, 5)
mansao = casa('azul', 40, 21, 12)

casinha.quantidade()
casita.quantidade()
casarao.quantidade()
mansao.quantidade()