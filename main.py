import no

a = no.no(0)  #        a
b = no.no(1)  #      /   \
c = no.no(2)  #     b     c
              #    /
d = no.no(3)  #   d

a.add_filho(b) #b deixa de ser raiz
a.add_filho(c) #c deixa de ser raiz
b.add_filho(d)

x = b.busca_root() # Buscando a raiz da árvore para iniciar a busca em pós ordem

x.delete(0)

x = b.busca_root()

print(x.valor)

y = x.busca_pos_ordem(0)
