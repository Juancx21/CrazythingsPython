class matriz:
    def __init__(self, n, m):
        self.n = n #columnas
        self.m = m #filas
        self.array = []
        self.rellenar()

    def rellenar(self):
        fila = []
        for i in range(self.m):
            for j in range(self.n):
                if i >= 1:
                    fila.append((i+1)*(j+1))
                else:
                    fila.append((j+1)*1)
            self.array.append(fila)
            fila = []

    def imprimir(self):
        print("#",*self.array[0], sep="\t")
        print("-"*(self.n*10))
        for i in range(self.m):
            print("{} |".format(i+1),*self.array[i], sep="\t")

# matriz(numero de columnas, numero de filas)
m = matriz(int(input("Ingrese el número de columnas que desee: ")),int(input("Ingrese el número de filas que desee: "))) 
m.imprimir() 