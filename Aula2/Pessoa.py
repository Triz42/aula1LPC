class Residencial():
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        
    def __str__(self):
        return 'O(A) {} fica situado no(a) {}'.format(self.nome, self.endereco)

class Apartamento(Residencial):
    def __init__(self, nome, endereco, andar):
        super().__init__(nome, endereco)
        self.andar = andar
    def __str__(self):
        return 'O(A) {} situado no(a) {} tem {} andar(es)'.format(self.nome, self.endereco, self.andar)
    
class Inquilino():
    nome = ""
    renda = ""
    def __init__(self, nome, renda):
        self.nome = nome
        self.renda = renda
        self.endereco = Apartamento("R. Azul","105 N",5)
    def __str__(self):
        return 'O(A) {} com renda de {} por mes mora no(a) {}'.format(self.nome, self.renda, self.endereco)
