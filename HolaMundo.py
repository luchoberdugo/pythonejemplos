"""
a, b = 5, 3
c = "hola "
d = "Mundo"
e = "HOLA MUNDO"

l = [1.54, "Hola", "Mundo", 3]
l2 = [a, b, c, d, e]
l3 = [5, 1, 4, 2, 3]
l4 = ["a", "b", "c"]

d = {1 : "a", 2 : "b", 3 : "c"}
d[4] = "hey"

t = 1, 2, 3
g, h, j = t

print(g, h, j)

s = {1, 3, 2}
s.add(4)
s.add(1)
print(s)

l.append("gato")
l.insert(1, "perro")
l.remove(1.54)
del l[0]
l2[1:1] = ["gato", "perro"]


print(l[1])
print(l2)
print(len(l2))
print("adios" in l2)
print(sum(l3))
print(sorted(l3))
print(len(d))
print(1 in d)
print(d.keys())
print(d.values())
"""
a, b = 1, 2
c = a / b
print(type(c))



