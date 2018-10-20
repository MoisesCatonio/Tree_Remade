import no

a = no.no(0)  #        a
b = no.no(1)  #      /   \
c = no.no(2)  #     b     c
              #    /
d = no.no(3)  #   d

a.add_filho(b) #b deixa de ser raiz, se torna filho de a.
a.add_filho(c) #c deixa de ser raiz, se torna filho de a.
a.add_filho(d) #d deixa de ser raiz, se torna filho de b.

x = b.busca_root() # Buscando a raiz da árvore para iniciar a busca em pós ordem
print(x.valor)


x.delete(3)

x = b.busca_root()
print(x.valor)

x.busca_pos_ordem(0)
x.busca_pos_ordem(2)

x.printer()