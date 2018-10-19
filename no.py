class no:
    """Classe que representa os nós, atributos presentes: valor, filho_esq, filho_dir."""
    def __init__(self, valor=None):
        """Construtor da classe"""
        self.valor = valor
        self.filho_esq = None
        self.filho_dir = None
        self.pai = None
        self.isroot = 1
        self.acessado = 0
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

    def zerar_acessos(self):
        if(self.filho_esq != None and self.filho_esq.acessado == 1):
            self.filho_esq.zerar_acessos()
        if(self.filho_dir != None and self.filho_dir.acessado == 1):
             self.filho_dir.zerar_acessos()
        self.acessado = 0

    def busca_pos_ordem(self, valor):
        if(self.filho_esq != None and self.filho_esq.acessado == 0):
            return self.filho_esq.busca_pos_ordem(valor)
        if(self.filho_dir != None and self.filho_dir.acessado == 0):
             return self.filho_dir.busca_pos_ordem(valor)
        if(self.valor == valor):
            print("Elemento encontrado! Retornando nó")
            self.busca_root().zerar_acessos()
            return self
        else:
            self.acessado = 1
            if(self.pai != None):
                return self.pai.busca_pos_ordem(valor)
        self.zerar_acessos()
        return