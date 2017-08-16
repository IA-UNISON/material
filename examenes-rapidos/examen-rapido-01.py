
# Vamos a generar 3 listas que parecerían iguales
lista_1 = [1, 2, 3, "toto", ["a", "b", "c"]]
lista_2 = lista_1
lista_3 = lista_1[:]

lista_2[0] = "XXX"
print(lista_2)

# Coloca lo que piensas que debería salir con
# print(lista_1)  -->  
# print(lista_3)  -->  

# Ejemplo:
# print(lista_2)  -->  ['XXX', 2, 3, 'toto', ['a', 'b', 'c']

lista_3[-1][0] = 1000
print(lista_3)

# Coloca lo que piensas que debería salir con
# print(lista_1)  -->
# print(lista_2)  -->

# Ejemplo:
# print(lista_3)  -->  [1, 2, 3, 'toto', [1000, 'b', 'c']]

# Ahora ejecuta los programas y revisa lo que sale de acuerdo a lo que pusiste
# y explica porqué pasa de esa manera.


class coordenadas:
    def __init__(self, x=0, y=0):
        "Inicializa un objet coordenadas"
        self.x = x
        self.y = y

    def __str__(self):
        return "\n\tCoordenada x = {}\n\tCoordenada y = {}".format(self.x, self.y)


a = coordenadas(3, 4)
b = a
b.x = 100

print("b = " + str(b))

# Coloca aqui lo que crees que saldrá si se ejecuta
# print("a = " + str(a))

