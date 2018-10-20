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
    

    #Destrutor para informar quais nós instanciados morreram ao final do programa
    # def __del__(self):
    #     print(self.valor)
    #     print("Morreu")
    #     self.valor = None
    #     self.filho_esq = None
    #     self.filho_dir = None
    #     self.pai = None
    #     self.isroot = None
    #     self.acessado = None

    def remove_references(self):
        self.valor = None
        self.filho_esq = None
        self.filho_dir = None
        self.pai = None
        self.isroot = None
        self.acessado = None

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
            self.filho_esq.add_filho(no_filho)
            print("O pai já possui 2 filhos, passando para o nó mais a esquerda da sub arvore!")

    def F_e_o_F_d(self):
        if(self.pai.filho_dir != None and self.valor == self.pai.filho_dir.valor):
            self.pai.filho_dir = None
        else:
            self.pai.filho_esq = None

    def busca_root(self):
        if(self.isroot == 1):
            return self
        else:
            return self.pai.busca_root()

    def zerar_acessos(self):
        if(self.filho_esq != None and self.filho_esq.acessado == 1):
            self.filho_esq.zerar_acessos()
        if(self.filho_dir != None and self.filho_dir.acessado == 1):
             self.filho_dir.zerar_acessos()
        self.acessado = 0

    def printer(self):
        if(self.filho_esq != None):
            self.filho_esq.printer()
        if(self.filho_dir != None):
            self.filho_dir.printer()
        if(self.isroot == 0):
            print("Nó com valor "+ str(self.valor) + ", filho do nó de valor " + str(self.pai.valor)+".") 
        else:
            print("Nó raiz, de valor " + str(self.valor))

    def busca_pos_ordem(self, valor):
        if(self.filho_esq != None and self.filho_esq.acessado == 0):
            return self.filho_esq.busca_pos_ordem(valor)
        if(self.filho_dir != None and self.filho_dir.acessado == 0):
             return self.filho_dir.busca_pos_ordem(valor)
        if(self.valor == valor):
            print("Elemento com valor "+ str(valor) +" encontrado! Retornando nó")
            self.busca_root().zerar_acessos()
            return self
        else:
            self.acessado = 1
            if(self.pai != None):
                return self.pai.busca_pos_ordem(valor)
        self.zerar_acessos()
        print("Valor "+ str(valor) +" não encontrado na árvore")
        return
    
    def delete(self, valor):
        to_remove = self.busca_pos_ordem(valor)

        if(to_remove.isroot == 0):
            if(to_remove.filho_esq != None and to_remove.filho_dir != None):
                to_remove.pai.filho_esq = to_remove.filho_esq
                to_remove.filho_esq.pai = to_remove.pai
                to_remove.filho_esq.add_filho(to_remove.filho_dir)
                to_remove.F_e_o_F_d()
                to_remove.remove_references()
                return
            elif(to_remove.filho_esq != None and to_remove.filho_dir == None):
                to_remove.pai.filho_esq = to_remove.filho_esq
                to_remove.filho_esq.pai = to_remove.pai
                to_remove.F_e_o_F_d()
                to_remove.remove_references()
                return
            else:
                to_remove.F_e_o_F_d()
                to_remove.remove_references()
                return
        else:
            if(to_remove.filho_esq != None and to_remove.filho_dir != None):
                to_remove.filho_esq.pai = None
                to_remove.filho_esq.isroot = 1
                to_remove.filho_esq.add_filho(to_remove.filho_dir)
                to_remove.remove_references()
                return
            elif(to_remove.filho_esq != None and to_remove.filho_dir == None):
                to_remove.filho_esq.pai = None
                to_remove.filho_esq.isroot = 1
                to_remove.remove_references()
                return
            else:
                to_remove.remove_references()
                return