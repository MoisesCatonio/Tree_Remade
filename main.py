import no

a = no.no(0)  #        a
b = no.no(1)  #      /   \
c = no.no(2)  #     b     c
              #    /  \
d = no.no(3)  #   d    e
e = no.no(4)  #  /
f = no.no(5)  # f


a.add_filho(b) #b deixa de ser raiz, se torna filho de a.
a.add_filho(c) #c deixa de ser raiz, se torna filho de a.
a.add_filho(d) #d deixa de ser raiz, se torna filho de b.
b.add_filho(e) #e deixa de ser raiz, se torna filho de b.
d.add_filho(f) #f deixa de ser raiz, se torna filho de d.

x = b.busca_root() # Buscando a raiz da árvore para iniciar a busca em pós ordem
print(x.valor)


#x.delete(3)

x = b.busca_root()
print(x.valor)

x.busca_pos_ordem(0)
x.busca_pre_ordem(4)
x.busca_em_ordem(4)

x.printer()