class no:
    """Classe que representa os nós, atributos presentes: valor, filho_esq, filho_dir."""
    def __init__(self, valor=None):
        """Construtor da classe"""
        self.valor = valor
        self.filho_esq = None
        self.filho_dir = None
        self.pai = None
        self.isroot = 1
        #Todos os nós são iniciados como possíveis raízes, até que na adição como filhos,
        #tem seu atributo de raiz alterado;
    
    def add_filho(self, no_filho):
        if self.filho_esq == None:
            self.filho_esq = no_filho
            self.filho_esq.isroot = 0
            self.filho_esq.pai = self
        elif self.filho_dir == None:
            self.filho_dir = no_filho
            self.filho_dir.isroot = 0
            self.filho_dir.pai = self
        else:
            print("O pai já possui 2 filhos, atribuição cancelada!")

    def busca_root(self):
        if(self.isroot == 1):
            print("Raiz encontrada! Retornando nó!")
            return self
        else:
            return self.pai.busca_root() 