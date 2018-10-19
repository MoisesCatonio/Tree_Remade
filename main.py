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

b.busca_root()

print(x.valor)