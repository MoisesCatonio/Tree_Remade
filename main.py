import no

a = no.no(0)  #     a
b = no.no(1)  #   /   \
c = no.no(2)  #  b     c

d = no.no(3)  #     d

a.add_filho(b) #b deixa de ser raiz
a.add_filho(c) #c deixa de ser raiz

print(b.isroot)
print(c.isroot)
print(d.isroot)

x = b.busca_root() # Buscando a raiz da árvore para iniciar a busca em pós ordem
y = x.busca_pos_ordem(2)

print(y.valor)